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

### Decisiones tomadas
- [x] Alcance inicial: **uso personal, sin login ni pagos**
- [x] Dónde corre: **la PC** (escalable después; el scraper es un script suelto → cron)
- [x] Forma de uso: **panel-first** (el chat es un extra)
- [x] IA: **LLM propio** con API key propia — proveedor como línea de config
- [x] Modelo: `deepseek-flash` (el `pro` no hace falta: es redacción, no razonamiento)
- [x] Costo IA estimado: **menos de US$1/mes**

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

1.
2.
3.
