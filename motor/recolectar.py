"""
RADAR — recolector diario.

Recorre las búsquedas del config, guarda el scrape CRUDO y las MÉTRICAS por separado
(si cambia el criterio, la historia no se pierde), y calcula la TEMPERATURA: el delta de
anuncios activos por anunciante contra la corrida anterior.

Uso:  python recolectar.py [--sin-anunciantes] [--limite N]

Salida:
  datos/crudo/AAAA-MM-DD.json      scrape completo del día
  datos/metricas/AAAA-MM-DD.json   métricas del día
  datos/historico.csv              una fila por búsqueda por día (se agrega)
  datos/anunciantes.csv            una fila por anunciante por día (la temperatura)
  datos/resumen.md                 el parte del día, en texto
"""
import argparse, csv, json, pathlib, re, sys, time
from datetime import date, datetime
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(__file__).resolve().parent
CFG = json.loads((BASE / "config.json").read_text(encoding="utf-8"))
DATOS = BASE / CFG.get("dir_datos", "datos")
HOY = date.today().isoformat()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

MESES = {"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,"jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}

EXTRACT = """() => {
  const pat = /Identificador de la biblioteca:?\\s*(\\d+)/;
  const divs = [...document.querySelectorAll('div')].filter(d => pat.test(d.textContent || ''));
  const mejor = {};
  divs.forEach(d => {
    const m = (d.textContent || '').match(pat);
    if (!m) return;
    const id = m[1], L = (d.textContent || '').length;
    if (!mejor[id] || L < mejor[id].L) mejor[id] = { el: d, L: L };
  });
  return Object.entries(mejor).map(([id, o]) => {
    let cur = o.el, card = null;
    for (let i = 0; i < 40 && cur.parentElement; i++) {
      cur = cur.parentElement;
      if ([...cur.querySelectorAll('img')].some(x => (x.src || '').includes('fbcdn'))) { card = cur; break; }
    }
    const raiz = card || o.el;
    const imgs = card ? [...card.querySelectorAll('img')]
        .filter(x => (x.src || '').includes('fbcdn'))
        .map(x => ({ url: x.src, area: (x.naturalWidth || 0) * (x.naturalHeight || 0) }))
        .sort((a, b) => b.area - a.area) : [];
    return { id: id, texto: raiz.innerText || '', imgs: imgs };
  });
}"""


def parsear(texto):
    """Del texto de la tarjeta saca anunciante, fecha de inicio, dominio y precio."""
    anunciante = dominio = precio = ""
    inicio = None
    lineas = [l.strip() for l in texto.split("\n")]
    for i, l in enumerate(lineas):
        if l == "Publicidad" and i > 0:
            anunciante = lineas[i - 1]
        m = re.search(r"En circulaci[oó]n desde el (\d{1,2}) (\w{3}) (\d{4})", l)
        if m:
            try:
                inicio = date(int(m.group(3)), MESES.get(m.group(2)[:3].lower(), 1), int(m.group(1)))
            except Exception:
                pass
        md = re.search(r"([a-z0-9-]+\.(?:com|ar|net|me|app|store|site|online|shop|uy|cl|mx|co|es)(?:\.ar)?)", l, re.I)
        if md and not dominio and "facebook" not in md.group(1).lower():
            dominio = md.group(1).lower()
        mp = re.search(r"(?:\$|ARS|MXN)\s?([\d.,]{3,})", l)
        if mp and not precio:
            precio = mp.group(0).strip()
    return anunciante.strip(), inicio, dominio, precio


def dias_desde(d):
    return (date.today() - d).days if d else None


def cargar_anterior():
    """La corrida anterior, para calcular el delta."""
    metricas = sorted((DATOS / "metricas").glob("*.json"))
    anterior = None
    for p in reversed(metricas):
        if p.stem != HOY:
            anterior = json.loads(p.read_text(encoding="utf-8"))
            break
    anunciantes = {}
    csv_ant = DATOS / "anunciantes.csv"
    if csv_ant.exists():
        filas = list(csv.DictReader(csv_ant.open(encoding="utf-8")))
        fechas = sorted({f["fecha"] for f in filas if f["fecha"] != HOY})
        if fechas:
            ult = fechas[-1]
            for f in filas:
                if f["fecha"] == ult:
                    anunciantes[f["clave"]] = {"fecha": ult, "anuncios": int(f["anuncios"])}
    return anterior, anunciantes


def contar_anunciante(pg, ad_id):
    """Abre la ficha de un anuncio y devuelve (anunciante, anuncios_activos_del_anunciante)."""
    url = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
           f"&country=ALL&id={ad_id}")
    pg.goto(url, wait_until="domcontentloaded", timeout=90000)
    pg.wait_for_timeout(CFG.get("espera_ficha_ms", 6000))
    texto = pg.evaluate("() => document.body.innerText") or ""
    anunciante = ""
    m = re.search(r"~?\s*([\d.,]+)\s+resultados", texto)
    count = None
    if m:
        try:
            count = int(re.sub(r"[.,]", "", m.group(1)))
        except Exception:
            pass
    ma = re.search(r"(?:Ver todos los anuncios de|Anuncios de)\s*\n?\s*(.+)", texto)
    if ma:
        anunciante = ma.group(1).strip()[:60]
    return anunciante, count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-anunciantes", action="store_true", help="no contar anuncios por anunciante")
    ap.add_argument("--limite", type=int, default=0, help="limitar cantidad de búsquedas")
    args = ap.parse_args()

    (DATOS / "crudo").mkdir(parents=True, exist_ok=True)
    (DATOS / "metricas").mkdir(parents=True, exist_ok=True)

    busquedas = CFG["busquedas"][:args.limite] if args.limite else CFG["busquedas"]
    anterior, temp_ayer = cargar_anterior()

    t0 = time.time()
    resultados, anunciantes_hoy = [], {}

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(locale="es-AR", user_agent=UA)
        pg = ctx.new_page()

        for kw, pais in busquedas:
            url = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
                   f"&country={pais}&q={kw.replace(' ', '+')}"
                   "&search_type=keyword_unordered&media_type=all")
            print(f"[{datetime.now():%H:%M:%S}] {kw} ({pais}) ...", flush=True)
            try:
                pg.goto(url, wait_until="domcontentloaded", timeout=90000)
                pg.wait_for_timeout(CFG.get("espera_busqueda_ms", 7000))
                for _ in range(CFG.get("scrolls", 5)):
                    pg.mouse.wheel(0, 2400); pg.wait_for_timeout(1300)
                tarjetas = pg.evaluate(EXTRACT)
                texto_pag = pg.evaluate("() => document.body.innerText") or ""
            except Exception as e:
                print(f"    ERROR {type(e).__name__}: {e}", flush=True)
                continue

            mt = re.search(r"~?\s*([\d.,]+)\s+resultados", texto_pag)
            total = None
            if mt:
                try:
                    total = int(re.sub(r"[.,]", "", mt.group(1)))
                except Exception:
                    pass

            ads, vistos = [], set()
            for c in tarjetas:
                if c["id"] in vistos:
                    continue
                vistos.add(c["id"])
                a, ini, dom, pre = parsear(c["texto"])
                ads.append({"id": c["id"], "anunciante": a, "inicio": ini.isoformat() if ini else None,
                            "dias": dias_desde(ini), "dominio": dom, "precio": pre,
                            "creativos": len(c["imgs"]),
                            "imgs": [i["url"] for i in c["imgs"][:3]],
                            "copy": re.sub(r"\s+", " ", c["texto"])[:600]})

            con_dias = [a for a in ads if a["dias"] is not None]
            fuerte = [a for a in con_dias if a["dias"] >= 90]
            dias_ord = sorted(a["dias"] for a in con_dias)
            mediana = dias_ord[len(dias_ord) // 2] if dias_ord else None
            pct90 = round(100 * len(fuerte) / len(con_dias)) if con_dias else None
            ant_prev = None
            if anterior:
                for r in anterior.get("busquedas", []):
                    if r["keyword"] == kw and r["pais"] == pais:
                        ant_prev = r.get("total")
            delta = None
            if total is not None and ant_prev:
                delta = round(100 * (total - ant_prev) / ant_prev)

            resultados.append({
                "keyword": kw, "pais": pais, "total": total, "total_ayer": ant_prev,
                "delta_pct": delta, "anuncios": len(ads),
                "con_dias": len(con_dias), "pct_90mas": pct90, "mediana_dias": mediana,
                "max_dias": max(dias_ord) if dias_ord else None,
                "anunciantes": sorted({a["anunciante"] for a in ads if a["anunciante"]}),
                "ads": ads,
            })
            print(f"    total={total} anuncios={len(ads)} 90+={pct90}% mediana={mediana}d", flush=True)

            # TEMPERATURA: anuncios activos por anunciante (lo que Adminer llama temperatura)
            if not args.sin_anunciantes:
                top = {}
                for a in ads:
                    if a["anunciante"]:
                        top[a["anunciante"]] = top.get(a["anunciante"], 0) + 1
                for nom, _n in sorted(top.items(), key=lambda x: -x[1])[:CFG.get("max_anunciantes_por_busqueda", 4)]:
                    clave = f"{nom}|{pais}"
                    if clave in anunciantes_hoy and anunciantes_hoy[clave]["anuncios"]:
                        continue
                    ejemplo = next((a for a in ads if a["anunciante"] == nom), None)
                    if not ejemplo:
                        continue
                    try:
                        nom_ficha, cnt = contar_anunciante(pg, ejemplo["id"])
                    except Exception as e:
                        print(f"    (anunciante {nom}: error {type(e).__name__})", flush=True)
                        continue
                    ant = temp_ayer.get(clave, {}).get("anuncios")
                    delta_a = round(100 * (cnt - ant) / ant) if (cnt and ant) else None
                    anunciantes_hoy[clave] = {
                        "fecha": HOY, "clave": clave, "anunciante": nom_ficha or nom, "pais": pais,
                        "keyword": kw, "anuncios": cnt, "anuncios_ayer": ant, "delta_pct": delta_a,
                        "dias_max": max((a["dias"] or 0) for a in ads if a["anunciante"] == nom) or None,
                    }
                    print(f"      · {nom[:30]:<30} activos={cnt} ayer={ant} delta={delta_a}", flush=True)

        b.close()

    # Crudo y métricas del día — UPSERT por (keyword, país), igual que los CSV: una corrida
    # parcial (o de prueba) NO puede borrar lo que ya se relevó hoy.
    crudo = DATOS / "crudo" / f"{HOY}.json"
    previo = []
    if crudo.exists():
        try:
            previo = json.loads(crudo.read_text(encoding="utf-8")).get("busquedas", [])
        except Exception:
            previo = []
    por_clave = {(r["keyword"], r["pais"]): r for r in previo}
    for r in resultados:
        por_clave[(r["keyword"], r["pais"])] = r
    dia_crudo = sorted(por_clave.values(), key=lambda r: (r["keyword"], r["pais"]))
    crudo.write_text(json.dumps({"fecha": HOY, "busquedas": dia_crudo}, ensure_ascii=False, indent=1),
                     encoding="utf-8")

    met_path = DATOS / "metricas" / f"{HOY}.json"
    met_prev = {}
    if met_path.exists():
        try:
            met_prev = json.loads(met_path.read_text(encoding="utf-8"))
        except Exception:
            met_prev = {}
    por_clave_met = {(r["keyword"], r["pais"]): r
                     for r in met_prev.get("busquedas", [])}
    for r in resultados:
        por_clave_met[(r["keyword"], r["pais"])] = {k: v for k, v in r.items() if k != "ads"}
    anun_prev = {a["clave"]: a for a in met_prev.get("anunciantes", [])}
    anun_prev.update(anunciantes_hoy)
    metricas = {"fecha": HOY, "generado": datetime.now().isoformat(timespec="seconds"),
                "minutos": round((time.time() - t0) / 60, 1),
                "busquedas": sorted(por_clave_met.values(), key=lambda r: (r["keyword"], r["pais"])),
                "anunciantes": sorted(anun_prev.values(), key=lambda a: a["clave"])}
    met_path.write_text(json.dumps(metricas, ensure_ascii=False, indent=1), encoding="utf-8")

    # CSV acumulativo de búsquedas — UPSERT por (fecha, keyword, país): correr dos veces
    # hoy (o una corrida parcial) actualiza esas filas, nunca las duplica ni las borra.
    hist = DATOS / "historico.csv"
    cab = ["fecha", "keyword", "pais", "total", "total_ayer", "delta_pct",
           "anuncios", "pct_90mas", "mediana_dias", "max_dias"]
    filas, orden = {}, []
    if hist.exists():
        with hist.open(encoding="utf-8", newline="") as f:
            for r in csv.reader(f):
                if not r or r == cab:
                    continue
                k = (r[0], r[1], r[2])
                if k not in filas:
                    orden.append(k)
                filas[k] = r
    for r in resultados:
        k = (HOY, r["keyword"], r["pais"])
        if k not in filas:
            orden.append(k)
        filas[k] = [HOY, r["keyword"], r["pais"], r["total"], r["total_ayer"], r["delta_pct"],
                    r["anuncios"], r["pct_90mas"], r["mediana_dias"], r["max_dias"]]
    with hist.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cab)
        for k in sorted(orden):
            w.writerow(filas[k])

    # CSV acumulativo de anunciantes (la temperatura) — misma regla.
    if anunciantes_hoy:
        ca = DATOS / "anunciantes.csv"
        cab_a = ["fecha", "clave", "anunciante", "pais", "keyword",
                 "anuncios", "anuncios_ayer", "delta_pct", "dias_max"]
        filas_a, orden_a = {}, []
        if ca.exists():
            with ca.open(encoding="utf-8", newline="") as f:
                for r in csv.reader(f):
                    if not r or r == cab_a:
                        continue
                    k = (r[0], r[1])
                    if k not in filas_a:
                        orden_a.append(k)
                    filas_a[k] = r
        for a in anunciantes_hoy.values():
            k = (a["fecha"], a["clave"])
            if k not in filas_a:
                orden_a.append(k)
            filas_a[k] = [a["fecha"], a["clave"], a["anunciante"], a["pais"], a["keyword"],
                          a["anuncios"], a["anuncios_ayer"], a["delta_pct"], a["dias_max"]]
        with ca.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(cab_a)
            for k in sorted(orden_a):
                w.writerow(filas_a[k])

    # El parte del día — se arma del CSV (la UNIÓN del día), no de esta corrida:
    # así una corrida parcial no deja un parte incompleto.
    def _n(x):
        try:
            return None if x in ("", "None", None) else float(x)
        except Exception:
            return None

    dia, anun_dia = [], []
    if hist.exists():
        with hist.open(encoding="utf-8", newline="") as f:
            dia = [r for r in csv.DictReader(f) if r.get("fecha") == HOY]
    ca_path = DATOS / "anunciantes.csv"
    if ca_path.exists():
        with ca_path.open(encoding="utf-8", newline="") as f:
            anun_dia = [r for r in csv.DictReader(f) if r.get("fecha") == HOY]

    L = [f"# RADAR — corrida {HOY}", "",
         f"{len(dia)} búsquedas · {int(sum(_n(r['anuncios']) or 0 for r in dia))} anuncios relevados", ""]
    crec = [a for a in anun_dia if _n(a.get("delta_pct"))]
    if crec:
        L += ["## Los que más crecieron (temperatura)", ""]
        for a in sorted(crec, key=lambda x: -_n(x["delta_pct"]))[:10]:
            L.append(f"- **{a['anunciante']}** ({a['pais']}): {a['anuncios_ayer']} → {a['anuncios']} "
                     f"anuncios activos (**{int(_n(a['delta_pct'])):+d}%**) · {a['keyword']}")
        L.append("")
    if anterior is None:
        L += ["> Primera corrida: todavía no hay temperatura (hace falta la de mañana).", ""]
    L += ["## Búsquedas", "", "| keyword | país | total | ayer | Δ | 90+ | mediana |",
          "|---|---|---|---|---|---|---|"]
    for r in sorted(dia, key=lambda x: -(_n(x["pct_90mas"]) or 0)):
        d = _n(r["delta_pct"])
        L.append(f"| {r['keyword']} | {r['pais']} | {r['total'] or '—'} | {r['total_ayer'] or '—'} | "
                 f"{f'{int(d):+d}%' if d is not None else '—'} | "
                 f"{int(_n(r['pct_90mas'])) if _n(r['pct_90mas']) is not None else '—'}% | "
                 f"{r['mediana_dias'] or '—'}d |")
    (DATOS / "resumen.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"\nLISTO en {metricas['minutos']} min · crudo: {crudo.name} · "
          f"anunciantes medidos: {len(anunciantes_hoy)}")
    print("\n".join(L[:14]))


if __name__ == "__main__":
    main()
