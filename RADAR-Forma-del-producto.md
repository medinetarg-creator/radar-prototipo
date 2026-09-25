# RADAR — Forma del producto

**Versión:** borrador 1 · 25 de septiembre de 2026
**Estado:** diseño para revisar. Todavía no hay una línea de código de producto.

---

## 1. Qué es, en una frase

Una web que mide la Biblioteca de Anuncios de Meta todos los días y te dice **dónde conviene meterse** (el mercado) y **qué copiar** (la oferta) — con datos medidos, no con opiniones.

Es la diferencia entre preguntarle a un consultor "¿qué nicho está bueno?" y **ver el número**.

---

## 2. Los dos niveles (esto ordena todo lo demás)

El error más común es mezclarlos. Son dos preguntas distintas, con dos criterios distintos:

| | **LA CANCHA** (mercado) | **LOS JUGADORES** (oferta) |
|---|---|---|
| Pregunta | ¿En qué subnicho me meto? | ¿Qué anuncio copio? |
| Unidad | Keyword | Oferta (anunciante + producto) |
| Se mide con | Competencia + Supervivencia | Persistencia + Crecimiento |
| Pantalla | **Mercados** | **Ofertas** |
| Ejemplo real (medido) | `repostería para vender` AR → 3.300 anuncios, **10% sobrevive** → 🔴 cementerio | Una oferta de 210 días corriendo con 143 anuncios activos |

**El orden importa:** primero elegís la cancha, después el rival. La librería de ofertas más linda del mundo no sirve si el mercado está muerto.

---

## 3. Las pantallas

Panel-first: entrás y ya está todo medido. El chat es un extra, no el camino principal.

```
RADAR
├── 1. Tablero          ← la home: qué cambió desde ayer
├── 2. Mercados         ← LA CANCHA: keywords medidas y su veredicto
│      └── detalle de keyword
├── 3. Ofertas          ← LOS JUGADORES: ranking de lo modelable
│      └── ficha de oferta
├── 4. Recomendados     ← qué hacer hoy (lista de acciones)
├── 5. Guardados        ← tu seguimiento, con evolución
├── 6. Nichos           ← el agente: de un nicho a keywords testeables
└── 7. Chat             ← preguntar en lenguaje natural (cajón lateral)
```

### 1 · Tablero (home)

**Para qué:** abrir y en 10 segundos saber si hay algo que hacer hoy.

- **KPIs:** mercados vigilados · ofertas en librería · ofertas probadas · seguimiento activo
- **Qué se movió:** cambios de las últimas 24 h en ofertas y mercados
- **Top oportunidades:** las 6 mejores por índice
- **Estado del sistema:** última corrida, próxima corrida, errores, días sin medir ⚠️
  *(crítico: si el scraper se cae, el historial tiene un hueco y hay que verlo)*

### 2 · Mercados (LA CANCHA)

**Para qué:** decidir dónde jugar.

Lista de keywords, cada una con:
- **Competencia** — anuncios activos totales
- **Supervivencia** — % de anuncios con 90+ días corriendo
- **Anunciantes** — cuántos distintos (fragmentación)
- **Veredicto** — 🟢 oro · 🟡 maduro · 🔴 cementerio · ⚫ no existe
- **Tendencia** — cómo se movió en 30 días

**Detalle de keyword:** los anuncios que corren ahí hoy, los anunciantes que dominan, y la curva histórica de las dos métricas.

**Acción:** "+ Medir keyword" → se encola para la próxima corrida.

### 3 · Ofertas (LOS JUGADORES)

**Para qué:** elegir qué modelar.

Es la librería del prototipo, pero con el criterio corregido: ordena por **antigüedad + crecimiento**, y la cantidad de anuncios es filtro de descarte, no mérito.

Cada tarjeta: creativo · anunciante · copy · señal · anuncios · días corriendo · precio · dominio.

**Ficha:** creativo grande, copy completo, histórico de anuncios activos, datos del anunciante, links reales (Biblioteca / landing / checkout) y tu seguimiento.

### 4 · Recomendados (qué hacer hoy)

**Para qué:** que no tengas que recorrer la librería. Esta pantalla **no es un catálogo, es una lista de tareas**.

Tres bloques, cada ítem con una acción explícita:

- 🟢 **Modelar** — oferta nueva que cumple el criterio (con el porqué en una línea)
- 🟡 **Vigilar** — está creciendo pero todavía no tiene antigüedad suficiente
- 🔴 **Salir** — una que tenías guardada y se está apagando

Se regenera en cada corrida.

### 5 · Guardados (tu seguimiento)

**Para qué:** no perder el hilo de lo que estás modelando.

- Tabla con miniatura, oferta, estado, días desde que la guardaste
- **Evolución:** el conteo de anuncios día por día (la curva real, no sintética)
- Estado propio: `por testear` · `testeando` · `funcionando` · `descartado`
- Notas libres
- **Alerta** cuando una guardada cae más de X% en una semana

### 6 · Nichos (el agente)

**Para qué:** convertir una idea vaga en keywords medibles.

Entrás con un nicho ("Recetas") y devuelve subnichos — **pero con una corrección clave sobre el prompt original**: cada subnicho se convierte en **frases testeables**, no en conceptos, y **se miden antes de recomendarse**.

> El prompt de COSMOS proponía "menú económico familiar" como prioridad #2. Medido: **1 anuncio**. La frase que la gente realmente usa es "menu semanal" (360 anuncios, 31% de supervivencia). El agente da conceptos; el sistema tiene que dar keywords con número.

### 7 · Chat

Cajón lateral. Preguntás en lenguaje natural y responde **con los datos de la base** (no con lo que el modelo "cree"). Ej: *"¿qué pasó con air fryer este mes?"* → contesta con la serie histórica real.

---

## 4. El criterio (las fórmulas)

### Nivel mercado

```
competencia   = anuncios activos totales de la keyword
supervivencia = % de anuncios con 90+ días corriendo
fragmentación = anunciantes distintos / anuncios relevados
```

**Índice de oportunidad del mercado (0–100):**

```
oportunidad = supervivencia × (1 − min(1, log10(total) / log10(20000)))
```

La lógica: la supervivencia dice *cuánta plata probada hay*; el logaritmo del total **castiga la saturación con rendimientos decrecientes** (pasar de 500 a 1.000 anuncios duele; pasar de 10.000 a 10.500 no cambia nada).

Probado con los datos reales medidos:

| Keyword (AR) | Total | Superv. | Índice |
|---|---|---|---|
| air fryer | 500 | 44% | **16,4** |
| recetas sin azúcar | 1.800 | 54% | **13,1** |
| air fryer (MX) | 810 | 13% | 4,8 |
| recetas | 11.000 | 52% | 3,1 |
| comidas económicas | 60 | 4% | 2,3 |
| repostería para vender | 3.300 | 10% | **1,8** |

El orden coincide con el análisis a mano. **Falta calibrarlo con ofertas que sepas que ganaron** — por eso te lo voy a pedir.

### Nivel oferta

| Peso | Señal | Qué mide |
|---|---|---|
| 🔴 Alto | **Días corriendo** | Que el CPA da. Es plata puesta todos los días |
| 🔴 Alto | **Δ anuncios del anunciante** (14 / 30 días) | Escalado real |
| 🟡 Medio | Varias versiones del mismo anuncio | Están optimizando → convierte |
| 🟡 Medio | Expansión de plataformas / países | Están ampliando |
| 🟡 Medio | Precio y embudo (landing) | Que pueda pagar el CPA |
| ⚪ Filtro | Volumen alto + pocos días | **Descarte:** campaña de marca |

### Señales resultantes

| Señal | Regla |
|---|---|
| 🟢 **Escalando** | 90+ días **y** sumando anuncios |
| 🔵 **Consolidada** | 180+ días, volumen estable |
| 🟠 **Prometedora** | –90 días pero ya creciendo |
| ⚪ **En prueba** | –90 días sin crecimiento |
| 🔴 **Marca** | 120+ anuncios y –45 días → **descartar** |

---

## 5. El modelo de datos

Seis tablas. Lo importante: **se guarda el crudo y lo derivado**.

```
keywords            (id, texto, pais, nicho, activa, creada)
keywords_mediciones (keyword_id, fecha, total, anunciantes,
                     mediana_dias, pct_90, veredicto)      ← 1 fila por día

anunciantes         (page_id, nombre, pais, primera_vez, ultima_vez)
anunciantes_mediciones (anunciante_id, fecha, ads_activos) ← la curva de crecimiento

ofertas             (id, anunciante_id, dominio, titulo, pais, nicho,
                     precio, checkout, embudo, primera_vez, activa)
ofertas_mediciones  (oferta_id, fecha, anuncios_activos, dias_corriendo) ← EL RADAR

anuncios            (id_biblioteca, oferta_id, copy, creativo_url,
                     primera_vez_visto, ultima_vez_visto, activo)

guardados           (oferta_id, estado, notas, fecha_guardado,
                     estado_anterior, cambiado)
corridas            (fecha, inicio, fin, ok, errores)     ← salud del sistema
```

**Regla de oro:** el scrape crudo se guarda **sin procesar** (JSON), y las métricas se calculan aparte. Así, cuando cambies el criterio —y lo vas a cambiar— **podés recalcular todo el historial sin volver a scrapear**. Si no hacés esto, cada cambio de criterio te borra la historia.

---

## 6. La rutina diaria

```
06:00  el scraper corre (una vez al día)
       ├─ mide las keywords activas            → keywords_mediciones
       ├─ releva los anunciantes seguidos      → anunciantes_mediciones
       ├─ releva las ofertas guardadas         → ofertas_mediciones
       ├─ descubre ofertas nuevas
       └─ baja los creativos nuevos
06:20  calcula: veredictos, índices, deltas
06:25  arma el parte: qué se movió, recomendaciones nuevas, alertas
       → recién ahí termina la corrida
```

La web **solo lee**. Nunca scrapea cuando la abrís: si abrir la app tarda 40 segundos, no la usás.

---

## 7. Dónde corre: hoy en tu PC, mañana en la nube

**Hoy, costo cero:**

| Pieza | Dónde | Cómo |
|---|---|---|
| Scraper | Tu PC | script de línea de comandos + Programador de tareas de Windows, 1 vez por día |
| Base de datos | Tu PC | un archivo SQLite |
| Web | Tu PC | servidor local, `localhost:PUERTO` |
| IA (briefs y redacción) | API | tu key de OpenRouter — centavos por informe |

**Sí, se escala. Y para que sea mover una pieza y no reescribir, hay 3 reglas que hay que respetar desde hoy (son gratis):**

1. **El scraper es un script suelto, no código de la web.** Escribe en la base; la web solo lee. El día que lo quieras en la nube, copiás el script y su tarea programada — que en Linux es un `cron`, o sea lo mismo. **Cambia una ruta, no una arquitectura.**
2. **La base es SQLite pero se escribe con SQL estándar.** Cuando pases a multiusuario, SQLite → Postgres es una migración, no un rewrite. (espíad usa Supabase, que es Postgres.)
3. **`user_id` en todas las tablas desde el día uno**, siempre en `1`. Agregar login después es sumar una tabla, no refactorizar todo.

**Lo que perdés hoy por estar en tu PC:** los días que esté apagada, no hay medición → **hueco en el historial**. Y no se recupera: la Biblioteca no guarda el pasado.

Mitigación: al prender la PC, el scraper corre igual (catch-up). No rellena el hueco, pero no acumula más.

**Costo de escalar** (cuando quieras): VPS USD 6–10/mes. Y a partir de cierto volumen de consultas diarias, Meta empieza a bloquear la IP → ahí entran proxies (~USD 20–50/mes). Para uso personal, no hace falta.

---

## 8. El stack

Deliberadamente aburrido, y todo ya probado en tu máquina:

- **Scraper:** Python + Playwright *(ya funciona — son los scripts de estos días)*
- **Base:** SQLite
- **Backend/web:** FastAPI (Python) sirviendo la web
- **Front-end:** HTML + JS sin build *(el sistema de diseño del prototipo se reusa tal cual)*
- **IA:** DeepSeek vía OpenRouter (o directo — es una línea de config). Solo para redactar briefs y resúmenes; **el 95 % del sistema no usa IA**
- **Modelo:** `deepseek-v4-flash`. No hace falta el `pro`: esto es redacción, no razonamiento complejo. Costo real estimado: **menos de US$1 por mes**
- **Programación:** Programador de tareas (Windows) → cron (Linux)

**Por qué no más:** nada de React, Docker, ni frameworks. Es una herramienta personal de una sola persona. Cada capa de más es una cosa que se rompe un domingo.

---

## 9. El roadmap

Ordenado por valor, no por dificultad. Cada fase sirve sola.

| Fase | Qué | Por qué en este orden |
|---|---|---|
| **0** | **El motor** — scraper + base + métricas. Sin interfaz. | Si el motor no es confiable, la web es una mentira linda. Se prueba por línea de comandos unos días |
| **1** | **Tablero + Mercados** | Es la decisión más valiosa: la cancha antes que el rival |
| **2** | **Ofertas + ficha** | Los jugadores. Reusa el prototipo y su criterio ya corregido |
| **3** | **Guardados + seguimiento** | Ahí el producto deja de ser una foto y empieza a ser un radar |
| **4** | **Recomendados** | Recién ahora hay historial suficiente para recomendar con fundamento |
| **5** | **Nichos (el agente)** | El brief medido: la entrada de todo el sistema |
| **6** | **Landing** — precio, embudo, checkout | Completa el criterio de la oferta |
| **7** | **Chat** | El extra, no el camino |
| — | *Multiusuario + pagos* | Cuando el de arriba funcione y vos lo uses todos los días |

**La fase 0 no tiene pantalla y es la más importante.** Antes de dibujar un tablero hay que confirmar que la medición diaria no falla.

---

## 10. Lo que necesito de vos

### Para arrancar la fase 0
1. **Una API key de IA.** Sirve la de **DeepSeek que ya tenés**. Si preferís OpenRouter, también — las dos son compatibles con OpenAI, el código es idéntico y el proveedor se cambia en **una línea de config**. Costo real: menos de US$1/mes.
2. **Dónde vive el proyecto:** ¿`C:\Proyecto Bases\RADAR`? ¿`K:\Infoproducto`?
3. **Las keywords iniciales.** Te propongo arrancar con las 16 que ya medí (recetas): sirven de línea base y ya sabemos qué esperar.

### Para calibrar el criterio (lo más valioso que me podés dar)
4. **10–20 ofertas que sepas que facturaron** — o que te consta que escalaron. Con eso ajusto los pesos del índice en lugar de usar umbrales inventados. Sin esto, el criterio es un buen razonamiento; con esto, es un criterio validado.
5. **Nichos donde ya tenés datos propios** (Medinet: salud, obras sociales). Ahí tenés una ventaja que espíad no tiene: conocés la demanda real, no la inferís.

### Para decidir el alcance
6. **¿Qué mercados?** Hoy medí AR y MX. ¿Sumamos BR, CO, US, ES, PT?
7. **¿Cuántas keywords por corrida?** Cada una × país ≈ 40 s. 20 keywords × 3 países ≈ 40 min diarios. Es el techo práctico en tu PC.

---

## Anexo · Lo que ya está probado

Nada de este documento es teórico. Todo esto ya corrió en tu máquina:

- ✅ Extracción de anuncios de la Biblioteca **sin cuenta y sin API** (Playwright)
- ✅ **279 anuncios** relevados en 6 búsquedas, **168 creativos** descargados
- ✅ Conteo de anuncios activos por anunciante (ficha del anuncio → `~N resultados`)
- ✅ Medición de competencia y supervivencia por keyword (16 mediciones)
- ✅ El hallazgo que corrige el criterio: **correlación −0,18** entre cantidad de anuncios y días corriendo
- ✅ Un prototipo navegable con el criterio ya corregido

**Lo único que falta es convertir esos scripts sueltos en un motor con memoria.**
