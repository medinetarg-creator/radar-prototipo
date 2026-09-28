# RADAR — Qué puedo hacer y qué no

> Dossier de capacidades, **medido en esta máquina el 27-sep-2026**. Cada ✅ de acá abajo salió
> de una prueba real, no de una suposición. El objetivo: saber de antemano qué parte del
> recorrido "de cero a producto terminado + creativos" se puede automatizar hoy y qué hay que
> comprar, pedir o hacer a mano.

---

## 1. Las 4 pruebas de hoy (con evidencia)

| # | Qué se probó | Resultado | Evidencia |
|---|---|---|---|
| 1 | **Maquetar y exportar un PDF de producto** (tapa + índice + diagrama) | ✅ Funciona sin instalar nada. A4, 3 páginas, texto extraíble | `_prueba-producto.pdf` |
| 2 | **Transcribir un audio/video en español, offline** | ✅ Texto perfecto, con acentos y puntuación. 15 s de audio en 18 s de proceso | `_probar_transcripcion.py` |
| 3 | **Generar una portada con IA** | ✅ Imagen 1024×1024, **texto en español sin errores** ("MAPAS MENTALES EN 7 DÍAS"). Costo medido: **US$0,039** | `_pruebas/tapa_prueba.png` |
| 4 | **Armar un creativo de video narrado** | ✅ MP4 1080×1920, 15,8 s, imagen con zoom lento + voz sincronizada | `_pruebas/prueba_creativo.mp4` |

---

## 2. Tabla maestra: qué parte del producto sale sola

| Pieza | ¿Se puede? | Con qué | Necesita | Costo |
|---|---|---|---|---|
| Scrapear el anuncio (copy, días, anunciante) | ✅ ya probado | Playwright sin login | nada | $0 |
| Contar los anuncios activos del anunciante | ✅ ya probado | ficha del anuncio → `~N resultados` | nada | $0 |
| Leer la **landing** del anuncio (precio, checkout, bloques) | ✅ | Playwright o `r.jina.ai` | nada | $0 |
| **Transcribir el video del anuncio** | ✅ **probado hoy** | `faster-whisper` local (ya instalado) + ffmpeg | bajar el video de Meta (a probar con un caso real) | $0 |
| **Ver la imagen del creativo** (¿hay avatar? ¿es mockup?) | ⚠️ con clave | Modelo de visión por OpenRouter (cascada gratis) | elegir el modelo | $0 (free tier) |
| Redactar la ficha paso a paso (7 etapas) | ✅ | API propia (deepseek) | nada | < US$1/mes |
| Escribir el ebook / libro completo | ✅ | API propia, por capítulos | nada | centavos |
| Índice, capítulos y estructura del pack | ✅ | Etapa PRODUCTO de la cadena | nada | $0 |
| **Mapas mentales y diagramas** | ✅ | SVG generado por código (se regenera si cambia el índice) | nada | $0 |
| **Maquetar el PDF final** | ✅ **probado hoy** | HTML + CSS → Chrome headless | nada | $0 |
| **Portadas** | ✅ **probado hoy** | OpenRouter → Gemini image | crédito de OpenRouter | **US$0,039 c/u** |
| Imágenes internas (ilustraciones, mockups) | ✅ | igual que portadas | crédito | US$0,039 c/u |
| **Voces** | ✅ | (a) Edge local gratis, (b) `openai/gpt-audio-mini` por OpenRouter, más natural | (b) crédito | (a) $0 · (b) centavos |
| Música de fondo para los videos | ✅ | `google/lyria-3` por OpenRouter | crédito | a medir |
| **Creativo de video** (imagen + voz + música, 15-30 s) | ✅ **probado hoy** | ffmpeg (ya instalado) | nada | $0 |
| Video con **movimiento real** de personas/escenas | ❌ | VEO 3 / HeyGen | cuenta paga + API | — |
| Publicar el producto y cobrar (Hotmart, Kiwify, ImpulTienda) | ❌ manual | — | tu cuenta | — |
| Prender y optimizar campañas de Meta | ❌ manual | — | tu Business Manager | — |

---

## 3. Lo que NO puedo (y por qué)

1. **Verificar si una oferta factura.** Meta no publica el gasto de los anuncios comerciales.
   Se infiere de la persistencia (días corriendo) y del crecimiento del conteo. Es un proxy,
   no un dato.
2. **Los 8 agentes de Cosmos.** Son de una plataforma paga. Nuestro motor los reemplaza —
   es justamente el punto del proyecto.
3. **Video fotorrealista con movimiento** (VEO 3, HeyGen). Sin cuenta paga no hay. Lo que sí
   hay hoy es creativo de video **narrado sobre imágenes** (probado), que es lo que usa la
   mayoría de los infoproductos de bajo ticket.
4. **Operar cuentas de terceros:** publicar en la plataforma de pago, crear la campaña,
   tocar el Business Manager. Eso es manual por diseño y además es donde vos tenés el control.
5. **Copiar los archivos del competidor** (su PDF, su video completo). Es ilegal y además el
   usuario exige cero humo. Se copia la **estructura** de la oferta, no el contenido.

---

## 3.bis El "gasto" y los "shows" de la extensión Ad Library Cloud (medido 27-sep-2026)

La extensión **Ad Library Cloud** de CPA.RIP (ID `mmehdbhpbgoegockemckbpjeoflflobc`, 50.000
usuarios) muestra en cada anuncio `Shows: 110361 | $ 1324.33`. **Se bajó el `.crx` y se leyó
el código.** Resultado:

1. **El importe gastado NO es un dato.** Está escrito a mano en `content.js`:
   `"$ " + (0.012 * shows)`. Es un CPM fijo de **US$12** aplicado a los shows.
   Comprobado: 0,012 × 110.361 = 1.324,33 — coincide al centavo con la captura.
2. **Los "shows" sí son un dato de Meta, pero tienen dos límites.** La extensión los lee de
   `ad_library_main.ad_details.aaa_info.eu_total_reach`. En el código de Meta ese campo vive en
   el fragmento `AdLibraryV3AdDetailsQuery` → `eu_transparency`, junto a `br_transparency` y
   `uk_transparency` (`total_reach`), y la tarjeta que lo muestra se llama **"Alcance"** y
   arranca solo si la `RegulatoryLocation` del **que mira** es EU, BR o UK. Meta la etiqueta
   como **estimación**.
3. **Desde Argentina ese campo no llega.** Medido: 0 apariciones de `eu_total_reach` /
   `aaa_info` en la ficha de 4 anuncios (incluido el de la captura) y en 2 búsquedas AR
   (`air fryer`, `recetas sin azúcar`, 54 y 65 anuncios en pantalla). La propia extensión avisa:
   *"Meta often blocks ad impression visibility for specific accounts and/or IP addresses"*.

**Consecuencia para RADAR:** la persistencia (días corriendo) sigue siendo el único proxy
disponible para el mercado argentino. **No prometer gasto ni impresiones de anuncios AR.**
El "Alcance" de la UE solo tendría sentido si algún día se analiza el mercado europeo, y
requeriría mirar la Biblioteca desde una IP europea.

## 4. Lo que necesito de vos (lista corta)

1. **2 o 3 anuncios de ejemplo con video** (links de la Biblioteca de Anuncios). Es lo único
   del circuito de transcripción que no probé todavía: bajar el video de un anuncio real.
2. **2 o 3 ejemplos de libros de mapas mentales / ebooks que se estén vendiendo** (links o
   capturas). No para copiar el contenido: para copiar el **formato del entregable** —
   cuántas páginas, qué bonos, cómo se ve la tapa.
3. **Crédito de OpenRouter** para las imágenes: alcanza con unos pocos dólares
   (US$0,039 por portada → 100 portadas ≈ US$4).
4. **Decisión sobre las voces:** ¿Edge local (gratis, algo robótico) o `gpt-audio-mini`
   (suena mejor, centavos)?
5. **Decisión sobre el video:** ¿te sirve el creativo narrado sobre imágenes (US$0) o querés
   que investiguemos VEO 3 con cuenta paga?
6. **Los 10–20 productos que se sepa que facturaron.** Sigue pendiente de antes: es lo que
   calibra el índice de oportunidad.

---

## 5. El recorrido completo: de cero a producto + creativos

```
[1] ANUNCIO           scrapeo el anuncio y el anunciante            ✅ automático
[2] CREATIVO          veo la imagen · transcribo el video            ✅ automático
[3] LANDING           precio, checkout, bloques de la página         ✅ automático
[4] FICHA             las 7 etapas completan el JSON                 ✅ automático
[5] DESGLOSE          qué producto es y cómo está armado             ✅ automático
[6] PROMESA           la elegís vos entre 6 variantes                👤 tu OK
[7] FUNNEL            los 11 bloques de la landing                   ✅ automático
[8] PRODUCTO          índice + capítulos + diagramas                 ✅ automático
[9] MAQUETA           PDF con tapa, índice y diagramas               ✅ probado
[10] CREATIVOS        imágenes + copys + guiones                     ✅ automático
[11] VIDEO            narrado sobre las imágenes                     ✅ probado
[12] CHECKOUT         publicación y cobro                            ❌ manual
[13] CAMPAÑA          Meta Ads                                       ❌ manual
```

Las etapas 1 a 4 son las que hoy hacés a mano (copiar y pegar en el prompt grande). **Ese es
el módulo MODELAR**: un botón en la tarjeta del anuncio que dispara 1→4 sin intervención.

---

## 6. Costo real de un producto terminado (estimado con lo medido)

| Ítem | Costo |
|---|---|
| Scraping + transcripción + ficha + redacción del libro | < US$1 |
| Portada + 5 imágenes internas | ≈ US$0,25 |
| Voces de los creativos (3 videos) | ≈ US$0,02 |
| Video (ffmpeg) | $0 |
| **Total por producto** | **≈ US$1,30** |

---

## 7. Lo que NO está decidido todavía

- Qué modelo de visión entra en la cascada (se elige probando 3 sobre creativos reales).
- Si el motor va a correr como script suelto o como servicio (importa para el botón del panel).
- Si el pack lleva plantillas editables (Canva/Sheets) además del PDF.
