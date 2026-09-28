# RADAR — Qué hacen adheart y Adminer (y qué falta acá)

> Medido el 27-sep-2026 con capturas reales de la cuenta del usuario (Demo en adheart) y con la
> corrida propia de RADAR sobre la misma búsqueda.
>
> Búsqueda de referencia: **recetas keto**.

---

## 1. La misma búsqueda, los dos lados

| | adheart.me | RADAR (hoy) |
|---|---|---|
| Resultados declarados | **5.210** (5,21 mil) | **280** (lo que declara Meta para AR) |
| Mercados | **6 países en simultáneo** de 25 disponibles (vi MX, UY, AR, CL, CO, ES) | 1 país por corrida (AR) |
| Ventana | "Días activos: 90 días" (ventana temporal, no "corriendo hace 90+") | Solo el estado de hoy |
| Histórico | colecta **desde 2019** | no existe: no se reconstruye hacia atrás |
| Anuncios extraídos | — | 56 (de 280) |
| 90+ días corriendo | no lo declara | **6 de 56 = 10 %** → 🔴 cementerio |

**La brecha de 280 → 5.210 no es criterio, es volumen acumulado y multi-país.** Por país y por
ventana, adheart ve un orden de magnitud parecido al nuestro. Lo que no tenemos es el archivo.

---

## 2. Campo por campo: qué trae cada tarjeta

| Dato | adheart | Adminer | RADAR hoy |
|---|---|---|---|
| Anunciante + antigüedad | ✅ "hoy · 1 día" / "ayer · 2 días" | ✅ | ✅ días corriendo |
| **Bandera de país por anuncio** | ✅ | ✅ (BR) | ❌ |
| Creativo (imagen/video) + duración | ✅ 0:27, 0:32, 1:00, 1:58 | ✅ | ✅ imagen |
| Copy completo | ✅ | ✅ | ✅ |
| **Tags de ángulo con IA** | ✅ **PAIN · DEAL · BONUS · URGENT · NORISK · ASK · SIMPLE · CALL OUT · CROWD · EXPERT · GUIDE · IDEAL · MEDIA · UNIQUE** | parcial (generador de copy) | ❌ |
| **CTA detectado** | ✅ SHOP NOW · WHATSAPP MESSAGE · LEARN MORE · SEE DETAILS | ❌ | ❌ |
| **Dominio/producto de destino** | ✅ ketouruguay.com, api.whatsapp.com/send, mykky.es | ✅ | ✅ (se scrapea, no se muestra) |
| **Precio en moneda local** | ✅ $99 MXN · $2.499 ARS · 10.000 pesos | ✅ R$169,90 | ✅ (se scrapea, no se muestra) |
| Descargar creativo / uniquizar / copiar / compartir | ✅ 6 acciones por tarjeta | ✅ | descarga ✅ |
| Favoritos y boletín | ✅ | ✅ | ✅ guardados |
| Categorías con conteo | ✅ Gambling · E-commerce · Adult · Novel · Crypto · Finanzas · Educación · **Nutra** | ✅ nichos | mercado por keyword |
| Panel de filtros | 18 filtros (texto, enlace, campaña, dominio, página, app, IP, idioma, medio, plataforma, formato, lead-form, fecha, días activos, alcance, clasificación, último activo, categoría) | varios | búsqueda + filtros básicos |
| Expórtale el histórico de un anunciante | ✅ tracking de competidores | ✅ | ❌ |
| Resumen / búsqueda inteligente | ✅ | ✅ Trends (tráfico web) | ❌ |
| **Veredicto de mercado** (oro/maduro/cementerio) | ❌ | ❌ | ✅ **solo RADAR** |
| **Creación del producto** (ficha → promesa → funnel → PDF) | ❌ | ❌ | ✅ **solo RADAR** |

**Precio de suscripción** — adheart: start US$69/mes (3.000 búsquedas), pro US$89/mes (9.000),
Team a medida, anual -18 %, con promo de acceso completo a **US$29** y contador. Adminer: Gold
R$119 / Diamond R$239 (mensual o trimestral), 20k / 60k vistas de anuncios por mes.

---

## 3. Lo que hay que copiar, en orden de valor

1. **Los tags de ángulo con IA** (PAIN, DEAL, BONUS, URGENT, NORISK, ASK, SIMPLE, CALLOUT,
   CROWD, EXPERT, GUIDE, IDEAL, MEDIA, UNIQUE). Es exactamente el "creativo tagueado" que se
   pidió: la taxonomía ya está probada por otro producto y se puede aplicar a la etapa 7.
2. **CTA detectado por anuncio** (SHOP NOW / WHATSAPP MESSAGE / LEARN MORE): dice en qué paso
   del funnel está el competidor — tráfico directo, WhatsApp o captura.
3. **Bandera de país por anuncio** + búsqueda multi-país en la misma corrida.
4. **Precio y dominio en la tarjeta**, no solo en la ficha.
5. **Categorías con conteo** para barrer nichos sin escribir keywords.
6. **Ventana temporal** en el filtro (últimos 90 días, último activo) — el histórico propio
   empieza a servir en cuanto haya corridas diarias.

## 4. Lo que NO se puede copiar y cómo se compensa

- **El archivo histórico** (adheart desde 2019, Adminer 135 M de anuncios). No se reconstruye
  hacia atrás: es tiempo, no ingeniería. **Compensación:** criterio (persistencia), veredicto y
  producto. Y empezar a guardar corridas diarias **hoy**, que es el único insumo que se acumula.
- **La escala multi-país.** Compensación: profundidad en AR (que es el mercado del usuario) en
  vez de amplitud.

## 5. La confirmación más útil de todas

adheart tiene un filtro llamado **"Días activos"**. Es decir: nuestro criterio principal
—el tiempo corriendo— es el mismo que usa una herramienta que cobra US$69 al mes. La
diferencia es que ellos lo usan como filtro y nosotros como **veredicto** (🟢/🟡/🔴/⚫).
