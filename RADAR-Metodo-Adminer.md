# RADAR — El método de Adminer, sacado de su propia trilha

> Fuente: los 7 videos de la playlist "Trilha: Sua primeira venda com a Adminer", subtítulos
> originales en portugués bajados de YouTube (no transcripción propia).
> Fecha: 27-sep-2026.

---

## 1. Su recorrido (7 videos)

| # | Video | Qué enseña |
|---|---|---|
| 1 | Como encontrar um produto para vender | Filtrar el ranking de **produtos quentes** |
| 2 | Como validar se o produto realmente vende | **La temperatura** y la curva de crecimiento |
| 3 | Colocando o produto na sua loja | Exportar el producto a la tienda |
| 4 | Encontrando anúncios que estão funcionando | La **biblioteca Premium** y sus filtros |
| 5 | Organizando seus testes de produtos | La **esteira de testes** (kanban) |
| 6 | Iniciando o teste do produto | Presupuesto, CTR/CPC/CPM, conversión |
| 7 | Agora é com você | Cierre |

---

## 2. La métrica central: la TEMPERATURA

- Escala de **0 a 150°**, y **no se calcula sobre ventas: se calcula sobre inversión en tráfico**.
  Monitorean todos los días los **anuncios activos** de cada producto en Facebook. Más anuncios
  activos = más inversión = "más está vendiendo".
- Tags automáticas: **~12° "testando"** · **~30° "escalando"** (la inversión viene subiendo) ·
  **128° "escalado"**.

### Cómo eligen (la parte contraintuitiva)

> "En vez de enfocarnos en esos productos que ya están vendiendo mucho, lo ideal es buscar
> productos **en crecimiento**, que todavía no están saturados."

- Filtrar por **mayor crecimiento** (%), no por mayor temperatura.
- Bajar el rango de anuncios (dejó **1 a 47** anuncios corriendo) y ordenar por crecimiento →
  aparecen productos de 20-50° con crecimiento de **hasta 2.300 % en 7 días**.
- Para quien arranca: temperatura **20-70°** y crecimiento **> 100 %**.

### Cómo validan (video 2)

1. **Temperatura** en el rango.
2. **Crecimiento > 100 %**.
3. **Gráfico de los últimos 7 días**: creciendo / estabilizado / cayendo.
4. **Pico de escala**: "si el pico fue hace 2-3 meses, el producto puede estar en caída."
   *Ejemplo que da: un producto pasa de 3 anuncios activos un día a 28 al día siguiente.*
5. **Criativo vencedor**: "hay un patrón de creativo que se repite → probablemente es el
   creativo ganador".
6. **Anúncios relacionados**: productos que el mismo público compra → ideas de **upsell**.
7. Proveedores (AliExpress), variación de precio, análisis de tráfico de la tienda
   (visitas del último mes), página de ventas, público (género/edad/intereses),
   generación de copy con IA (3 opciones), denunciar producto trucho (alimenta su IA).

---

## 3. La biblioteca Premium (video 4)

- **"Hoy tenemos más de 195 millones de anuncios"** (la landing dice 135 M: los números no
  coinciden entre su propia web y su propio video).
- Filtros que usan: fecha de publicación (estacionalidad: Pascua, Día del Niño),
  **checkout** (pegar la URL del checkout para encontrar anuncios que lo usan), idioma,
  **botón CTA**, tipo de medio (imagen/video), nicho, cantidad de anuncios activos,
  actualizados recientemente / recién publicados, y **"período mínimo activo"**
  (anuncios corriendo hace más de 10 días, 22 días…).
- Su razonamiento textual: *"Nadie va a estar invirtiendo en Facebook, quemando dinero,
  si ese producto no vende."*
- También buscan por **infoproductos**, por dropshipping y por **low ticket** (20 a R$100).
- Y su principio editorial, que es el mismo de RADAR:

> **"La idea no es copiar esos anuncios, sino entender la estructura, el abordaje y la promesa
> de lo que funciona hoy en el mercado."**

---

## 4. La esteira de testes (video 5)

Un **kanban** con etapas: `triagem → aprobados para la tienda → agregando a la tienda →
haciendo creativos → listos para anunciar → anunciando → validados / no validados`.
Cada tarjeta guarda: link del producto, link del anuncio en Facebook, link del proveedor,
link del video y notas (para el que ayude en la operación). Aparte, **favoritos con colecciones**
por nicho o por estacionalidad.

## 5. El test (video 6)

- Presupuesto inicial **R$5-10 por día por conjunto de anuncios**. "El objetivo no es escalar:
  es juntar datos."
- Métricas: **CTR, CPC, CPM y conversión de la página**.
- Su diagnóstico: *"Cuando un test no genera ventas, no necesariamente el problema está en el
  producto: puede estar en el creativo, en la promesa, en la página o en el público."*
  El trabajo es encontrar la combinación **producto × creativo × página**.

---

## 6. Choque con el criterio de RADAR (y quién tiene razón)

| | Adminer | RADAR (medido) |
|---|---|---|
| Señal de que vende | **Cantidad de anuncios activos** ("temperatura") | ⚠️ **no sirve sola**: correlación −0,18 con días corriendo |
| Señal principal | Crecimiento en 7 días | **Persistencia** (días corriendo) + delta del conteo |
| Productos saturados | Los evitan (bajan el rango de anuncios) | Los detectan y descartan (🔴 cementerio / Marca) |
| Producto en caída | Pico de escala hace 2-3 meses | Caída del conteo en las corridas diarias |

**El choque es real pero parcial.** Adminer usa la cantidad como *proxy de ventas*, y RADAR
midió que la cantidad sola no distingue una oferta copiable de una campaña de marca
(Santander: 610 anuncios / 17 días). Pero **después ellos mismos contradicen su propia métrica**:
mandan a los principiantes a **no** mirar los productos de temperatura alta, y usan
"período mínimo activo" y el "pico de escala" — que es exactamente el criterio de RADAR.

**Conclusión:** nuestro criterio no es una teoría; es la práctica que usan las dos herramientas
que cobran por esto (adheart: "Días activos"; Adminer: "período mínimo activo" + pico de escala).
La diferencia es que ninguna de las dos lo convierte en **veredicto** (🟢/🟡/🔴/⚫), y RADAR sí.

## 7. Lo que hay que copiarles (además de lo de `RADAR-Competencia.md`)

1. **Temperatura propia = delta de anuncios activos** entre corridas diarias, con etiqueta
   (testando / escalando / escalado). Es la misma métrica, pero calculada sobre un dato que
   sabemos medir y sin confundirla con "ventas".
2. **Ordenar por crecimiento, no por volumen** — coincide con lo que ya decidimos.
3. **La esteira de testes** (kanban) como vista propia, con los links por tarjeta.
4. **Favoritos con colecciones** por nicho y por estacionalidad.
5. **Filtro por estacionalidad** (fecha de publicación: Pascua, Día del Niño) — un nicho de
   temporada es una oportunidad repetible.
6. **Anuncios relacionados = ideas de upsell** (ya está en la etapa PRODUCTO, pero sin datos).
7. **La frase del final, textual:** *no copiar los anuncios, entender la estructura y la promesa*.
   Es el mismo principio que ya está escrito en la skill.
