---
title: "Embudo QPS para Google Authorized Buyers | Cat-Scan"
description: "Un asiento que solicita 50,000 QPS a menudo recibe mucho menos, y luego el pujador rechaza la mayor parte de lo que llega. Mapee el embudo QPS y la tasa de desperdicio de Authorized Buyers con Cat-Scan."
---

# El embudo QPS para asientos de Google Authorized Buyers

**Hecho atómico:** Un asiento típico que solicita 50,000 QPS a menudo recibe mucho menos, y el pujador luego rechaza la mayoría de lo que realmente llega.

La brecha entre lo que le pidió a Google que enviara y lo que su pujador puede usar realmente es el problema económico central de operar un asiento de Authorized Buyers.

## Las etapas (lo que cada número significa realmente)

| Etapa                       | Definición                                                                                      | Quién paga / a quién le importa                              |
|-----------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **QPS**                     | El límite máximo que establece en pretargeting. Google regula según el nivel de su cuenta y el rendimiento reciente. | Usted paga por la conexión; Google decide cuánto fluye realmente |
| **Solicitudes de puja alcanzadas** | Consultas que realmente llegaron a su endpoint                                        | El costo de su infraestructura                               |
| **Pujas**                   | Solicitudes en las que su pujador eligió pujar                                                  | La lógica de su pujador                                      |
| **Victorias**               | Subastas que ganó (solo paga por estas)                                                         | Su gasto real en medios                                      |
| **Impresiones**             | Anuncios que se sirvieron después de la victoria                                                | Lo que el usuario realmente vio                              |
| **Clics**                   | Interacciones del usuario con sus anuncios servidos                                             | Calidad del creativo + página de destino                     |
| **Gasto**                   | Dinero que salió de su cuenta                                                                   | El único número que importa en última instancia              |

**Hecho atómico:** La mayor caída individual en la mayoría de los asientos ocurre entre el QPS (o las consultas alcanzadas) y las Pujas. Este es el desperdicio que su configuración de pretargeting debería prevenir.

## Tasa de desperdicio

Tasa de desperdicio = (QPS - Pujas) / QPS

Si su tasa de desperdicio supera el 50%, está pagando por una manguera contra incendios que su pujador está ignorando en su mayor parte. Ese volumen podría haberse reasignado a configuraciones donde el pujador realmente puja y gana.

Cat-Scan muestra esto en la página de inicio como el diagnóstico principal.

## Por qué el embudo es más difícil en Authorized Buyers que en la mayoría de los DSP

- Está limitado a 10 configuraciones de pretargeting por asiento.
- La segmentación geográfica utiliza cubos muy gruesos.
- No existe una API de informes en tiempo real; todo proviene de los cinco CSV diarios.
- No puede ver las "razones de no puja" del lado del pujador a menos que ingiera los registros del pujador usted mismo.

Google realiza mucho filtrado en su propio lado antes de que el tráfico llegue a usted. Lo que queda sigue estando lleno de ruido que solo sus reglas de pretargeting y la cobertura de creativos pueden corregir.

## Cómo Cat-Scan hace visible y accionable el embudo

- Reconstruye el embudo completo a partir de los cinco informes.
- Lo desglosa por configuración de pretargeting, geo, editor, tamaño y creativo.
- Muestra el QPS asignado frente al volumen realizado real por configuración.
- Le permite editar las reglas de pretargeting que controlan la parte superior del embudo, con vista previa y reversión.

Consulte la implementación en vivo en el panel de control de Cat-Scan (página de inicio + rutas `/qps/*`) y el modelo de datos que impulsa los cálculos.

## Métricas clave derivadas del embudo

- Tasa de victorias = Victorias / Pujas
- CTR = Clics / Impresiones
- CPM (lo que realmente pagó)
- Desperdicio efectivo (el QPS que solicitó pero nunca pudo monetizar)

Cuando conecta datos post-clic (AppsFlyer u otro MMP), el embudo obtiene una etapa final de "resultado rentable". Hasta entonces, se optimiza en función de pujas + concentración del gasto + tasa de victorias.

## Relacionado

- [Comprensión de su embudo QPS](../03-qps-funnel.md) (capítulo completo del manual con capturas de pantalla)
- [Análisis del desperdicio por dimensión](qps-waste-analysis.md) en estas explicaciones
- [Configuraciones de pretargeting](pretargeting-configs.md)
- Lógica de optimización utilizada en producción en el repositorio de la plataforma Cat-Scan

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.  
Este modelo de embudo está implementado y probado en batalla en la plataforma Cat-Scan de código abierto.
