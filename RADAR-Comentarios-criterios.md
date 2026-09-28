# RADAR — Minería de comentarios: qué se puede, dónde entra y con qué criterio

Probado de punta a punta el 27-sep-2026 en esta máquina. Todo lo de abajo son números medidos, no
estimaciones. Scripts: `tiktok/_comentarios2.py`, `tiktok/_diag_panel.py`, `tiktok/_sonda_instagram.py`.

---

## 1. Qué se probó y qué salió

### 1.1 TikTok: los comentarios se leen SIN login ✅

Se interceptan las respuestas XHR de `/api/comment/list` que la propia página pide: **el navegador
firma el pedido, nosotros leemos la respuesta**. No hay que descifrar la firma de TikTok.

| Qué | Resultado |
|---|---|
| Video de prueba | [@marianahidalgo.nutricion](https://www.tiktok.com/@marianahidalgo.nutricion/video/7483644555674406150) — 896.200 vistas, 653 comentarios |
| Páginas cosechadas | **23** (20 comentarios por página) |
| Comentarios crudos | **458** |
| Comentarios únicos | **203** después de descartar repetidos |
| Tiempo | ≈ 3 min de navegador con ventana visible |

**Trampas pagadas:**

0. **Hay que abrir la ventana (`headless=False`).** En headless la página llega degradada: el panel
   de comentarios no renderiza y el endpoint devuelve una respuesta vacía. Con ventana, anda de una.
1. **La búsqueda de TikTok NO sirve: pide login.** `/search/video?q=...` devuelve "Hubo un problema
   / Iniciar sesión" y 0 resultados. La página de un video y sus comentarios, en cambio, son
   abiertos. **Consecuencia: para descubrir contenido orgánico hay que entrar por otro lado**
   (Google/web search, el perfil del anunciante, o los "recomendados" de un video — que traen la
   misma cuenta, no el nicho).
2. **El contenedor scrolleable no es el que parece.** No tiene `data-e2e` útil: es
   `div[class*="DivCommentMain"]`. Scrollear `[data-e2e="comment-list"]` no dispara nada y parece
   que "no pagina". Diagnóstico: `tiktok/_diag_panel.py`.
3. **20 comentarios por request**, `has_more` viene siempre en 1: no sirve como corte. El corte hay
   que hacerlo por "N intentos seguidos sin comentarios nuevos".
4. **El piso de 20 es engañoso.** La primera página llega sola al cargar el video; si sólo se mira
   ahí, se cree que el video tiene 20 comentarios cuando tenía 653.

### 1.2 La capa orgánica barata: yt-dlp da las métricas sin navegador ✅

Para *descubrir* y *medir* videos no hace falta Playwright: `yt-dlp --skip-download` devuelve por
video, en ~2 segundos y sin cookies:

```
vistas | likes | comentarios | guardados
```

Medido sobre 7 videos del nicho "resistencia a la insulina" en TikTok:

| @cuenta | vistas | likes | coments | **guardados** | coment/vista |
|---|---|---|---|---|---|
| marianahidalgo.nutricion | 896.200 | 63.700 | 653 | 26.366 | 0,073 % |
| nutrimaga | 387.800 | 13.800 | 179 | 1.742 | 0,046 % |
| nancynutricion8 | 67.800 | 3.315 | 84 | 956 | 0,124 % |
| nancynutricion8 (otro) | 48.100 | 2.152 | 46 | 497 | 0,096 % |
| soynutri.salud | 46.400 | 1.401 | 22 | 181 | 0,047 % |
| biencomidosnutricion | 3.530 | 127 | 6 | 21 | 0,170 % |
| miamisurgeon | 3.157 | 108 | 14 | 12 | 0,443 % |

Esto es **el video 3 de los TikToks, medido**: "los reels que más comentarios, likes o guardados
tienen son los que ya validaron". Y sale gratis.

### 1.3 Instagram: los comentarios están detrás del login ❌

Probado sobre un post público del nicho. El **caption sí se ve** sin cuenta (sirve para leer la
oferta), pero los comentarios no: aparece el modal "No te pierdas ninguna publicación de…" /
"Regístrate en Instagram" y la lista no se renderiza. Las llamadas van por `/api/graphql` y no
devuelven comentarios sin sesión.

**Conclusión:** Instagram queda afuera hasta que haya una cuenta logueada (o su perfil de Chrome
con sesión). TikTok es la fuente de comentarios, gratis y sin cuenta.

### 1.4 La señal de "dolor textual" ES medible ✅

Sobre los 203 comentarios únicos del video de 653 comentarios:

| Dolor | Comentarios | % | Likes acumulados |
|---|---|---|---|
| peso / resultado ("bajé", kilos, "no puedo bajar") | 10 | 4 % | **910** |
| esperanza / fracaso ("perdiendo la esperanza", "no puedo") | 6 | 2 % | **891** |
| metformina | 13 | 6 % | 608 |
| inositol | 14 | 6 % | 22 |
| exámenes / diagnóstico (HOMA, endocrinólogo) | 8 | 3 % | 32 |
| ansiedad / antojo / chatarra | 8 | 3 % | 8 |
| tiempo / plazo ("¿en cuánto tiempo?") | 6 | 2 % | 17 |
| dinero / precio | 2 | 0 % | 10 |

Y las frases que salen listas para un gancho:

> "Voy a copiar todo lo que hiciste porque **ya estoy perdiendo la esperanza y la voluntad**" (870♥)
> "Llevo tomando **metformina más de 5 años**" (546♥)
> "**No puedo dejar la chatarra**" (3♥)
> "Ya cambié mis hábitos, nada de azúcar ni harinas… **llevo 3 meses sin nada pero sigo sin poder
> bajar de peso**" (4♥)
> "**Siempre tengo hambre**, trataré con Ozempic que es **mi último recurso**" (2♥)

---

## 2. La alineación: ¿en qué paso del proceso entra? (la pregunta)

**Decisión: los comentarios NO son una etapa de MERCADO. Son insumo de la etapa 3 (DESGLOSE) y de
la 7 (CREATIVOS).** No se cosechan "en la corrida de keywords".

**Por qué:** una keyword se busca en la Biblioteca de Anuncios, y **Meta no publica los comentarios
de los anuncios** — ahí no hay nada que raspar. Los comentarios viven en el **contenido orgánico**,
que es de una cuenta y de un video concretos. O sea: la unidad de la minería de comentarios es el
**anunciante/oferta**, no el mercado. Es una fuente nueva, en paralelo, que se cuelga del
`oferta_base`.

```
  1. MERCADO      ── keyword en la Biblioteca        (sin comentarios: no existen ahí)
  2. OFERTA BASE  ── elegir anunciante               ← acá se decide a quién minar
        │
        ├── NUEVA FUENTE: contenido orgánico del anunciante (yt-dlp)  ← métricas, gratis, diario
        │        └── comentarios del video que más engancha (Playwright, ~3 min)
        ↓
  3. DESGLOSE     ── AVATAR (dolores, lenguaje del mercado)  ← acá ENTRAN los comentarios
  4. PROMESA
  5. FUNNEL
  6. PRODUCTO
  7. CREATIVOS    ── ganchos y libretos                       ← acá se USAN
```

### Los tres modos, y cuándo usar cada uno

| Modo | Cuándo corre | Qué hace | Costo |
|---|---|---|---|
| **A — Métricas orgánicas** | **En la corrida diaria**, para cada anunciante que ya pasó el filtro (90+ días, no marca) | yt-dlp sobre sus últimos N videos → vistas, likes, comentarios, guardados, y la **curva día a día** | ~2 s por video, sin navegador |
| **B — Cosecha de comentarios** | **Sólo para la oferta base elegida** (etapa 2 → 3) | Abre el video que más engancha y baja hasta N comentarios | ~3 min de navegador |
| **C — A demanda** | Cuando el usuario aprieta "minar comentarios" en una oferta guardada | Igual que B, pero sobre cualquier pieza que se elija | ~3 min |

**Lo que NO hay que hacer:** minar comentarios de todos los anunciantes de la corrida. El volumen
no cambia el veredicto del mercado y multiplica el tiempo. Los comentarios son para **escribir el
creativo**, no para decidir en qué nicho meterse.

---

## 3. Los criterios de medición (dónde está la trampa)

### 3.1 Nunca rankear por frecuencia sola

Medido: **inositol aparece en 14 comentarios y junta 22 likes; "perdiendo la esperanza" aparece en
1 comentario y junta 870.** Si se rankea por cantidad de menciones, gana "inositol" (un dato
farmacológico, no un dolor). Si se rankea por likes, gana la desesperanza, que es lo que la gente
siente pero no escribe.

**Regla:** son **dos columnas distintas y no se mezclan**.
- **Frecuencia de mención** = el dolor que la gente **verbaliza** → es el texto del copy.
- **Likes del comentario** = cuánta gente **se identificó sin escribir** → es el dolor del gancho.

Un dolor que aparece en las dos (como "metformina": 13 menciones y 608 likes) es el más seguro.

### 3.2 El denominador obligatorio: comentarios por vista

203 comentarios suenan a mucho; sobre 896.200 vistas son **0,023 %**. Un video de 3.530 vistas con
6 comentarios tiene **0,17 %** — siete veces más intenso por vista. Sin el denominador, se repite el
error de "*menú económico familiar* tiene 1 anuncio" ya corregido en la skill: el número absoluto
miente.

| Métrica | Fórmula | Qué dice |
|---|---|---|
| **Intensidad de conversación** | comentarios / vistas | cuánto moviliza el tema. Referencia útil: 0,05 %–0,15 % |
| **Intención de guardar** | **guardados / vistas** | "esto me va a servir" — la señal más limpia de que el contenido resuelve algo. Medido: 2,9 % en el video grande, 0,6 % en el chico |
| **Dolor dominante** | comentarios que mencionan el tema, y sus likes por separado | las dos columnas de 3.1 |

**Piso de muestra:** con menos de 20 comentarios no se concluye nada (es la primera página, no el
video). Con 150+ únicos ya aparecen los patrones repetidos.

### 3.3 Cuidado con contar como dolor lo que es otra cosa

De los 203: 14 preguntas de producto ("¿dónde compraste el inositol?"), 8 de logística médica
("¿endocrinólogo o nutricionista?"), 2 de precio. Son **objeciones y preguntas frecuentes**, un
producto distinto del dolor: sirven para el guion de la landing y para el FAQ, no para el gancho.
Etiquetar cada comentario en `dolor` / `pregunta` / `objeción` / `testimonio` antes de contar.
Los **testimonios** ("a mí me funcionó", "yo ya lo revertí") son la prueba social más barata que hay.

---

## 4. Cambios que esto pide en la ficha

Campos nuevos (nombres propuestos para no chocar con los que ya existen):

```json
{
  "oferta_base": {
    "organico": {
      "plataforma": "tiktok",
      "cuenta": "@marianahidalgo.nutricion",
      "videos": [
        { "id": "...", "url": "...", "vistas": 896200, "likes": 63700,
          "comentarios": 653, "guardados": 26366,
          "intensidad": 0.00073, "intencion_guardar": 0.029, "fecha": "2026-09-27" }
      ]
    }
  },
  "desglose": {
    "avatar": {
      "dolores_textuales": [
        { "texto": "llevo 3 meses sin azúcar y sigo sin poder bajar de peso",
          "fuente": "<url del video>", "likes": 4, "etiqueta": "dolor" }
      ],
      "dolores_ranking": [
        { "tema": "peso/resultado", "menciones": 10, "likes_acumulados": 910 },
        { "tema": "esperanza/fracaso", "menciones": 6, "likes_acumulados": 891 }
      ],
      "preguntas_frecuentes": [],
      "objeciones_reales": [],
      "testimonios": [],
      "muestra": 203, "metodo": "tiktok_comentarios", "fecha_corrida": "2026-09-27"
    }
  }
}
```

El campo `muestra` es obligatorio: un ranking de dolores con 20 comentarios no vale lo mismo que uno
con 200, y eso tiene que verse en la ficha.

---

## 5. Límites y lo que falta

- **Instagram y Facebook: bloqueados** sin cuenta logueada (§1.3). Se destraba sólo con una sesión;
  no probado si conviene usar un perfil de Chrome del usuario.
- **La búsqueda de TikTok pide login** (§1.1, trampa 1), así que el descubrimiento de contenido
  orgánico **no** puede ser "buscar la keyword en TikTok". Hay que entrar por el perfil del
  anunciante o por buscador externo. Falta definir cuál, y probar el scraping de perfil.
- **La cosecha se cortó en 23 páginas por tiempo, no por tope**: `has_more` seguía en 1. Faltó
  medir cuánto tarda bajar los 653 y si hay rate limit con corridas largas.
- **No probado**: que el mismo video anuncie una oferta pautada (el puente orgánico → anuncio).
  Es el paso que hace que todo esto le sirva a RADAR y todavía no se validó con un caso real.
- **El piso de 20 comentarios** de la primera página puede hacer pasar un video por "poco
  comentado" cuando tiene 653. Muestrear siempre al menos 2-3 páginas.
