# RADAR — el motor

El motor es lo único que no se puede hacer después: **corre todos los días y guarda lo que
Meta muestra hoy.** La Biblioteca de Anuncios no tiene historial, así que un día sin correr es
un día que no se recupera.

## Qué corre

| Archivo | Qué hace |
|---|---|
| `config.json` | Las búsquedas (keyword + país), cuántos anunciantes medir por búsqueda y los tiempos de espera. **Acá se agregan keywords.** |
| `recolectar.py` | La corrida completa: entra a la Biblioteca, extrae los anuncios, mide los anunciantes y escribe todo. |
| `tablero.py` | Arma `Radar\tablero.html` con los datos del día: la tabla de persistencia, la temperatura y los anuncios. Autocontenido, se abre con doble clic. |
| `corrida_AAAA-MM-DD.log` | La salida cruda de cada corrida. |

```bash
cd "C:\Users\odiki\OneDrive\Desktop\Radar\motor"
"C:\Proyecto Bases\AutoValidadorPro\.venv\Scripts\python.exe" recolectar.py
"C:\Proyecto Bases\AutoValidadorPro\.venv\Scripts\python.exe" tablero.py
```

Flags: `--limite N` (probar con pocas búsquedas) · `--sin-anunciantes` (corrida rápida, sin
medir la temperatura).

## Qué guarda (crudo y métricas, por separado)

Separados a propósito: si mañana cambia el criterio, **la historia no se pierde**.

| Archivo | Contenido |
|---|---|
| `datos/crudo/AAAA-MM-DD.json` | El scrape completo del día: cada anuncio con su copy, imagen, dominio, precio, días corriendo. |
| `datos/metricas/AAAA-MM-DD.json` | Las métricas del día, sin los anuncios: totales, % de 90+, mediana, y los anunciantes medidos. |
| `datos/historico.csv` | Una fila por búsqueda por día. Es la serie para graficar. |
| `datos/anunciantes.csv` | Una fila por anunciante por día. **Esta es la temperatura.** |
| `datos/resumen.md` | El parte del día, listo para leer. |

## La temperatura

`anuncios activos de un anunciante hoy` menos `ayer`, en porcentaje.

Es la misma métrica que Adminer llama "temperatura" — ellos la calculan sobre cuánta publicidad
está recibiendo un producto. La diferencia: **acá no se confunde con "ventas"**. Un CPM alto no
prueba nada por sí solo (lo medimos: la cantidad de anuncios correlaciona −0,18 con los días
corriendo). Lo que manda sigue siendo la **persistencia**: nadie paga publicidad 90 días
seguidos perdiendo plata. La temperatura dice **cuándo cambió**, la persistencia dice **si vale**.

Por eso la temperatura **no existe hasta la segunda corrida**. La primera es la base.

## Programado

Cron diario, 7:00 (hora de Argentina). El parte se entrega al chat de Hermes y a Telegram.

- Ver: `hermes cron list`
- Correr a mano ahora: `hermes cron run <id>`

## Lo que todavía no hace

- Bajar los creativos (hoy guarda las URLs; las URLs de Meta expiran).
- Medir la landing del anuncio (precio y checkout reales).
- Etiquetar el ángulo de cada anuncio (DEAL / PAIN / BONUS…) como hace adheart.
- Publicar el tablero: hoy el prototipo es HTML suelto y lee datos de ejemplo.
