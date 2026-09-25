# RADAR — La cadena de creación

> Cómo ordenar la mentoría "Operación: Ventas automáticas" (Sistema Pedro&Mica) en una
> línea de producción donde **cada paso recibe lo que produjo el anterior**.
>
> Borrador 1 — 25-sep-2026

---

## 1. Por qué esto y no una lista de prompts

La mentoría son **6 prompts sueltos** que se usan a mano. El problema que marcaste es real
y el propio documento lo prueba: cada prompt **vuelve a pedir** lo que el anterior ya produjo.

- El de *Desarmar la oferta* termina: *"pedime la captura y el mercado objetivo"*
- El de *Rediseñar Oferta* arranca: *"pedime la página (captura/texto/URL) y el país objetivo"*
- El de *Funnel* no tiene forma de saber qué promesa se eligió en el paso anterior

**Cada vez que pegás a mano, el proyecto puede divergir.** Si elegís la promesa 4 y después
pegás la 2, ya no sabés qué estás modelando.

La solución no es "un prompt más largo": es **una ficha que se va completando**. Cada etapa
**lee** lo que ya está en la ficha y **escribe** lo suyo. Nunca se vuelve a pedir dos veces.

---

## 2. El marco de la mentoría

El curso tiene 4 pilares que alimentan un resultado:

```
   TRÁFICO   ·   COPYWRITING   ·   FUNNEL   ·   PRODUCTO
        \            |            |            /
         \           |            |           /
          ~~~~~~~~ MODELAGE CULTURAL ~~~~~~~~
```

Y su propio resumen del recorrido: **Mercado → Oferta → Mensaje → Funnel → Tráfico → Monetización**.

**Ojo con el orden.** El curso enseña *Tráfico* casi al final (módulo #10), pero el pilar
está primero en el diagrama. La secuencia real de trabajo es la de abajo: sin mercado y sin
oferta validada, producir creativos es tirar plata.

---

## 3. La ficha (el estado que viaja)

Esto es lo que hoy se copia y pega a mano. Es **un solo objeto** que se completa de arriba abajo.

| Campo | Lo escribe | Lo lee |
|---|---|---|
| `nicho` | vos | 1 |
| `keywords[]` | 1 | 2 |
| `oferta_base` (link, anunciante, ads activos, días, captura) | 2 | 3 |
| `desglose` (11 etapas de ingeniería reversa) | 3 | 4, 5 |
| `promesa_elegida` + `subpromesas[]` | 4 | 5, 8 |
| `funnel` (11 bloques de la landing) | 5 | 6, 8 |
| `producto` (entregables del MVP) | 6 | — |
| `checkout` (plataforma, bump, upsell) | 7 | — |
| `creativos[]` + `avatar` + `guion` | 8 | 9 |
| `campania` | 9 | — |

**La ficha es el activo.** Con esto, cambiar de criterio no obliga a volver a empezar:
se recalcula, igual que hicimos con las métricas de RADAR.

---

## 4. Las 9 etapas

Cada una dice: **qué lee · qué escribe · quién lo hace**.

### Etapa 1 — MERCADO · *¿en qué nicho me meto?*
- **Lee:** tu nicho (una palabra)
- **Escribe:** keywords, dolores, deseos, mecanismos, formatos, hooks, 20 combinaciones de búsqueda, top 10
- **Ejecuta:** **PROMPT 1 — Detector de ofertas** (+ agente Cosmos `agent_espion_meta_ads_001`)
- **Truco del curso que vale:** no buscar por nicho sino por **huella de infraestructura**
  (`impultienda`, `inlead.digital`, `Systeme.io`, `Lovable.app`). Buscando la plataforma
  encontrás a todos los que venden, en cualquier nicho.

### Etapa 2 — OFERTA BASE · *¿a quién modelo?*
- **Lee:** las keywords
- **Escribe:** la oferta elegida — link de la Biblioteca, anunciante, anuncios activos, **días corriendo**, captura
- **Ejecuta:** **manual** (Biblioteca de Anuncios)
- ⚠️ Acá va **nuestro** criterio, no el del curso (ver punto 6)

### Etapa 3 — DESGLOSE · *¿cómo está armada?*
- **Lee:** la oferta base + su captura (+ checkout + anuncios, son pantallas aparte)
- **Escribe:** las 11 etapas — producto, promesa, mecanismo, avatar, landing, oferta, checkout, order bump, upsell, funnel completo, anuncios
- **Ejecuta:** **PROMPT 2 — Desarmar la oferta**
- Bloques propios del curso: `1. PRODUCTO · 2. AVATAR · 3. PROMESA · 4. MECANISMO · 5. OFERTA`

### Etapa 4 — PROMESA · *¿qué prometo?*
- **Lee:** del desglose → promesa actual, avatar, mecanismo, objeción #1
- **Escribe:** puntaje /100 + 6 promesas + 5-6 subpromesas + **la elegida**
- **Ejecuta:** **PROMPT 3 — Rediseñar Oferta** (+ agente `agent_modelador_oferta_001`)

### Etapa 5 — FUNNEL · *¿cómo lo digo?*
- **Lee:** la promesa elegida + avatar + mecanismo
- **Escribe:** los 11 bloques de la página de venta
- **Ejecuta:** **PROMPT 4 — Página de venta**
- **Extra del curso:** plantilla de Lovable — `https://lovable.dev/invite/EC2BG7H`

### Etapa 6 — PRODUCTO · *¿qué entrego?*
- **Lee:** el funnel → qué prometió la landing
- **Escribe:** el MVP (mapa mental, PDF, app) y los productos complementarios
- **Ejecuta:** agentes — Cosmos `agent_creador_libros_digitales_001`,
  `agent_creador_productos_complementarios_001`, GPT "Nova Creator"; herramientas ChatGPT / Claude / Lovable

### Etapa 7 — CHECKOUT · *¿cómo cobro?*
- **Lee:** el precio de la oferta
- **Escribe:** plataforma, order bump, upsell, downsell
- **Ejecuta:** **manual** — Hotmart / Shopify / ImpulTienda; estrategia trip wire

### Etapa 8 — CREATIVOS · *¿cómo lo muestro?*
- **Lee:** el avatar + hook + la promesa elegida
- **Escribe:** 10 creativos con ángulos distintos, el avatar base y el guion de escenas
- **Ejecuta:** **PROMPT 5 — Creativos masivos** + **PROMPT 6 — Avatar base**; VEO 3 para animar, HeyGen para el clon, CapCut para editar

### Etapa 9 — CAMPAÑA · *¿cómo lo reparto?*
- **Lee:** los creativos + el funnel
- **Escribe:** Business Manager configurado y campaña de calentamiento andando
- **Ejecuta:** **manual** (10 pasos del curso)

### ⚠️ Etapa 10 — LANZA Y ESCALA · **el curso NO la tiene**
El módulo #9 existe con el título y **nada adentro**. Es el hueco más grande: el curso te
lleva hasta prender la campaña y ahí se corta.

---

## 5. Inventario completo de prompts

**El `.md` que me pasaste NO tiene todo.** Perdía **67 % del contenido** (38.000 de 63.500
caracteres) y con eso se perdieron 2 prompts enteros y todos los agentes.

### Prompts (6)
| # | Nombre | Módulo | Tamaño |
|---|---|---|---|
| 1 | **Promt detector de ofertas** | #1 | 3.270 |
| 2 | **Promt Maestro** (ingeniería reversa, 11 etapas) | #3 | 4.690 |
| 3 | **Promt Maestro** (promesas, rúbrica /100) | #4 | 4.170 |
| 4 | **Pormt maestro** (página de venta, 11 bloques) | #5 | ~1.300 |
| 5 | **🎯 PASO #1 – Perfect promt creativos masivos** | #8 | 3.630 |
| 6 | **Prompt base para crear el avatar** | #8 | 760 |

Los #5 y #6 **no estaban en el `.md`**.

### Agentes de Cosmos (externos, requieren cuenta paga)
- `agent_espion_meta_ads_001` — espiar competencia
- `agent_modelador_oferta_001` — modelar oferta
- `agent_creador_libros_digitales_001` — crear ebooks
- `agent_creador_productos_complementarios_001` — productos complementarios
- `agent_creador_publico_objetivo_001` — crear avatar
- `agent_analisis_experto_landingpages_001` — analista de landing
- `agent_creador_copy_paginas_001` — copys
- `agente_modelador_de_creativos` — modelar creativos

### Plataformas y herramientas mencionadas
- **Investigación paga:** `adminer.pro`, `adheart.me`
- **Checkout:** Hotmart, Shopify, ImpulTienda
- **Producto:** ChatGPT, Claude, Lovable
- **Video:** VEO 3, HeyGen, CapCut
- **App ya construida por el curso:** `https://protocolo-de-implementacion.lovable.app/`

---

## 6. Lo que la mentoría se contradice

En el módulo #1, entre las "señales a observar", el curso lista **"anuncios activos hace tiempo"**.
Es la señal correcta.

Pero la rúbrica práctica del módulo #2 usa **solo cantidad**:

- 3-10 anuncios activos → "Comenzando"
- 10-30 → "ya vende todos los días"
- +15 → poner en seguimiento para modelar

**La antigüedad desaparece de la rúbrica.** Y eso es exactamente lo que medimos con datos
reales: la cantidad de anuncios correlaciona **−0,18** con los días corriendo. Una oferta de
19 anuncios hace 130 días vale más que una de 312 sin historial.

En la Etapa 2 va nuestro criterio, que ya está medido:

- **Volumen = filtro de descarte** (¿es una marca grande? ¿es un banco, un retailer, una ONG?)
- **Días corriendo = la señal** (90+ fuerte, 180+ casi seguro)
- **Delta del conteo = el crecimiento** (aparece solo si el scraper corre todos los días)

---

## 7. Qué falta

1. **La Etapa 10 (Lanza y escala)** — el curso la tiene vacía. Hay que escribirla o marcar que no existe.
2. **Los videos** — hay 5 bloques de video ("REVISAR PILAR") que la API no baja. Si importan, hay que verlos aparte.
3. **Reescribir los 6 prompts como etapas de la cadena** — que cada uno declare qué campos
   de la ficha lee y qué campos escribe. Es el paso 2, y elimina el copiar y pegar.
4. **Decidir qué agentes de Cosmos seguimos usando** — son de una plataforma paga. Varios
   los podemos reemplazar con nuestro propio motor.

---

## 8. Dónde está el material

Todo bajado de Notion con la API, en `C:\Users\odiki\Desktop\Radar\mentoria\`:

- **`mentoria-completa.md`** — la mentoría entera, 1.429 bloques reconstruidos (63.570 chars)
- **`prompts-extraidos.md`** — los 6 prompts y agentes, extraídos y limpios
- **`estructura.json`** — el árbol completo con el contexto de cada bloque
- **`img/`** — las imágenes descargadas
- **`RADAR-CAMBIOS.md`** · **`RADAR-Forma-del-producto.md`** — el resto del proyecto
