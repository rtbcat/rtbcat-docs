---
title: "Informes CSV de Authorized Buyers: 5 que Cat-Scan necesita"
description: "Google Authorized Buyers no tiene una API de informes, por lo que Cat-Scan reconstruye el embudo a partir de cinco informes CSV programados. Referencia completa de métricas y dimensiones más configuración."
---

# Configuración de sus informes CSV

*Audiencia: compradores de medios, gestores de cuentas*

Antes de que Cat-Scan pueda analizar nada, necesita datos. Google Authorized Buyers
no tiene una API de informes, por lo que todos los datos fluyen a través de **cinco informes CSV programados**
que crea una vez en su cuenta de Google AB.

!!! warning "¿Por qué cinco informes separados?"
    Las columnas de informes de Google no son todas compatibles entre sí. Por
    ejemplo, "Solicitudes de puja" no puede aparecer en el mismo informe que "ID de aplicación móvil"
    o "ID de creativo + ID de facturación". Para obtener visibilidad completa del embudo, necesita cinco
    informes que Cat-Scan combina automáticamente.

## Los cinco informes de un vistazo

| # | Nombre del informe | Qué le dice a Cat-Scan | Columnas clave |
|---|-------------------|------------------------|----------------|
| 1 | **Quality** | Rendimiento a nivel de creativo con visibilidad | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Canal de pujas a nivel de creativo (pujas -> victorias) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Embudo completo del flujo de pujas por país | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Embudo completo del flujo de pujas por editor | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Por qué Google está rechazando sus pujas | Filtering reason, Bids, Opportunity cost |

---

## Referencia completa de métricas

Cada métrica que Cat-Scan ingiere, qué significa y qué informe la proporciona.

### Métricas del embudo (canal del flujo de pujas)

Estas rastrean la progresión de una solicitud de puja a través del sistema de subastas de Google.
Presentes en los informes **Pipeline -- Geo** y **Pipeline -- Publisher**.

| Métrica | Definición | Unidad | Informe(s) |
|---------|-----------|--------|-----------|
| **Bid requests** | Total de solicitudes de puja que Google envió a su endpoint de pujador. Este es el volumen de entrada bruto — la parte superior del embudo. Incluye solicitudes a las que su pujador puede no haber respondido a tiempo. | recuento | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Solicitudes de puja que realmente llegaron a su pujador y obtuvieron una respuesta (exitosa o no). Menor que "Bid requests" si su pujador tiene problemas de latencia o tiempos de espera agotados. | recuento | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Solicitudes donde su pujador encontró inventario coincidente (un creativo que se ajusta a la solicitud). Este es el primer filtro: si no tiene creativo para el tamaño/formato solicitado, se detiene aquí. | recuento | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Solicitudes donde su pujador devolvió una respuesta de puja válida y analizable (HTTP 200 con una puja bien formada). Excluye tiempos de espera agotados, errores y respuestas sin puja. | recuento | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Respuestas de puja reales que realizó su pujador. Un subconjunto de respuestas exitosas — su pujador puede responder exitosamente pero optar por no pujar (respuesta sin puja). | recuento | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Pujas que Google aceptó en la subasta. Las pujas pueden ser rechazadas antes de entrar a la subasta debido a reglas de filtrado (desaprobación de creativos, violaciones de políticas, precio mínimo, exclusiones de pretargeting). La brecha entre "Bids" y "Bids in auction" se muestra en el informe Bid Filtering. | recuento | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Pujas que ganaron la subasta. Usted paga por estas. La brecha entre "Bids in auction" y "Auctions won" es competencia — otros compradores lo superaron en la puja. | recuento | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Anuncios que se representaron realmente en el navegador o aplicación de un usuario después de ganar la subasta. Ligeramente menos que "Auctions won" debido a fallos de representación del anuncio, navegaciones de página antes de la representación e interferencia del bloqueador de anuncios. | recuento | Los cinco informes |
| **Clicks** | Interacciones del usuario (toques/clics) en sus anuncios servidos. | recuento | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Métricas de gasto y costo

| Métrica | Definición | Unidad | Informe(s) |
|---------|-----------|--------|-----------|
| **Spend** | Dinero total gastado en impresiones ganadas para el período. Este es su costo real de medios. Denominado en la moneda de su cuenta (generalmente USD). | moneda (micros en datos sin procesar, dólares en la interfaz) | Quality |
| **Opportunity cost** | Ingresos estimados que perdió porque Google filtró sus pujas antes de que entraran a la subasta. Calculado por Google en función de las tasas de victorias históricas y los CPM para inventario similar. Útil para priorizar qué razones de filtrado corregir primero. | moneda | Bid Filtering |

### Métricas de calidad y visibilidad

Estas son métricas a nivel de creativo del informe **Quality**. Miden
lo que sucede *después* de que se sirve la impresión.

| Métrica | Definición | Unidad | Informe(s) |
|---------|-----------|--------|-----------|
| **Active View viewable** | Impresiones que cumplieron el estándar de visibilidad MRC: al menos el 50% de los píxeles del anuncio estaban en el área visible del navegador durante al menos 1 segundo continuo (2 segundos para video). Este es el estándar de la industria para "¿fue realmente visto este anuncio?" | recuento | Quality |
| **Active View measurable** | Impresiones donde la visibilidad *podía* medirse. Algunos entornos (ciertas aplicaciones, iframes de dominio cruzado, navegadores más antiguos) bloquean la medición. Tasa de visibilidad = Active View viewable / Active View measurable. | recuento | Quality |
| **Video starts** | Número de veces que un creativo de video comenzó a reproducirse. Solo se completa para creativos en formato de video. | recuento | Quality |
| **Video completions** | Número de veces que un creativo de video se reprodujo hasta el 100% de finalización (o hasta el punto de saltar si es omitible). Tasa de finalización de video = completions / starts. | recuento | Quality |

### Métricas de filtrado de pujas

Del informe **Bid Filtering**. Estas le dicen *por qué* se están rechazando
las pujas antes de entrar a la subasta.

| Métrica | Definición | Unidad | Informe(s) |
|---------|-----------|--------|-----------|
| **Bids** | Total de pujas que realizó su pujador (misma definición que la anterior). En este informe, se usa como denominador para calcular las tasas de filtrado. | recuento | Bid Filtering |
| **Bids in auction** | Pujas que sobrevivieron al filtrado y entraron a la subasta. `Bids - Bids in auction` = total de pujas filtradas. | recuento | Bid Filtering |
| **Opportunity cost** | Consulte las métricas de gasto anteriores. En este informe, desglosado por razón de filtrado para que pueda ver qué razón le cuesta más. | moneda | Bid Filtering |

### Dimensiones (columnas de agrupación)

Las dimensiones no son métricas — son los ejes a lo largo de los cuales se desglosan las métricas.
Cat-Scan las usa para segmentar sus datos.

| Dimensión | Qué es | Qué informes |
|-----------|--------|--------------|
| **Day** | Fecha calendario (UTC). Requerida en todos los informes. Cat-Scan la usa para deduplicación y visualización de series temporales. | Los cinco |
| **Hour** | Hora del día (0--23, UTC). Permite granularidad horaria en el análisis del canal. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Código de país ISO de dos letras (p. ej., US, DE, IL). El origen geográfico de la solicitud de puja. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (opcional) |
| **Billing ID (Pretargeting config)** | ID numérico de la configuración de pretargeting que aceptó este tráfico. Se mapea 1:1 a una tarjeta de configuración en Cat-Scan. | Quality |
| **Creative ID** | ID numérico de Google para el activo creativo. Vincula a la galería de Creativos en Cat-Scan. | Quality, Bids in Auction, Bid Filtering (opcional) |
| **Creative size** | Dimensiones en píxeles del creativo (p. ej., `300x250`, `728x90`). Se usa para el análisis de desperdicio basado en tamaño. | Quality |
| **Creative format** | El formato del anuncio: `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (opcional) |
| **Platform** | Plataforma del dispositivo: `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (opcional) |
| **Environment** | Dónde se sirvió el anuncio: `WEB`, `APP`. | Quality (opcional) |
| **App ID** | ID de paquete de la aplicación móvil (p. ej., `com.example.app`). Solo se completa para inventario en aplicación. | Quality (opcional) |
| **App name** | Nombre de la aplicación legible por humanos. | Quality (opcional) |
| **Publisher ID** | ID numérico del editor (sitio web o aplicación). | Quality (opcional), Pipeline -- Publisher |
| **Publisher name** | Nombre del editor legible por humanos. | Quality (opcional), Pipeline -- Publisher |
| **Publisher domain** | El dominio del sitio web del editor (p. ej., `news.example.com`). | Quality (opcional) |
| **Buyer account ID** | Su ID de cuenta de comprador / asiento. Necesario cuando opera múltiples asientos. | Bids in Auction, Bid Filtering (opcional) |
| **Filtering reason** | El código de razón de Google por qué se filtró una puja antes de entrar a la subasta (p. ej., `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Paso a paso: creación de cada informe

### 1. Informe Quality

Este es su informe de rendimiento a nivel de creativo con datos de visibilidad y gasto.

**En Google Authorized Buyers -> Reporting -> New Report:**

| Configuración | Valor |
|---------------|-------|
| Report type | RTB |
| Time range | Yesterday (programado diariamente) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Optional dimensions | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Metrics | Reached queries, Impressions, Clicks, Spend |
| Optional metrics | Video starts, Video completions, Active View viewable, Active View measurable |

**Nombre de archivo sugerido:** `catscan-quality`

!!! note
    Este informe **no debe** incluir "Bid requests", "Bids" o "Bids in
    auction" — esas columnas son incompatibles con "Billing ID" en los informes de Google.

---

### 2. Informe Bids in Auction

Este informe captura el canal de pujas a nivel de creativo, completando las
métricas que el informe Quality no puede incluir.

| Configuración | Valor |
|---------------|-------|
| Report type | RTB |
| Time range | Yesterday (programado diariamente) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Metrics | Bids in auction, Auctions won, Bids, Impressions |

**Nombre de archivo sugerido:** `catscan-bidsinauction`

!!! info "Cómo Cat-Scan los combina"
    Quality + Bids in Auction se combinan en `(Day, Creative ID)` para darle
    la imagen completa: desde las pujas realizadas hasta las impresiones servidas y el gasto incurrido.

---

### 3. Informe Pipeline -- Geo

Este es su informe de la parte superior del embudo: cuántas solicitudes de puja le envía Google
por país y cuántas sobreviven a cada etapa del embudo.

| Configuración | Valor |
|---------------|-------|
| Report type | RTB |
| Time range | Yesterday (programado diariamente) |
| Dimensions | Day, Country, Hour |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Nombre de archivo sugerido:** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **No** añada Creative ID, Billing ID ni App ID a este informe. Estas
    columnas son incompatibles con "Bid requests".

---

### 4. Informe Pipeline -- Publisher

Igual que Pipeline -- Geo, pero desglosado por editor en lugar de (o además de) la geografía.

| Configuración | Valor |
|---------------|-------|
| Report type | RTB |
| Time range | Yesterday (programado diariamente) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Metrics | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Nombre de archivo sugerido:** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Informe Bid Filtering

Este informe le muestra *por qué* Google está filtrando sus pujas antes de que entren a la
subasta — fundamental para diagnosticar problemas de pretargeting.

| Configuración | Valor |
|---------------|-------|
| Report type | RTB |
| Time range | Yesterday (programado diariamente) |
| Dimensions | Day, Filtering reason |
| Optional dimensions | Country, Buyer account ID, Creative ID |
| Metrics | Bids, Bids in auction, Opportunity cost |

**Nombre de archivo sugerido:** `catscan-bid-filtering`

### Razones de filtrado comunes

Estos son los valores que verá en la dimensión **Filtering reason**. Cada
uno le dice una razón específica por la que Google rechazó su puja antes de entrar a la subasta.

| Razón de filtrado | Qué significa | Qué hacer |
|-------------------|--------------|-----------|
| `CREATIVE_NOT_APPROVED` | El creativo no ha pasado la revisión de Google, o fue desaprobado | Verifique el estado del creativo en Google AB. Corrija las violaciones de políticas. |
| `BID_BELOW_AUCTION_FLOOR` | El precio de su puja estaba por debajo del CPM mínimo del editor | Aumente la puja o excluya inventario de bajo valor mediante pretargeting |
| `DISAPPROVED_BY_EXCHANGE` | La política a nivel de exchange de Google bloqueó la puja | Revise las políticas de anuncios de Google para el creativo específico |
| `FILTERED_BY_PRETARGETING` | Sus propias reglas de pretargeting excluyeron este tráfico | Intencional si sus reglas son correctas; revise si es inesperado |
| `NO_MATCHING_CREATIVE` | La solicitud de puja pedía un tamaño/formato que no tiene | Cargue creativos para los tamaños faltantes, o excluya esos tamaños en el pretargeting |
| `CREATIVE_SIZE_MISMATCH` | Las dimensiones del creativo no coinciden con el espacio publicitario | Verifique el tamaño del creativo frente a lo que solicita el editor |
| `LANDING_PAGE_DISAPPROVED` | La URL de destino no pasó la revisión de Google | Corrija la página de destino o use una URL diferente |
| `SSL_REQUIRED` | El editor requiere HTTPS pero su creativo o página de destino usa HTTP | Cambie todos los activos y URLs a HTTPS |
| `FREQUENCY_CAPPED` | El usuario ya ha visto este creativo demasiadas veces | Comportamiento esperado; ajuste los límites de frecuencia si son demasiado agresivos |

---

## Programación de la entrega

Para cada uno de los cinco informes:

1. Haga clic en **Schedule** en Google Authorized Buyers.
2. Establezca la frecuencia en **Daily**.
3. Establezca el método de entrega:
      - **Email** — envíe a la cuenta de Gmail conectada a Cat-Scan (habilita la
        importación automática). Consulte [Importación de datos](09-data-import.md) para la
        configuración de importación automática de Gmail.
      - **Manual** — si prefiere descargar y cargar los CSV usted mismo mediante
        `/import`.

!!! tip "Use la importación automática de Gmail"
    Programar los cinco informes para enviarlos por correo electrónico a una cuenta de Gmail conectada significa
    que Cat-Scan los importa automáticamente cada día. No se necesitan cargas manuales
    después de la configuración inicial.

## Verificación de su configuración

Después de importar su primer conjunto de CSV (manualmente o mediante Gmail):

1. Vaya a `/import` en Cat-Scan.
2. Verifique la **cuadrícula de frescura de datos** — debería ver "imported" para los cinco
   tipos de informe de la fecha de ayer.
3. Si alguna celda muestra "missing", el informe correspondiente aún no se ha recibido.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Una vez que las cinco columnas muestran verde para ayer, Cat-Scan tiene datos completos y
todas las funciones (embudo, análisis de desperdicio, recomendaciones, optimizador) funcionarán.

## Detección automática

No necesita decirle a Cat-Scan qué informe está cargando. El sistema de importación
detecta el tipo de informe automáticamente a partir de los encabezados de columna:

- ¿Tiene **Bid filtering reason**? -> Bid Filtering
- ¿Tiene **Bid requests** + **Publisher ID**? -> Pipeline -- Publisher
- ¿Tiene **Bid requests** (sin Publisher ID)? -> Pipeline -- Geo
- ¿Tiene **Creative ID** + **Billing ID**? -> Quality
- ¿Tiene **Creative ID** + **Bids in auction**? -> Bids in Auction

## Cómo Cat-Scan usa cada métrica

Esto mapea las métricas de CSV sin procesar a lo que ve en la interfaz de usuario de Cat-Scan.

| Función de la interfaz | Métricas usadas | Informe(s) fuente |
|-----------------------|----------------|-------------------|
| **Embudo QPS** (página de inicio) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (ambos) + Quality |
| **Cálculo del % de desperdicio** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Tasa de victorias** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Cualquier informe con ambos |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Tasa de visibilidad** | `Active View viewable / Active View measurable` | Quality |
| **Tasa de finalización de video** | `Video completions / Video starts` | Quality |
| **Análisis de desperdicio geo** (`/qps/geo`) | Bid requests, Impressions, Spend por Country | Pipeline -- Geo + Quality |
| **Desperdicio por editor** (`/qps/publisher`) | Bid requests, Impressions, Spend por Publisher | Pipeline -- Publisher + Quality |
| **Desperdicio por tamaño** (`/qps/size`) | Impressions, Spend por Creative size | Quality |
| **Razones de filtrado** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost por Filtering reason | Bid Filtering |
| **Métricas de tarjeta de configuración** | Reached queries, Impressions, Spend por Billing ID | Quality |
| **Rendimiento de creativos** | Impressions, Clicks, Spend, Active View viewable por Creative ID | Quality |
| **Puntuación del optimizador** | Todas las métricas de pipeline + quality, agregadas por segmento | Los cinco |

## Errores comunes

| Error | Qué sucede | Solución |
|-------|-----------|---------|
| Añadir "Bid requests" al informe Quality | Google devuelve errores o datos incompletos | Elimine "Bid requests" — es incompatible con "Billing ID" |
| Olvidar el informe Bid Filtering | Cat-Scan no puede mostrarle *por qué* se rechazan las pujas | Cree el 5.° informe con la dimensión "Filtering reason" |
| Usar "Last 7 days" en vez de "Yesterday" | Datos superpuestos, archivos más grandes, importaciones más lentas | Configure en "Yesterday" y programe diariamente |
| No programar — solo exportaciones manuales | Los datos se vuelven obsoletos, fallan las verificaciones de salud | Programe la entrega diaria por correo electrónico |
| Falta la dimensión "Hour" en los informes Pipeline | Sin granularidad horaria en el análisis de QPS | Añada Hour a Pipeline -- Geo y Pipeline -- Publisher |
| Faltan métricas opcionales en el informe Quality | Sin datos de visibilidad o video en Cat-Scan | Añada Active View viewable, Active View measurable, Video starts, Video completions |

## Próximos pasos

- [Navegación de administración](02-navigating-the-dashboard.md): diseño de la barra lateral y
  lista de verificación de configuración
- [Importación de datos](09-data-import.md): mecánicas detalladas de importación, cargas
  fragmentadas y solución de problemas
- [Embudo QPS](03-qps-funnel.md): una vez que los datos estén fluyendo, comience a analizar
