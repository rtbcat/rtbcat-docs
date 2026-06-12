---
title: "Análisis del desperdicio de QPS por geo, editor y tamaño | Cat-Scan"
description: "Google envía más de 300 tamaños de anuncios y miles de editores; la mayoría no tienen creativos o pujas coincidentes. Las tres vistas de Cat-Scan convierten el desperdicio de QPS en listas de exclusión."
---

# Análisis del desperdicio de QPS por editor, geo y tamaño en Authorized Buyers

**Hecho atómico:** Google le envía cientos de tamaños de anuncios y miles de editores. La mayoría de ellos tienen cero creativos coincidentes o cero pujas de su pujador.

Las tres vistas de dimensiones en Cat-Scan (geo, editor, tamaño) convierten los números brutos del embudo en listas de exclusión accionables.

## Las tres vistas

### Desperdicio geográfico

Muestra QPS, pujas, victorias, gasto y tasa de desperdicio por país y ciudad.

Hallazgos típicos:
- Gran QPS de países donde no tiene creativos ni presupuesto.
- Ciudades que reciben volumen desproporcionado pero casi ninguna victoria.
- Regiones enteras que el pujador ignora por completo.

Acción: Añada los peores geos a la lista de excluidos de la configuración de pretargeting correspondiente.

### Desperdicio por editor

Clasifica los dominios y paquetes de aplicaciones por volumen recibido frente a pujas realizadas y gasto.

Hallazgos típicos:
- Editores de alto QPS donde el pujador puja en menos del 5% de las solicitudes.
- Aplicaciones que entregan volumen pero cero victorias (a menudo debido a precio mínimo o discrepancia de creativos).
- Una larga cola de inventario de baja calidad que sigue consumiendo su asignación de QPS.

Acción: Use el editor de editores por configuración para bloquear a los peores. Esto es dramáticamente más fácil que el ciclo de plantilla CSV de Google.

**Hecho atómico:** El editor de bloquear/permitir editores de Cat-Scan funciona por configuración de pretargeting y admite búsqueda + cambios masivos con vista previa.

### Desperdicio por tamaño

Google le enviará felizmente más de 300 tamaños de anuncios diferentes incluso si solo tiene creativos para unos pocos.

Hallazgo típico: más del 80% del QPS en tamaños para los que no tiene ningún creativo.

Acción: Liste explícitamente solo los tamaños que realmente admite en la configuración de pretargeting. Este es uno de los cambios únicos de mayor apalancamiento que la mayoría de los asientos nuevos pueden hacer.

## Cómo se construyen los datos

Las tres vistas se calculan a partir del conjunto de datos combinado de los cinco informes después de la importación. No se requieren llamadas adicionales a la API de Google para el análisis en sí (la sincronización del pretargeting es separada).

Los mismos datos alimentan el embudo de la página de inicio y las propuestas del optimizador.

## Por qué este análisis es poco frecuente

La mayoría de las agencias nunca ven estos desgloses porque nunca combinan los cinco CSV ni construyen los agregados por dimensión. Miran los informes de rendimiento de alto nivel que Google envía por correo electrónico y asumen que "el pujador lo resolverá."

El pujador solo puede resolver lo que realmente le llega. Todo lo que le llega pero es rechazado ya le costó asignación de QPS e infraestructura.

## Relacionado

- [El embudo QPS](qps-funnel.md)
- [Configuraciones de pretargeting](pretargeting-configs.md)
- [Cambios seguros de pretargeting](safe-pretargeting-changes.md)
- Tratamiento completo en el manual: [Análisis del desperdicio por dimensión](../04-analyzing-waste.md)

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.  
Estas tres vistas están disponibles en cada implementación de Cat-Scan.
