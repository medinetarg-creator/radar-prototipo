"""
RADAR — tablero.

Arma el tablero HTML con los datos REALES del último día recolectado. Es autocontenido:
lleva los datos embebidos, no necesita servidor ni internet (salvo las imágenes de Meta,
que son las del anuncio original).

Uso:  python tablero.py [AAAA-MM-DD]

Salida:  C:\\Users\\odiki\\Desktop\\Radar\\tablero.html
"""
import csv, json, pathlib, sys
from datetime import date

BASE = pathlib.Path(__file__).resolve().parent
DATOS = BASE / "datos"
SALIDA = BASE.parent / "tablero.html"

UMBRAL_ORO, UMBRAL_MIXTO = 40, 15


def veredicto(pct):
    if pct is None:
        return "sin-datos", "⚫ Sin datos"
    if pct >= UMBRAL_ORO:
        return "oro", f"🟢 Aguanta ({pct}% +90d)"
    if pct >= UMBRAL_MIXTO:
        return "mixto", f"🟡 Mixto ({pct}% +90d)"
    return "cementerio", f"🔴 Cementerio ({pct}% +90d)"


def _n(x):
    """Numérico tolerante: los CSV guardan vacío en vez de None."""
    try:
        return None if x in ("", "None", None) else int(float(x))
    except Exception:
        return None


def leer_csv(path, fecha):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if r.get("fecha") == fecha]


def cargar(fecha=None):
    metricas_dir = DATOS / "metricas"
    archivos = sorted(metricas_dir.glob("*.json"))
    if fecha:
        met_path = metricas_dir / f"{fecha}.json"
        if not met_path.exists():
            met_path = None
    else:
        met_path = archivos[-1] if archivos else None
    if met_path is None and not leer_csv(DATOS / "historico.csv", fecha or ""):
        sys.exit("No hay ninguna corrida. Corré recolectar.py primero.")
    fecha = met_path.stem if met_path else fecha
    met = json.loads(met_path.read_text(encoding="utf-8")) if met_path else {"busquedas": [], "anunciantes": []}
    crudo_path = DATOS / "crudo" / f"{fecha}.json"
    crudo = json.loads(crudo_path.read_text(encoding="utf-8")) if crudo_path.exists() else {"busquedas": []}
    return fecha, met, crudo


def construir(fecha, met, crudo):
    # Las tablas salen del CSV del día (la UNIÓN de todas las corridas de hoy), no de la
    # última corrida: si una corrida fue parcial, el tablero igual muestra el día completo.
    filas_b = leer_csv(DATOS / "historico.csv", fecha)
    busquedas = ([{"keyword": r["keyword"], "pais": r["pais"], "total": _n(r["total"]),
                   "anuncios": _n(r["anuncios"]) or 0, "pct_90mas": _n(r["pct_90mas"]),
                   "mediana_dias": _n(r["mediana_dias"]), "max_dias": _n(r["max_dias"]),
                   "delta_pct": _n(r["delta_pct"]), "total_ayer": _n(r["total_ayer"])}
                  for r in filas_b] or met.get("busquedas", []))
    filas_a = leer_csv(DATOS / "anunciantes.csv", fecha)
    anunciantes = sorted(
        ([{"anunciante": r["anunciante"], "pais": r["pais"], "anuncios": _n(r["anuncios"]),
           "anuncios_ayer": _n(r["anuncios_ayer"]), "delta_pct": _n(r["delta_pct"]),
           "dias_max": _n(r["dias_max"]), "keyword": r["keyword"]} for r in filas_a]
         or met.get("anunciantes", [])),
        key=lambda a: -(a["anuncios"] or 0))
    total_anuncios = sum(b.get("anuncios") or 0 for b in busquedas)
    datos = {"fecha": fecha, "busquedas": busquedas, "anunciantes": anunciantes,
             "ads": {f"{r['keyword']}|{r['pais']}": (r.get("ads") or [])
                     for r in crudo.get("busquedas", [])}}
    for b in busquedas:
        b["veredicto"], b["veredicto_txt"] = veredicto(b.get("pct_90mas"))

    filas = "".join(
        f"""<tr data-v="{b['veredicto']}">
        <td><b>{b['keyword']}</b><span class="pais">{b['pais']}</span></td>
        <td class="num">{b.get('total') or '—'}</td>
        <td class="num">{b.get('anuncios')}</td>
        <td><div class="barra"><i style="width:{b.get('pct_90mas') or 0}%"></i></div>
            <span class="pct">{b.get('pct_90mas') if b.get('pct_90mas') is not None else '—'}%</span></td>
        <td class="num">{b.get('mediana_dias') if b.get('mediana_dias') is not None else '—'}d</td>
        <td class="num">{b.get('max_dias') or '—'}d</td>
        <td class="ver">{b['veredicto_txt']}</td></tr>""" for b in busquedas)

    crec = [a for a in anunciantes if a.get("delta_pct") is not None]
    filas_a = "".join(
        f"""<tr><td><b>{a['anunciante']}</b></td><td class="pais2">{a['pais']}</td>
        <td class="num">{a['anuncios'] if a['anuncios'] is not None else '—'}</td>
        <td class="num">{a['anuncios_ayer'] if a.get('anuncios_ayer') else '—'}</td>
        <td class="num delta">{f"{a['delta_pct']:+d}%" if a.get('delta_pct') is not None else '—'}</td>
        <td class="num">{a.get('dias_max') or '—'}d</td>
        <td class="pais2">{a['keyword']}</td></tr>""" for a in anunciantes)

    sin_temp = ("" if crec else
                '<p class="nota">Hoy es la <b>base</b>: la temperatura (Δ% de anuncios activos) '
                'aparece sola en la segunda corrida. Un anunciante con más anuncios activos está '
                'metiendo más plata — pero eso solo dice <i>cuándo cambió</i>, no si vale.</p>')

    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>RADAR — {fecha}</title><style>
*{{box-sizing:border-box}}
body{{margin:0;font:14px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;color:var(--foreground,#e8e8e8)}}
h1{{font-size:17px;margin:0 0 2px}}
h2{{font-size:14px;margin:22px 0 8px;opacity:.85}}
.sub{{opacity:.6;font-size:12px;margin-bottom:14px}}
.chips{{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 18px}}
.chip{{border:1px solid var(--border,#333);border-radius:20px;padding:4px 12px;font-size:12px}}
.chip b{{color:var(--accent,#7cc4ff)}}
.tabs{{display:flex;gap:6px;border-bottom:1px solid var(--border,#333);margin-bottom:14px}}
.tab{{background:none;border:0;color:inherit;opacity:.55;font:inherit;padding:8px 12px;cursor:pointer;
     border-bottom:2px solid transparent}}
.tab.on{{opacity:1;border-bottom-color:var(--accent,#7cc4ff)}}
.panel{{display:none}} .panel.on{{display:block}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{text-align:left;font-weight:600;opacity:.6;font-size:11px;text-transform:uppercase;
   letter-spacing:.04em;padding:6px 8px;border-bottom:1px solid var(--border,#333)}}
td{{padding:7px 8px;border-bottom:1px solid var(--border,#222)}}
td.num{{text-align:right;font-variant-numeric:tabular-nums}}
.pais{{margin-left:6px;font-size:10px;opacity:.5;border:1px solid var(--border,#333);
      border-radius:4px;padding:1px 4px}}
.pais2{{opacity:.55;font-size:12px}}
.barra{{display:inline-block;width:70px;height:6px;border-radius:3px;background:var(--border,#333);
       vertical-align:middle;margin-right:8px;overflow:hidden}}
.barra i{{display:block;height:100%;background:var(--accent,#7cc4ff)}}
tr[data-v="cementerio"] .barra i{{background:#e0605f}}
tr[data-v="mixto"] .barra i{{background:#d8a657}}
tr[data-v="oro"] .barra i{{background:#63b06a}}
.pct{{font-variant-numeric:tabular-nums;font-size:12px}}
.ver{{font-size:12px;white-space:nowrap}}
.nota{{font-size:12px;opacity:.65;border-left:2px solid var(--accent,#7cc4ff);padding:6px 10px;
      background:var(--card,rgba(127,127,127,.07))}}
.sel{{background:var(--card,rgba(127,127,127,.07));border:1px solid var(--border,#333);color:inherit;
     font:inherit;font-size:12px;padding:5px 8px;border-radius:6px;margin-bottom:12px}}
.grilla{{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:12px}}
.ad{{border:1px solid var(--border,#333);border-radius:10px;overflow:hidden;display:flex;
    flex-direction:column}}
.ad img{{width:100%;height:150px;object-fit:cover;background:var(--card,rgba(127,127,127,.07))}}
.ad .cuerpo{{padding:8px 10px;font-size:12px;flex:1}}
.ad .quien{{font-weight:600;margin-bottom:3px}}
.ad .dias{{font-size:11px;opacity:.6;margin-bottom:6px}}
.ad .copy{{opacity:.72;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;
          overflow:hidden;margin-bottom:6px}}
.ad .pie{{font-size:11px;opacity:.6;display:flex;justify-content:space-between;gap:6px}}
.ad a{{color:var(--accent,#7cc4ff);text-decoration:none;font-size:11px}}
.vacio{{opacity:.5;font-size:12px;padding:10px 0}}
</style></head><body>
<h1>RADAR</h1>
<div class="sub">Corrida del {fecha} · datos reales de la Biblioteca de Anuncios de Meta</div>
<div class="chips">
  <span class="chip"><b>{len(busquedas)}</b> búsquedas</span>
  <span class="chip"><b>{total_anuncios}</b> anuncios relevados</span>
  <span class="chip"><b>{len(anunciantes)}</b> anunciantes medidos</span>
  <span class="chip"><b>{met.get('minutos', '?')}</b> min de corrida</span>
</div>
<div class="tabs">
  <button class="tab on" data-p="p1">Búsquedas</button>
  <button class="tab" data-p="p2">Temperatura</button>
  <button class="tab" data-p="p3">Anuncios</button>
</div>
<div class="panel on" id="p1">
  <h2>Persistencia por búsqueda</h2>
  <table><thead><tr><th>Búsqueda</th><th class="num">Anuncios</th><th class="num">Relevados</th>
  <th>+90 días</th><th class="num">Mediana</th><th class="num">Máx</th><th>Veredicto</th></tr></thead>
  <tbody>{filas}</tbody></table>
  <p class="nota">El <b>% de anuncios con 90 días o más</b> es el único proxy honesto que tenemos del
  mercado: nadie paga publicidad tres meses seguidos perdiendo plata. Meta no publica el gasto.</p>
</div>
<div class="panel" id="p2">
  <h2>Anuncios activos por anunciante</h2>
  {sin_temp}
  <table><thead><tr><th>Anunciante</th><th>País</th><th class="num">Activos</th>
  <th class="num">Ayer</th><th class="num">Δ</th><th class="num">Máx días</th><th>Búsqueda</th></tr></thead>
  <tbody>{filas_a}</tbody></table>
</div>
<div class="panel" id="p3">
  <h2>Anuncios relevados</h2>
  <select class="sel" id="filtro"></select>
  <div class="grilla" id="grilla"></div>
</div>
<script>
const D = {json.dumps(datos, ensure_ascii=False)};
document.querySelectorAll('.tab').forEach(t => t.onclick = () => {{
  document.querySelectorAll('.tab').forEach(x => x.classList.toggle('on', x === t));
  document.querySelectorAll('.panel').forEach(p => p.classList.toggle('on', p.id === t.dataset.p));
}});
const claves = Object.keys(D.ads);
const sel = document.getElementById('filtro');
sel.innerHTML = '<option value="">Todas las búsquedas</option>' +
  claves.map(k => `<option value="${{k}}">${{k}} (${{(D.ads[k] || []).length}})</option>`).join('');
const pintar = () => {{
  const f = sel.value, g = document.getElementById('grilla');
  let lista = [];
  claves.forEach(k => {{ if (!f || k === f) lista = lista.concat(D.ads[k].map(a => ({{...a, busqueda: k}}))); }});
  lista.sort((a, b) => (b.dias || 0) - (a.dias || 0));
  if (!lista.length) {{ g.innerHTML = '<p class="vacio">Sin anuncios para esta búsqueda.</p>'; return; }}
  g.innerHTML = lista.slice(0, 150).map(a => `<div class="ad">
    ${{a.imgs && a.imgs[0] ? `<img loading="lazy" src="${{a.imgs[0]}}">` : ''}}
    <div class="cuerpo">
      <div class="quien">${{a.anunciante || 'Anunciante sin nombre'}}</div>
      <div class="dias">${{a.dias !== null && a.dias !== undefined ? a.dias + ' días corriendo' : 'sin fecha'}}
        ${{a.creativos ? ' · ' + a.creativos + ' creativo(s)' : ''}}</div>
      <div class="copy">${{(a.copy || '').slice(0, 260)}}</div>
      <div class="pie"><span>${{a.dominio || '—'}}</span><span>${{a.precio || ''}}</span></div>
      <a target="_blank" href="https://www.facebook.com/ads/library/?id=${{a.id}}">Ver en la Biblioteca ↗</a>
    </div></div>`).join('') + (lista.length > 150 ? '<p class="vacio">…y ' + (lista.length - 150) + ' más.</p>' : '');
}};
sel.onchange = pintar; pintar();
</script></body></html>"""


def main():
    fecha = sys.argv[1] if len(sys.argv) > 1 else None
    fecha, met, crudo = cargar(fecha)
    SALIDA.write_text(construir(fecha, met, crudo), encoding="utf-8")
    filas = leer_csv(DATOS / "historico.csv", fecha)
    adss = sum(len(v) for v in (crudo.get("busquedas") and
               {f"{r['keyword']}|{r['pais']}": (r.get("ads") or []) for r in crudo["busquedas"]} or {}).values())
    print(f"tablero.html generado con el día {fecha}: {len(filas)} búsquedas, "
          f"{sum(_n(r['anuncios']) or 0 for r in filas)} anuncios relevados, "
          f"{adss} con detalle embebido")
    print(SALIDA)


if __name__ == "__main__":
    main()
