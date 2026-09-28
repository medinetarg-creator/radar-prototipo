# RADAR — Plan del módulo MODELAR

> La hoja de ruta **"Ideas a aplicar"** leída contra lo que ya existe.
> Verificado el 28-sep-2026 contra el motor, el dossier de capacidades y la cadena de prompts.

---

## 1. Qué de la hoja de ruta ya está andando

| Lo que pide la hoja de ruta | Estado real |
|---|---|
| Motor que corre solo todos los días scrapeando la Biblioteca | ✅ **hecho** — cron 7:00, `motor/recolectar.py` |
| Validar viabilidad por persistencia (días corriendo) | ✅ **hecho** — es el criterio central, ya en código |
| Tablero con los productos calificados | ⚠️ **a medias** — `tablero.html` se genera, pero es HTML suelto |
| Búsqueda a demanda por nicho + subnicho | ❌ no existe (hoy las keywords se agregan en `config.json`) |
| Botón **Modelar** | ❌ no existe |
| Deep scrape: auditar la landing del anuncio | ✅ **verificado 28-sep** — sin navegador, ~3 KB y segundos por landing |
| Deep scrape: analizar al anunciante | ❌ no hecho, y **sin verificar** (ver punto 3) |
| Cadena de prompts con ficha | ✅ **escrita** — `RADAR-Prompts-encadenados.md`, 7 etapas, verificada |
| Nivel de conciencia | ✅ ya está en la cadena |
| Producto: inventario de promesas + índice | ✅ ya está en la cadena (etapa 6) |
| Creativos: ángulos + 10 piezas + guion | ✅ ya está en la cadena (etapa 7) |
| Maquetar el PDF del producto | ✅ **probado** (HTML+CSS → Chrome headless) |
| Producir el creativo (imagen + voz + video) | ✅ **probado** — US$0,039 y ~4 min |

**Resumen:** la hoja de ruta no arranca de cero. La mitad ya está construida o probada. Lo que
falta es el **puente**: la entrada manual, el botón, y el deep scrape.

---

## 1.b — Verificado hoy con dos landings reales

No hizo falta navegador ni credenciales. Con `curl` a `r.jina.ai` (convierte la página a
Markdown) salen ~3 KB por landing, en segundos y gratis. Probado sobre dos ofertas del corpus
del 27-sep:

**`academiakarinagao.com`** — 306 días corriendo. Academia con catálogo (Recetarios, Cursos,
Combos), precios en **USD $4 a $17**, plataforma de checkout **Wisboo**. Un infoproducto low
ticket de verdad, y el caso ideal para modelar.

**`pipitea.com`** — 79 días, anunciado por "Cholesterol Relief Community". "Premium Tea from
Yunnan's Mountains", con *GMP Certified* y *3-6 Day Shipping*.

> **No es un infoproducto: es un producto físico.**

De ahí sale un filtro que no teníamos y que conviene usar: **la landing dice sola si es físico
o digital.** Envíos, certificaciones, "kilos", "3-6 day shipping" → físico. Se descarta sin
gastar una sola llamada a la IA. Y es un error que hoy la hoja de ruta no contempla: el motor
mide persistencia, y una oferta de té puede llevar 79 días corriendo tan tranquila.

---

## 1.c — El agregado: base de conocimiento y variantes

Los dos pedidos de tu "Agregado" ya están incorporados a la cadena.

**Base de conocimiento (`conocimiento`).** Es el insumo que faltaba, y el más barato de todos:
**el motor ya lo baja todos los días y hoy lo tira.** Cada corrida guarda todos los avisos de
la búsqueda, no solo el ganador. Eso —más las landings del nicho (`r.jina.ai`) y los subtítulos
de los videos (`yt-dlp`)— es el material del tema. Todo a $0 y ya verificado.

Sin esto el producto sale siendo una copia de la oferta modelada, que es exactamente lo que la
cadena hacía hasta ahora. El campo tiene `temas` (lo que se sabe) y `huecos` (lo que ninguna
fuente cubrió). El segundo es el que importa: es lo que evita escribir con seguridad sobre algo
que no se sabe.

> **El límite, y va en serio:** esto es para ENTENDER el tema, no para copiar material ajeno.
> El texto del producto se escribe de cero.

**Variantes.** Ya en la cadena, en dos lugares:

- **Etapa 6 (Producto):** en vez de un índice, propone **3 versiones estructurales** del mismo
  contenido — por tiempo, por categoría, por nivel o caso — cada una con su índice completo, y
  recomienda una. Vos elegís.
- **Etapa 7 (Creativos):** los 10 creativos tienen que cubrir **modelos de enfoque distintos**
  (confesión · error común · mecanismo · antes/después · objeción frontal · demo · curiosidad ·
  historia de origen · comparación · urgencia). Mínimo 6 modelos distintos, y si dos se repiten
  el sistema tiene que decirlo.

Esto es lo que convierte "modelar" en modelar de verdad: te llevás la lógica y elegís tu propio
envase, en vez de clonar el del competidor.

---

## 2. Las 4 cosas que corregiría antes de construir

### 2.1 — Confunde DATO con ANÁLISIS

La Fase 1 dice:

> *"Poblado de la Ficha: toda esta información … completa automáticamente los campos de las
> etapas de Mercado, Oferta Base, Desglose y Promesa."*

**El scrape no puede llenar el Desglose ni la Promesa.** El scrape produce **datos** (precio,
bonos, upsell, días corriendo). El Desglose y la Promesa son **análisis**: los produce el
modelo leyendo esos datos.

La diferencia importa mucho en la práctica:

- **Un dato** puede estar mal y no te enterás nunca. "Precio: $97" se ve igual si es correcto
  o si el scraper leyó el número equivocado.
- **Un análisis** lo podés juzgar. "El mecanismo de esta oferta es X" lo leés y sabés si tiene
  sentido.

**Consecuencia para el diseño:** la pantalla tiene que mostrar las dos cosas distinto. Los datos
con **su fuente** ("esto dice la landing, acá está el link"), el análisis como **propuesta**
("esto entiendo yo"). Si se mezclan, no hay forma de auditar nada.

Esto ya está resuelto en la cadena: es exactamente para lo que existe `notas.faltantes`.

### 2.2 — El editor drag & drop es el riesgo más grande

La Fase 2, Paso 3 pide un editor tipo Lovable: arrastrar bloques, editar colores y fuentes.

**Es un producto en sí mismo** — semanas de trabajo — y no aporta a lo que la hoja de ruta
quiere lograr, que es tener el producto y los creativos terminados. El dossier de capacidades
ya probó que **maquetar sale** (HTML+CSS → Chrome headless, con tapa, índice y diagramas).

**Lo que propongo en su lugar:** la landing sale como **HTML editable** y el editor es **un
campo de texto por bloque**. Cambiar una headline es abrir el bloque 1 y escribir. Mover el
bloque 9 arriba del 8 es cambiar un número de orden.

Eso cubre el 90 % de la necesidad con el 5 % del esfuerzo — y tiene una ventaja que el drag &
drop no tiene: **la salida sigue siendo HTML**, que es lo que después se publica. Un editor
visual obliga a exportar.

Si más adelante el editor visual se justifica, se construye sobre esto. Al revés no funciona.

### 2.3 — "Ingresar al perfil del anunciante" no está verificado

La Fase 1 dice: *"Ingresa a su perfil en Meta para ver qué otros productos vende."*

En el dossier de capacidades **ese ítem no aparece**. Lo que sí está medido es: entrar a la
**ficha de un anuncio** revela el `page_id` y el total de anuncios del anunciante. Eso es
distinto — y más chico — que "ver qué otros productos vende".

**Antes de diseñarlo hay que medirlo.** Si no se puede, la Fase 1 pierde ese punto y no pasa
nada: el resto del deep scrape se sostiene solo.

### 2.4 — No dice qué pasa cuando una etapa falla

La hoja de ruta asume que el deep scrape siempre trae lo que necesita. En la práctica: la
landing puede estar caída, el checkout puede ser una imagen, el precio puede estar en una
moneda rara.

La cadena ya tiene la respuesta (`notas.faltantes` + regla 9: un faltante no se usa como si
existiera). **La hoja de ruta tiene que decirlo explícitamente**, porque es lo que decide si la
pantalla muestra "no pude leer el precio" o un precio inventado.

---

## 3. La secuencia corregida

```
FASE A — DATOS              (sin IA, sin pantalla)        ← el primer paso
  a1. Landing: precio, checkout, bump/upsell, garantía
  a2. Anunciante: qué otros productos vende        (a verificar)
  a3. Video del anuncio: transcripción
  → escribe oferta_base + desglose.crudo, con "sin datos" donde falte

FASE B — ANÁLISIS           (con IA, por CLI)
  b1. Etapa 3: desglose, 11 etapas → nivel de conciencia
  b2. Etapa 4: promesa, 6 variantes + subpromesas
  → escribe desglose + promesa

FASE C — VALIDACIÓN HUMANA  (acá sí, pantalla)
  c1. Avatar    → tabla de derivación + imagen + tu aprobación
  c2. Promesa   → elegís entre las 6
  c3. Funnel    → 11 bloques → HTML editable (NO drag & drop)
  c4. Producto  → inventario de promesas + índice
  c5. Creativos → ángulos + 10 piezas + guion

FASE D — EJECUCIÓN
  d1. Ficha consolidada (JSON) → se la pasás a Hermes
  d2. Producción: PDF del producto + creativos (imagen, voz, video)
  d3. Manual: checkout y campaña
```

**Por qué A antes que C:** igual que con el motor, el deep scrape se puede probar por línea de
comandos sobre un anuncio real, sin construir una sola pantalla. Si no trae datos buenos, la
pantalla no tiene sentido. Y es el paso que la hoja de ruta llama "detrás de escena" — con
razón: es lo que menos se ve y lo que más sostiene.

---

## 4. El primer paso concreto

**Un script, `motor/modelar.py`, que recibe el link de un anuncio y devuelve una ficha
poblada.** Sin pantalla, sin botón, sin drag & drop.

Entrada:  link de la Biblioteca de Anuncios
Salida:   `datos/fichas/<id>.json` con `oferta_base` completa y todo lo que se pudo leer

Qué hace:
1. Reusa el scrapeo que ya funciona (`recolectar.py`) para los datos del anuncio.
2. Entra a la landing y saca precio, checkout, bonos, garantía.
3. Transcribe el video del anuncio si tiene.
4. Llena lo que puede y **marca `notas.faltantes` con lo que no**.
5. Corre las etapas de análisis (desglose + promesa) con la API.

**Criterio de terminado:** con un anuncio real, la ficha sale con `oferta_base` completa y sin
ningún campo inventado. Se verifica leyendo el JSON, no con una captura de pantalla.

Cuando eso funcione, el botón **Modelar** es un `subprocess` a ese script. El botón no tiene
lógica propia — solo dispara y muestra.

---

## 5. Lo que necesito para arrancar

- **Un anuncio real para probar** (link de la Biblioteca). Idealmente uno que ya haya pasado
  el filtro de persistencia.
- **Confirmar** si el editor drag & drop se reemplaza por el editor por bloque (punto 2.2).
- **Crédito de OpenRouter** si vamos a generar imágenes en la Fase C. Alcanza con unos dólares
  (US$0,039 por portada).
- Sigue pendiente de antes: **los 10–20 productos que se sepa que facturaron**, que calibran
  el índice. No bloquea este paso, pero sin eso el veredicto de la Fase 0 queda sin calibrar.
