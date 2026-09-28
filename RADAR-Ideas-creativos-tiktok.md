# Ideas para creativos — 3 TikToks transcritos (27-sep-2026)

Transcripción local (faster-whisper, offline, $0) de tres videos de TikTok que el usuario pasó como
fuente de ideas para los creativos de RADAR. Los audios y las transcripciones crudas quedan en
`C:\Users\odiki\OneDrive\Desktop\Radar\tiktok\` (`*.mp3`, `transcripciones.json`, `salida.txt`).

## Las fuentes

| # | Link | Autor | Métricas | Qué es |
|---|---|---|---|---|
| 1 | [vt.tiktok.com/ZSb6yqvKx](https://vt.tiktok.com/ZSb6yqvKx/) | @rovarmarr | 231 s · 438 likes · 59 reposts | PARTE 2: cómo hacer **creativos réplica** y creativos de 0 copiando el guión de marcas argentinas |
| 2 | [vt.tiktok.com/ZSb6Htc7P](https://vt.tiktok.com/ZSb6Htc7P/) | @marian.ecomerce | 102 s · 95 likes | **Psicología de venta**: de dónde sacar el dolor real del nicho |
| 3 | [vt.tiktok.com/ZSb6HCNjW](https://vt.tiktok.com/ZSb6HCNjW/) | @marian.ecomerce | 59 s · 10 likes | Usar los **reels que ya viralizaron** como anuncios |

Los tres hablan de lo mismo desde otro ángulo: **nadie inventa el creativo, se copia uno que ya
funciona**. Ese es exactamente el trabajo de RADAR, así que los métodos se traducen casi 1 a 1.

---

## Lo que dicen (síntesis por audio)

### 1. Creativo réplica (@rovarmarr, 231 s)

Dos caminos para tener el primer creativo:

- **A — Creativo réplica:** tomar el creativo que ya funciona de una marca de afuera y pasarlo a
  español. Herramienta que nombra: *RecCloud* (pago, barato, con algunos gratis) → "traducir el
  video al español", modo **doblaje + subtítulos**, fuente de subtítulos inglés → español, y en el
  doblaje **clonación de voz** (recomienda clonar la propia voz; la "voz de ella" suena rara).
  Ajusta a mano los subtítulos que se salen del cuadro o que aparecen en dos posiciones distintas,
  saca la marca de agua, y recorta los silencios con Claude.
- **B — Guión adaptado de marca argentina:** elige una página de acá, ve un creativo que le gusta
  ("si te pasan 2 de estas 5 cosas, esto es lo que te falta"), lo descarga y se lo pasa a **Gemini**
  con el link de la página: Gemini lo transcribe y le **adapta el guión al producto propio**.
  Después arma el video con material de **Pinterest** (o IA tipo Flow) usando las búsquedas que le
  devolvió el modelo, y el audio en **Estudio** (gratis).

### 2. De dónde sale el dolor (@marian.ecomerce, 102 s)

El método más barato y más subestimado: **leer los comentarios del nicho**. Buscar el problema
principal ("bajar de peso", "resistencia a la insulina") y leer los comentarios: ahí la gente
cuenta su problema **con sus propias palabras**. Chat y Pinterest dan los problemas comunes;
los comentarios dan **cómo lo dice la persona**. Con dos o tres comentarios que repiten el mismo
dolor ya alcanza para armar el creativo. Y el creativo funciona cuando nombra el dolor en esos
términos exactos ("te cuesta bajar de peso porque tenés ansiedad por las cosas dulces y resistencia
a la insulina") → *"soy yo"*. Segundo movimiento: la resolución del problema en el mismo anuncio.

### 3. Reels virales como anuncios (@marian.ecomerce, 59 s)

Un reel que ya se viralizó, se comentó o se guardó **ya está probado gratis**: ese guion, esa imagen,
ese contenido le sirvió a la gente. Su método: mirar la competencia y el nicho, detectar los videos
con **muchos comentarios, likes o guardados**, y pasar esos mismos contenidos a anuncios para
campañas nuevas. Validar orgánico primero, pauta después.

---

## Qué adopta RADAR

RADAR hoy mira **solo anuncios pagos** (Biblioteca de Anuncios = estado de hoy + persistencia).
Los tres videos señalan dos capas que RADAR todavía no mira y que son más baratas que el scraping
de Meta:

### A. Capa orgánica: la señal previa a la pauta

Guardados, comentarios y likes de un reel de la competencia son una **prueba de guion que ya se
pagó sola**. Encaja en el nivel oferta sin tocar el criterio de persistencia:

```
viralidad = f(guardados, comentarios, likes) / alcance orgánico
```

Un creativo con muchos **guardados** sobre pocas visualizaciones es la señal más limpia (guardar =
"esto me va a servir"). Un 🔴 Marca con muchos seguidores y pocos guardados es marca, no oferta —
coincide con el criterio que ya dio la correlación −0,18 entre cantidad de anuncios y días corriendo.

### B. Mina de comentarios: el dolor con las palabras del cliente

Es el insumo que hoy falta en la ficha. La etapa de redacción del creativo escribe ganchos
inventados; con los comentarios escribe el dolor **textual** del cliente. Propuesta: un campo nuevo
en la ficha, `dolores_textuales[]`, con frases literales + fuente (URL del reel/creativo) y cuántos
comentarios distintos repiten la misma idea.

### C. Réplica estructurada: de "transcribir el video" a "extraer la estructura"

RADAR ya tiene la pata de transcripción verificada (ver más abajo). Lo que agrega el video 1 es el
destino: el guión no se copia, se **desarma en su estructura** (gancho → dolor → mecanismo →
prueba → CTA) y se regenera con el producto propio. Es el paso que convierte el espía en fábrica.

### D. Testear creativos con lo que ya funcionó, no con lo que se te ocurrió

Regla para el orden de producción: antes de generar un creativo nuevo, mirar si hay un creativo
propio o de la competencia que **ya validó orgánicamente**, y adaptarlo primero.

---

## Banco de creativos (listo para usar)

Ángulos y ganchos que salen directamente de los tres audios.

| # | Ángulo | Gancho | Origen |
|---|---|---|---|
| 1 | Diagnóstico por checklist | "Si te pasan 2 de estas 5 cosas, esto es lo que te falta. Te lo muestro en un minuto." | 1 (el creativo que copia) |
| 2 | Dolor nombrado con precisión | "Te cuesta bajar de peso porque tenés ansiedad por las cosas dulces y resistencia a la insulina." | 2 |
| 3 | Testimonio del comentario | "Leé los comentarios de este nicho y me vas a entender." (se leen comentarios reales en pantalla) | 2 |
| 4 | Dolor → mecanismo en el mismo anuncio | "Tenés ansiedad por la comida y las cosas dulces: esto es lo que tenés que hacer en tu alimentación." | 2 |
| 5 | Prueba social orgánica | "Este reel se guardó N veces. Ahora lo estoy pautando." | 3 |
| 6 | Detrás del proceso (creativo réplica) | "Así convierto un anuncio en inglés en uno en español sin perder el guión." | 1 |
| 7 | Guión de marca local adaptado | Tomar el creativo argentino que corre hace más días y **reescribir la primera línea** con el producto propio | 1 + criterio de persistencia de RADAR |

---

## Lo que este circuito aporta verificado (medido hoy en esta máquina)

- **Bajar el video de TikTok funciona** con `yt-dlp.exe` del venv de AutoValidadorPro
  (`2026.08.19`), sin cookies: resuelve el *JS challenge* de TikTok solo. Los links cortos
  `vt.tiktok.com/...` se siguen directo. Los 3 videos bajaron en segundos.
- **La transcripción local funciona**: faster-whisper `small` `int8`, detectó español en los tres
  (prob. 0,98–1,00), acentos y puntuación correctos. **Se puede prescindir de RecCloud y de Gemini
  para transcribir**: es exactamente lo que RADAR ya hace offline y gratis.
- **Costo real de la transcripción: tiempo, no plata.** 231 s de audio → 626 s de proceso;
  102 s → 132 s; 59 s → 130 s (los tiempos incluyen la carga del modelo). Total ≈ 15 min de CPU
  para 6,5 min de audio. Es el cuello de botella a tener en cuenta si se transcriben videos en lote;
  no hay costo por unidad.

## Límites y desacuerdos (para no copiar el método a ciegas)

- **Doblar el video de una marca ajena no es "copiar el guion", es republicar su material.** El
  video 1 dobla y resube el creativo tal cual. Eso pone el anuncio bajo riesgo de derechos y, más
  importante para la pauta, Meta castiga el creativo duplicado: dos anunciantes con la misma pieza
  compiten entre sí y el rendimiento cae. RADAR debería quedarse con la **estructura** y el material
  propio (camino B del video 1, que además es gratis).
- **La marca de agua no se puede sacar "así nomás".** Quitarla no cambia que el video sea el de otro.
- **Lo que dice RADAR de un video no se hereda:** los likes que muestra TikTok (438 / 95 / 10) no
  dicen nada del mercado del producto; son del video sobre el método. No usarlos como dato.
- **Los comentarios hay que medirlos, no leerlos "a ojo".** El video dice "con dos o tres comentarios
  que repiten el dolor ya alcanza". Para RADAR conviene contar cuántos comentarios distintos repiten
  la misma formulación y guardar el recuento: si no, es la misma trampa que el "1 anuncio" de
  *menú económico familiar*.
- **El scraping de comentarios y de guardados en TikTok/IG no está probado todavía** en esta máquina.
  Es la capacidad nueva que habría que medir antes de prometerla (mismo criterio que
  `RADAR-Capacidades.md`).

---

## Anexo — transcripciones completas

### Video 1 — @rovarmarr (231 s)

> ¿Cómo testear tu primer producto? En la parte 1 vimos cómo encontrar el producto y en esta parte
> vamos a ver cómo hacer los creativos. Tenemos dos opciones, uno es el creativo réplica que sería
> básicamente usar los creativos que encontramos de la marca de afuera y pasarlos a español y la
> segunda opción es agarrar guiones de marcas de nichos parecidos acá o el mismo nicho y adaptar sus
> guiones a nuestro producto. Vamos a ver cómo hacer los anuncios réplicas. Acá ya tengo un anuncio
> que elegí en la parte 1 del video. Una vez descargado el creativo lo que vamos a hacer es ir a esta
> página que se llama RecCloud, es una página que es de pago pero es muy barata y también tiene la
> opción de hacer un par de gustos gratis pero nos puede servir un montón porque básicamente te
> transcribe el audio al español y también te hace los subtítulos. Lo que tenemos que hacer es ir a
> la parte de soluciones y tocar traducir el video al español. Una vez que subimos nuestro video lo
> que vamos a hacer es seleccionar doblaje más subtítulos. [...] En el doblaje vos podemos elegir la
> clonación de vos que sería la misma voz usando el video o una voz de ella, yo recomiendo clonación
> de vos porque voz de ella se escucha muy raro y acá vamos a sacar los subtítulos. Esta parte sí es
> de pago pero es muy barata. [...] Marca de agua en este caso no tiene así que se la voy a sacar y
> vamos a tocar traducir. [...] En este caso hay muchos silencios porque bueno obviamente es para que
> quede la misma cantidad de segundos que el video original lo que podemos hacer es recortárselos con
> Claude, le pido a Claude que me lo recorte, le paso el video, le digo que recorte los silencios y lo
> hace muy rápido. Ahora vamos a ver cómo hacer los guiones de marcas argentinas adaptados al producto
> que vos elegís. [...] Vamos a ver uno de sus creativos: "si te pasan 2 de estas 5 cosas esto es lo
> que te falta, te lo muestro en un minuto". Este creativo me gusta, vamos a descargarlo y lo vamos a
> usar. Una vez que descargamos el creativo lo que vamos a hacer es ir a Gemini. [...] le vamos a
> pasar el guión y le vamos a pedir que lo transcriba. [...] Acá nos dejó la transcripción tal cual
> del video y acá nos adaptó el guión a nuestro producto para hacer el creativo. [...] Podemos irnos a
> Pinterest y buscar cosas como por ejemplo bien triplamado, panza hinchada, hierbas naturales, una
> persona cansada [...] o podemos hacerlo con IA. [...] Para el audio lo que vamos a hacer es ir a
> Estudio que esto sí es gratis y ya con eso tendríamos el creativo hecho.
>
> *Transcripción completa sin recortes:* `tiktok/transcripciones.json` (campo `texto`), y con
> marcas de tiempo en `salida.txt` / `marcas`.

### Video 2 — @marian.ecomerce (102 s)

> Saben de dónde pueden sacar buena info para armar sus creativos de forma gratuita y muy simple y
> conectando con la gente: mirar acerca de los problemas principales en el nicho de donde ustedes van
> a vender. Vamos a poner por ejemplo nutrición: "quiero bajar de peso pero tengo resistencia a la
> insulina", o buscan "resistencia a la insulina", o los problemas más comunes por dar un ejemplo, y
> lean los comentarios. La gente ahí está dando los testimonios de lo que te está pasando: "no, a mí
> me pasa esto, no me pasa que yo no puedo bajar de peso por esto, a mí me cuesta esto". Y ahí está
> todo cantado. Si bien Chat y Pinterest puede dar los problemas más comunes de su nicho, y ustedes
> ahí van a armar sus creativos, si ustedes llegan a leer los comentarios de la gente y hay dos o
> tres que combinan el mismo problema, ya está chicos, con eso pueden validar. Pero pónganse a leer
> comentarios, lean a la gente, escuchen a la gente, porque cuando ustedes armen un anuncio
> hablándole a esa persona: "me cuesta bajar de peso porque tengo mucha ansiedad" y vos le hablás a
> la persona "te cuesta bajar de peso porque tenés ansiedad por las cosas dulces y tenés la
> resistencia a la insulina" — yo, o sea, soy yo. Entienden cómo funciona: ustedes tienen que atacar
> el punto de dolor porque ahí la persona se siente identificada y también pueden armar un buen
> anuncio contando la resolución del problema: "bueno, tenés ansiedad por la comida y las cosas
> dulces, tenés que hacer esto, esto y esto en tu alimentación".

### Video 3 — @marian.ecomerce (59 s)

> Aprovecho esta pregunta para contarles que algo que me sirvió bastante es ver los reels que se me
> viralizaron en los TikToks de un tema puntual de mi ebook, por ejemplo, y usarlos a mi favor.
> Porque un reel que se te viraliza o que la gente comenta un montón o le da like llama la atención.
> Entonces es algo que bueno, estás pagando y no sabes si va a funcionar o no. Entonces fíjate en tu
> competencia o del nicho en el que vas a vender y fíjate videos o reels que tienen muchos
> comentarios, muchos likes o guardados, porque te está dando indicio de que es un video que tiene un
> guión o una imagen o un contenido que a la gente le sirve. O sea, contenido gratis que se va a
> viralizar: si es más gratis, si es más, le ponés plata. Entonces lo que yo hice fue eso: de mis
> productos los reels que se me viralizaron de mi Instagram los subía como anuncios y explotaban.
> Para nuevas campañas, nuevos anuncios, hago nuevas campañas. [corte]
