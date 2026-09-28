# RADAR — Registro de cambios y pendientes

Este archivo es el **estado del proyecto fuera del chat**. Existe para que se pueda empezar
una sesión nueva sin perder nada.

---

## Cómo se usa

- **Vos escribís los cambios acá o me los mandás en UN solo mensaje.** No hace falta un
  formato especial: numerá y listo.
- **No los mandes de a uno por chat.** Cada mensaje re-lee toda la conversación
  (~164.000 tokens en esta sesión), así que 10 mensajes cuestan 10 veces más que uno solo
  con los 10 cambios juntos.
- Yo voy marcando acá lo que ya está hecho.

---

## Hecho ✅

### Prototipo
- [x] Prototipo navegable single-file, 7 vistas (panel, librería, ficha, match, guardados, tendencias, planes)
- [x] Tema oscuro + claro, densidad conmutable
- [x] Imágenes de creativos en tarjetas, ficha, match y guardados
- [x] Verificado en Chromium: 0 errores JS, sin desborde, usable en teléfono

### Criterio (corregido)
- [x] La señal principal pasó de **cantidad de anuncios** a **antigüedad + crecimiento**
- [x] 5 señales nuevas: Escalando / Consolidada / Prometedora / En prueba / Marca (descarte)
- [x] Orden por defecto por señal, no por volumen
- [x] Evidencia del cambio: correlación **−0,18** entre cantidad de anuncios y días corriendo

### Datos reales (probado contra la Biblioteca de Anuncios)
- [x] Extracción sin cuenta y sin API (Playwright): **279 anuncios** en 6 búsquedas, **168 creativos**
- [x] Conteo de anuncios activos por anunciante (ficha del anuncio → `~N resultados`)
- [x] Medición de mercado por keyword: competencia + supervivencia (16 mediciones, AR y MX)
- [x] Hallazgo: "repostería para vender" = 10 % de supervivencia (cementerio);
      "air fryer" AR = 500 anuncios totales y 44 % de supervivencia (oro)
- [x] Índice de oportunidad propuesto: `supervivencia × (1 − log10(total)/log10(20000))`

### Publicación
- [x] Sitio público: https://medinetarg-creator.github.io/radar-prototipo/
- [x] Repo: https://github.com/medinetarg-creator/radar-prototipo (público — se puede borrar)
- [x] Copia en `K:\Drive Medinet\RADAR\`

### Mentoría (Notion) — bajada y reordenada
- [x] Bajada completa con la API de Notion: 1.429 bloques, 55 imágenes
- [x] Detectado que el `.md` exportado perdía **67 %** del contenido (38 k de 63,5 k chars)
- [x] Recuperados **2 prompts enteros** que el `.md` no tenía (creativos masivos, avatar)
- [x] Recuperados 8 agentes de Cosmos y los marcos de gatillos y niveles de conciencia
- [x] `RADAR-Cadena-de-creacion.md` — la mentoría como línea de producción de 9 etapas
- [x] `RADAR-Prompts-encadenados.md` — los 6 prompts reescritos como etapas con ficha

### Decisiones tomadas
- [x] Alcance inicial: **uso personal, sin login ni pagos**
- [x] Dónde corre: **la PC** (escalable después; el scraper es un script suelto → cron)
- [x] Forma de uso: **panel-first** (el chat es un extra)
- [x] IA: **LLM propio** con API key propia — proveedor como línea de config
- [x] Modelo: `deepseek-flash` (el `pro` no hace falta: es redacción, no razonamiento)
- [x] Costo IA estimado: **menos de US$1/mes**
- [x] La mentoría se reordena como **cadena con estado** (la ficha), no como prompts sueltos
- [x] El recorrido: **consulta → mercado → desglose → promesa → funnel → producto → creativos**

---

## Pendientes 📋

### Para arrancar la fase 0 (el motor)
- [ ] Definir la carpeta del proyecto
- [ ] Definir las keywords iniciales (propuesta: las 16 ya medidas)
- [ ] **10–20 ofertas que se sepa que facturaron** ← calibra los pesos del índice

### Fases siguientes
- [ ] Fase 1: Tablero + Mercados
- [ ] Fase 2: Ofertas + ficha
- [ ] Fase 3: Guardados + seguimiento diario
- [ ] Fase 4: Recomendados
- [ ] Fase 5: Nichos (el agente)
- [ ] Fase 6: Landing (precio, embudo, checkout)
- [ ] Fase 7: Chat

---

## Cambios pedidos

_(agregar acá; un número por cambio)_

### Módulo MODELAR — pedido 27-sep (ideas crudas, sin ordenar)

1. **Botón `Modelar` en la página principal**, al lado del icono de guardado, en cada producto
   que se pueda modelar.
2. `Modelar` abre un **módulo nuevo** que corre el **prompt encadenado** ya escrito
   (`RADAR-Prompts-encadenados.md`): entra el anuncio → se scrapea el anuncio → se leen sus
   datos → se saca la imagen del producto → se detecta el avatar → se completa la ficha.
3. **La salida no es la ficha: es el producto ya modelado.**
   - libro de mapas mentales → el libro con sus diagramas
   - ebook / PDF → el ebook redactado
4. **Todo se escribe** (lo más posible) en vez de copiarse a mano. Qué queda manual y qué lo
   hace el motor, módulo por módulo — pendiente de definir.

_(seguir agregando ideas acá; un número por idea)_

22. **El método de Adminer, extraído de sus subtítulos** (no de la web): `RADAR-Metodo-Adminer.md`.
    Su métrica central es la **cantidad de anuncios activos** ("temperatura", 0-150°), que es el
    proxy que nuestras mediciones rechazan — pero **su propia guía se contradice**: manda a los
    principiantes a ordenar por **crecimiento**, bajar el rango de anuncios y mirar el
    "período mínimo activo". O sea: nuestro criterio es la práctica que ellos mismos recomiendan,
    solo que ninguna de las dos herramientas lo convierte en veredicto.
23. **A copiar:** temperatura propia = delta de anuncios entre corridas; **esteira de testes**
    (kanban con etapas y links por tarjeta); favoritos con **colecciones** por nicho y
    estacionalidad; filtro por fecha de publicación (estacionalidad); "anuncios relacionados"
    como ideas de upsell.
24. **Técnica para leer cualquier producto de la competencia:** bajar los subtítulos de YouTube
    con `yt-dlp --write-auto-subs` (segundos, gratis, sin transcribir).

### De la comparación con adheart / Adminer — 27-sep

13. **Tags de ángulo con IA por anuncio** (PAIN · DEAL · BONUS · URGENT · NORISK · ASK ·
    SIMPLE · CALL OUT · CROWD · EXPERT · GUIDE · IDEAL · MEDIA · UNIQUE). Es la taxonomía que
    adheart ya usa; va directo a la etapa 7 para que los creativos salgan tagueados.
14. **CTA detectado por anuncio** (SHOP NOW / WHATSAPP MESSAGE / LEARN MORE): dice en qué paso
    del funnel está el competidor.
15. **Bandera de país por anuncio** y búsqueda multi-país en la misma corrida.
16. **Precio y dominio en la tarjeta**, no solo dentro de la ficha.
17. **Categorías con conteo** (E-commerce, Nutra, Finanzas…) para barrer nichos sin keywords.
18. **Ventana temporal en el filtro** (días activos / últimos 90 días).
19. **Lo que no se puede copiar:** el archivo histórico (adheart desde 2019, Adminer 135 M de
    anuncios) y la escala multi-país. Se compensa con criterio + veredicto + producto, y
    **empezando a guardar corridas diarias ya**.
20. **Confirmación:** adheart tiene un filtro "Días activos" — nuestro criterio principal es el
    mismo que usa una herramienta de US$69/mes. Ellos lo usan como filtro, RADAR como veredicto.
21. Detalle completo en `RADAR-Competencia.md`.

### Sobre la extensión Ad Library Cloud — 27-sep (investigado, no sirve para AR)

10. La extensión trae un dato que parecía oro: `Shows: 110361 | $ 1324.33` en cada anuncio.
    **Se bajó el `.crx`, se leyó el código y se midió.** Resultado en `RADAR-Capacidades.md`
    sección 3.bis: el **importe es inventado** (CPM fijo de US$12: `shows × 0,012`, coincide al
    centavo) y los **shows son el "Alcance" de la UE** (`eu_total_reach`), que Meta entrega solo
    a quien mira desde la UE/Brasil/UK. Desde Argentina no llega: 0 apariciones en 4 anuncios y
    2 búsquedas AR.
11. **Consecuencia:** la persistencia (días corriendo) sigue siendo el único proxy del mercado
    argentino. No prometer gasto ni impresiones para anuncios AR.
12. **Lo que sí vale de la extensión:** descarga de creativos en HD y guardado — que nuestro
    scraper ya hace por su cuenta.

### Ideas sueltas — 27-sep (segunda tanda)

5. **Transcribir el video del anuncio** (un anuncio ya validado) para sacar el texto, los
   dichos y los ángulos → insumo para los creativos propios. *Probado: funciona offline.*
6. **Generar las imágenes** de tapas, páginas y mapas mentales por OpenRouter. *Probado.*
7. **Generar las voces** (Edge local gratis u `gpt-audio-mini` por OpenRouter).
8. **VEO 3 para animar** los videos: probablemente fuera de la web, pero **el prompt grande
   tiene que salir con TODOS los creativos tagueados** (cada pieza con su ángulo, su gancho,
   su copy, su prompt de imagen, su texto en pantalla y su voz en off), listos para ejecutar.
9. **El dossier de capacidades** está en `RADAR-Capacidades.md` — qué se puede, qué no, con
   qué, cuánto cuesta, y qué falta pedir.

### 3 TikToks de métodos de creativos — 27-sep (transcritos)

13. El usuario pasó 3 TikToks sobre cómo armar creativos. Se bajaron con `yt-dlp.exe` del venv de
    AutoValidadorPro (resuelve el JS challenge solo, sin cookies) y se transcribieron con
    faster-whisper local. **Los dos pasos quedan verificados en esta máquina**: bajar video de
    TikTok ✅ (antes solo estaba probado el circuito de transcripción).
14. **Lo que dicen los videos:** (a) creativo réplica = tomar un creativo ganador de una marca de
    afuera y doblarlo al español; (b) adaptar el guión de una marca argentina con Gemini; (c) el
    guion sale de **leer los comentarios del nicho** (el dolor con las palabras del cliente);
    (d) un reel que ya se viralizó es un creativo **ya validado gratis** → subirlo como anuncio.
15. **Lo que RADAR adopta:** una capa orgánica (guardados/comentarios/likes como prueba previa a la
    pauta), un campo `dolores_textuales[]` en la ficha, y réplica de la **estructura** del guión
    (gancho → dolor → mecanismo → prueba → CTA) en vez del video ajeno.
16. **Desacuerdo marcado:** doblar y resubir el creativo de otra marca no es copiar el guión, es
    republicar su material (riesgo de derechos + Meta castiga el creativo duplicado). Quedarse con
    la estructura y material propio.
17. **Costo medido:** la transcripción cuesta tiempo, no plata — 231 s de audio → 626 s de CPU;
    102 s → 132 s; 59 s → 130 s. Es el cuello de botella para transcripción en lote.
18. **Pendiente de verificar:** scrapeo de comentarios/guardados en TikTok e Instagram (la
    capacidad nueva que habilitaría el punto 15). No prometerla hasta medirla.
19. Documento con las transcripciones completas, el banco de 7 creativos y el análisis:
    `RADAR-Ideas-creativos-tiktok.md`. Audios y JSON crudos en `tiktok/`.

### Minería de comentarios + creativo de muestra — 27-sep (probado)

20. **TikTok: los comentarios se leen sin login** interceptando `/api/comment/list` (el navegador
    firma, nosotros leemos). Medido: 23 páginas, 458 crudos, **203 comentarios únicos** del video de
    653 comentarios. Hay que abrir **ventana visible** (headless devuelve la página degradada) y
    scrollear `div[class*="DivCommentMain"]` (no tiene `data-e2e`). Detalle en
    `RADAR-Comentarios-criterios.md`.
21. **TikTok búsqueda = login wall**: `/search/video?q=` devuelve "Hubo un problema". El video y sus
    comentarios, abiertos. Para descubrir orgánico hay que entrar por perfil o por buscador externo.
22. **Instagram: captions sí, comentarios no** (modal de registro). Queda afuera hasta tener sesión.
23. **Capa orgánica barata:** `yt-dlp --skip-download` da vistas/likes/comentarios/**guardados** por
    video en ~2 s sin navegador. Es la señal del video 3 ("los reels que ya viralizaron") medida.
24. **La señal de dolor textual es medible**, pero con dos columnas que no se mezclan: frecuencia de
    mención (inositol 14 menciones / 22♥) vs likes (1 comentario / 870♥ "perdiendo la esperanza").
    Denominadores obligatorios: comentarios/vistas e **guardados/vistas**. Etiquetar antes de contar:
    dolor · pregunta · objeción · testimonio.
25. **Dónde entra en la cadena (decidido):** los comentarios **no** son etapa de MERCADO (Meta no
    publica comentarios de anuncios ni la Biblioteca los muestra). Son fuente nueva que se cuelga de
    `oferta_base` → alimentan el AVATAR de la etapa 3 y se usan en la etapa 7. Tres modos: métricas
    orgánicas en la corrida diaria (gratis, por anunciante que pasó el filtro) · cosecha completa
    sólo de la oferta base elegida · a demanda desde la pantalla.
26. **Creativo #2 producido de punta a punta** como muestra: voz es-AR (Edge, $0), imagen con
    OpenRouter (US$0,039) y MP4 1080×1920 con ffmpeg ($0). Total **US$0,039 y ~4 min**.
    `RADAR-Creativo-2-muestra.md` + archivos en `tiktok/creativo2_*`.
27. **Truco de formato verificado:** sin `image_config: {aspect_ratio: "9:16"}` el modelo de imagen
    devuelve 1024×1024 cuadrado; con eso, 768×1344. Ahorra el recorte.
28. **Pendiente:** el puente orgánico → anuncio pautado (que el mismo video promocione una oferta de
    la Biblioteca) todavía no se validó con un caso real.
