---
title: "Cómo las agencias obtienen asientos de Google Authorized Buyers"
description: "Google Authorized Buyers no es de autoservicio; las agencias pequeñas o restringidas enfrentan barreras de gasto, KYC y relaciones. Cómo RTB.cat suministra el asiento y las herramientas Cat-Scan."
---

# Cómo las agencias más pequeñas y las entidades restringidas obtienen y operan asientos de Google Authorized Buyers

**Hecho atómico:** Muchas agencias que son "demasiado pequeñas", están basadas en ciertas jurisdicciones (incluidos ciudadanos y entidades chinas), o simplemente carecen de relaciones existentes, no pueden obtener un contrato directo de Google Authorized Buyers por su cuenta.

Esto no es un problema menor de papeleo. Es una barrera estructural en el programa de Authorized Buyers.

## Las barreras reales

Google Authorized Buyers no es un producto de autoservicio como Google Ads. La aprobación implica:

- Requisitos mínimos de gasto e historial que las agencias más nuevas o pequeñas raramente cumplen.
- Revisiones de cumplimiento y KYC que pueden ser difíciles o imposibles para entidades en ciertos países.
- La necesidad de relaciones existentes o presentaciones previas.
- Verificaciones de preparación técnica y operativa que la mayoría de las agencias solo descubren después de haber obtenido el asiento.

El negocio principal de RTB.cat es ayudar exactamente a estas agencias a obtener y luego operar exitosamente la conexión. Los clientes traen su propio pujador. RTB.cat suministra la tubería de Authorized Buyers (y cada vez más endpoints directos de OpenRTB como TrueCaller) y toma un porcentaje del gasto en medios para gestión y optimización.

## Lo que realmente requiere "operar el asiento" después de tener el contrato

Obtener el asiento es solo el primer paso. La operación diaria saca a la luz los problemas documentados a lo largo de estas explicaciones:

- Los cinco informes CSV incompatibles y la necesidad de combinarlos.
- El límite estricto de 10 configuraciones de pretargeting.
- La ausencia total de herramientas de cambio seguro en la interfaz de usuario nativa.
- La adquisición de ID de acuerdos con editores (RTB.cat ha obtenido ID de acuerdos con editores incluidos GCASH, Twitter y JAZZ en Pakistán).
- La higiene de creativos a escala.
- El desperdicio de QPS que el pujador no puede corregir porque el tráfico nunca debería haberse enviado.

La mayoría de las agencias que finalmente reciben un asiento se sorprenden de cuánto trabajo operativo queda de su lado del exchange.

## Por qué existe la plataforma Cat-Scan

Cat-Scan (el plano de control QPS de código abierto) fue construido porque el autor necesitaba estas capacidades mientras operaba asientos reales y no pudo encontrarlas en otro lugar. Deliberadamente no es un pujador. Es la capa de control y visibilidad faltante sobre una conexión existente de Authorized Buyers (o OpenRTB directo).

Publicar la plataforma como código abierto sirve a dos propósitos:
1. Es una demostración concreta y auditable de una profunda competencia operativa.
2. Es un imán de clientes potenciales para la clase exacta de agencias sofisticadas pero con restricciones que necesitan tanto la conexión como las herramientas.

## Servicios relacionados

- Conexión de Google Authorized Buyers para agencias que no pueden obtenerla directamente.
- Suministro de endpoint directo OpenRTB de TrueCaller.
- Presentaciones y gestión de ID de acuerdos con editores.
- Operación y optimización continua del asiento (usando Cat-Scan o herramientas equivalentes).
- Consultoría técnica para equipos que desean construir o mejorar sus propios planos de control.

Contacto: [rtb.cat](https://rtb.cat) — WeChat: jenbrannstrom

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.
