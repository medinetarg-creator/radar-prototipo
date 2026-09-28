# Creativo #2 — "La balanza no se mueve" (pieza de muestra, 27-sep-2026)

Pieza completa del banco de ideas, armada con los **dolores textuales reales** medidos en los 203
comentarios del video del nicho (ver `RADAR-Comentarios-criterios.md`). Es la muestra de la etapa 7:
todo lo que el pipeline tiene que entregar por cada creativo, con los archivos ya producidos.

## Ángulo

**Dolor nombrado con precisión.** El ángulo no dice "bajá de peso": dice el dolor exacto que la
gente escribió con sus palabras. La prueba de que es el dolor correcto no es una opinión — está
medida: los comentarios sobre *peso/resultado* juntaron **910 likes** y los de *esperanza/fracaso*
**891**, los dos temas más "likeados" del video, con sólo 10 y 6 menciones. La gente no lo escribe:
le da like al que lo escribió.

- **Avatar:** mujer 35-45, Argentina/AMBA, probó de todo, el médico le nombró la resistencia a la
  insulina y le recetó metformina, sigue igual.
- **Dolor (textual):** *"llevo 3 meses sin azúcar ni harinas y sigo sin poder bajar de peso"* (4♥) ·
  *"ya estoy perdiendo la esperanza y la voluntad"* (870♥) · *"no puedo dejar la chatarra"* (3♥) ·
  *"llevo tomando metformina más de 5 años"* (546♥) · *"siempre tengo hambre, trataré con Ozempic
  que es mi último recurso"* (2♥) · *"a mí no me quisieron dar metformina, me dijeron que baje por
  mi cuenta"* (29♥).
- **Mecanismo:** el problema no es la fuerza de voluntad — es que el cuerpo no deja entrar la
  glucosa, y por eso se guarda. Sale de la línea del video: *"la resistencia a la insulina no se
  mejora prohibiendo alimentos"*.
- **Objeción que elimina:** "ya probé todo y no me funciona" → no probaste el orden correcto.

## Bloque 1 — Gancho (primeros 3 segundos)

Dos versiones para testear; la primera es la que está en el video de muestra.

| # | Gancho | Por qué |
|---|---|---|
| **A (usado)** | "¿Ya probaste de todo y la balanza no se mueve?" | Interpela sin nombrar el tema: la que lo vive levanta la cabeza. |
| B (alt.) | "Llevo 5 años con metformina y nadie me explicó esto." | Arranca en primera persona con el fármaco que apareció 13 veces en los comentarios. |

**Texto en pantalla (frame 1):**
> Nada de azúcar. Nada de harinas.
> Y la balanza no se mueve.

## Bloque 2 — Voz en off (39,8 s · 108 palabras)

> ¿Ya probaste de todo y la balanza no se mueve? Nada de azúcar, nada de harinas, gimnasio tres
> veces por semana, y igual el pantalón no te cierra. Y encima el médico te dijo: tenés resistencia
> a la insulina, tomá metformina. Llevás meses así. **Nadie te explicó que el problema no es la
> fuerza de voluntad.** Tu cuerpo no está dejando entrar la glucosa, y por eso todo lo que comés se
> guarda. En este video te muestro los tres cambios que sí mueven la aguja cuando tenés resistencia
> a la insulina, en orden, y sin pasar hambre. El primero lo podés hacer mañana en el desayuno.
> Escribí DESAYUNO y te lo mando.

Estructura: dolor (0-12 s) → giro/devolución de la culpa (12-20 s) → mecanismo (20-27 s) →
promesa concreta y CTA (27-40 s).

## Bloque 3 — Copy del anuncio (texto en Meta)

**Primaria:**
> Si venís haciendo todo "bien" y la balanza sigue igual, no es falta de voluntad.
> Cuando tenés resistencia a la insulina, la glucosa no entra a la célula: se guarda. Por eso el
> cuerpo te pide comer más y el esfuerzo no rinde.
> Los 3 cambios que sí mueven la aguja, en orden, y sin pasar hambre 👉 escribí **DESAYUNO** y te los
> mando.
> ⚠️ Material educativo. No reemplaza la consulta médica.

**Titular:** La balanza no se mueve (y no es tu culpa)
**Descripción:** Los 3 cambios, en orden. Sin pasar hambre.
**CTA:** Enviar mensaje · WhatsApp

## Bloque 4 — Prompt de imagen (inglés, texto en español)

```
Vertical 9:16 photo for a Meta ad, first frame. A 38-year-old Latin American woman in a small
bright kitchen at 9 pm, wearing a casual home t-shirt, sitting at the table with an open notebook
and a plate with half a piece of cake pushed aside. She looks tired and frustrated, one hand on her
lower belly, the other holding a phone. Soft warm indoor lighting, natural realistic photography,
shallow depth of field, no text on the image, commercial advertising quality, authentic and not
over-styled. Tall vertical framing.
```

**Truco verificado:** para que devuelva vertical hay que mandar
`"image_config": {"aspect_ratio": "9:16"}` en el body. Sin eso devuelve **1024×1024 cuadrado** y el
video hay que recortarlo o rellenarlo. Con eso devolvió **768×1344** (9:16 exacto).

## Las piezas producidas

| Archivo | Qué es |
|---|---|
| `tiktok/creativo2_voz.mp3` | Voz en off, 39,8 s, es-AR (Edge local, $0) |
| `tiktok/creativo2_imagen_vertical.png` | Frame 1, 768×1344, generado por OpenRouter (US$0,039) |
| `tiktok/creativo2_texto.txt` | El texto en pantalla del frame 1 |
| `tiktok/creativo2_creativo.mp4` | **La pieza terminada**: 1080×1920, h264+aac, 40,4 s, $0 de edición |

Comando con el que se armó (ffmpeg, sin instalar nada):

```bash
ffmpeg -y -loop 1 -i creativo2_imagen_vertical.png -i creativo2_voz.mp3 \
 -vf "scale=1080:1890,pad=1080:1920:0:15:black,\
      zoompan=z='min(zoom+0.0008,1.12)':d=1:s=1080x1920:fps=25,\
      drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':textfile='creativo2_texto.txt':\
      fontcolor=white:fontsize=54:line_spacing=12:box=1:boxcolor=black@0.45:boxborderw=22:\
      x=(w-text_w)/2:y=150,format=yuv420p" \
 -c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 128k -shortest creativo2_creativo.mp4
```

Verificado con `ffprobe`: `h264 · 1080×1920 · 40,44 s` + `aac · 39,79 s` (el video dura lo que el
audio, `-shortest` hace su trabajo) y el frame 1 revisado a ojo: texto legible arriba, imagen
vertical sin deformar.

**Costo total de la pieza: US$0,039 y ~4 minutos.** Lo único manual que queda es subirla a Meta.

## Lo que el pipeline tiene que devolver por cada creativo (recordatorio de contrato)

Cada pieza sale con los seis campos poblados, no con un guión suelto:
**ángulo · gancho · copy · prompt de imagen · texto en pantalla · voz en off**. Y ahora también
**los dolores textuales que la sostienen**, con fuente y likes, para poder defender por qué el
gancho dice lo que dice.
