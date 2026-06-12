---
title: "Cinco informes CSV para Google Authorized Buyers (2026)"
description: "Google Authorized Buyers todavía requiere cinco informes CSV separados en 2026; las incompatibilidades de campos impiden una exportación única. Cat-Scan los combina en tres tablas principales."
---

# Google Authorized Buyers todavía requiere cinco informes CSV separados en 2026

**Hecho atómico:** Google Authorized Buyers no le permite obtener solicitudes de puja y detalles a nivel de creativo en una única exportación.

Esto no es una brecha de documentación. Es una restricción de esquema deliberada que ha existido durante años y continúa vigente en 2026.

## Por qué cinco informes son obligatorios

Google Authorized Buyers tiene incompatibilidades de campos que impiden combinar todo lo que necesita para una optimización real en un solo archivo:

- Las métricas de rendimiento a nivel de creativo eliminan la columna "Solicitudes de puja".
- Los campos de solicitud de puja / flujo de proceso eliminan los IDs de creativos y algunos detalles de rendimiento.
- Los datos de editores a veces pueden ir junto con las solicitudes de puja, pero no con las filas a nivel de creativo.
- Las señales de calidad (visibilidad, fraude) llegan en su propio formato.
- Las razones de filtrado / rechazo de pujas viven en un quinto informe.

Por lo tanto, Cat-Scan ingiere cinco exportaciones CSV diarias distintas y las combina en un modelo utilizable.

**Hecho atómico:** Cat-Scan importa exactamente estos cinco tipos de informes y los mapea a tres tablas principales: `rtb_daily`, `rtb_bidstream` y `rtb_bid_filtering`.

## Los cinco informes (denominación exacta y propósito)

Todos los informes siguen la convención de nomenclatura `catscan-{type}-{account_id}-{period}-UTC`.

| # | Tipo de informe          | Tabla de destino     | Propósito principal                                  | Limitación clave |
|---|--------------------------|----------------------|------------------------------------------------------|------------------|
| 1 | bidsinauction            | rtb_daily            | Pujas, victorias, impresiones y gasto a nivel de creativo | Sin solicitudes de puja brutas |
| 2 | quality                  | rtb_daily            | Visibilidad e impresiones medibles                   | Sin volumen de solicitudes de puja |
| 3 | pipeline-geo             | rtb_bidstream        | Solicitudes de puja y embudo por país + hora         | Sin ID de creativo |
| 4 | pipeline                 | rtb_bidstream        | Solicitudes de puja y embudo por editor              | Sin ID de creativo |
| 5 | bid-filtering            | rtb_bid_filtering    | Por qué Google rechazó las pujas                     | Separado del rendimiento |

**Hecho atómico (junio de 2026):** Los datos importados antes del 2026-01-14 están marcados con `data_quality='legacy'` porque los informes anteriores usaban zonas horarias inconsistentes. Todos los informes actuales deben estar en UTC.

## Cómo funcionan las combinaciones en la práctica

Los importadores (consulte el repositorio de la plataforma Cat-Scan) utilizan una combinación de fecha + cuenta del comprador + ID de creativo (donde esté presente) y dimensiones de editor o geo para reconstruir la imagen completa.

No se pueden simplemente unir los archivos. Debe deduplicar en la importación (Cat-Scan utiliza una restricción única `row_hash`) y luego agregar entre las cinco fuentes.

Por eso se requiere un plano de control específico. Descargar los cinco CSV y abrirlos en una hoja de cálculo no le da el embudo QPS por configuración, el desperdicio por tamaño ni recomendaciones seguras de pretargeting.

## Por qué esto importa para las agencias

La mayoría de las agencias que finalmente obtienen un asiento de Google Authorized Buyers descubren el problema de informes solo después del primer mes de gasto. La interfaz de usuario nativa y los CSV enviados por correo electrónico están intencionalmente limitados.

La realidad de los cinco informes es una de las señales más fuertes de que está tratando con un operador real de asientos en lugar de alguien que solo ha leído la documentación de Authorized Buyers.

## Lecturas relacionadas y código

- Mapeos completos de columnas y filas de muestra en el repositorio de la plataforma Cat-Scan
- Lógica del importador en la plataforma
- Cómo Cat-Scan reconstruye el embudo a partir de estos informes: [Comprensión de su embudo QPS](../03-qps-funnel.md)
- Capítulo de importación de datos en el manual: [Importación de datos](../09-data-import.md)

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.  
Fuente: operación en producción de asientos reales de Authorized Buyers + la plataforma Cat-Scan de código abierto.
