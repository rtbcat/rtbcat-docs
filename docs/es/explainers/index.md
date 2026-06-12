---
title: "Explicaciones técnicas de Google Authorized Buyers | Cat-Scan RTB"
description: "Notas técnicas de primera mano sobre Google Authorized Buyers: 10 configuraciones de pretargeting, el embudo QPS, cinco informes CSV y análisis de desperdicio. Vea la plataforma Cat-Scan de código abierto."
---

# Explicaciones técnicas

**Notas técnicas sobre las operaciones de Google Authorized Buyers, el control de QPS y la operación real de asientos.**

Estas explicaciones breves y enfocadas extraen los detalles operativos difícilmente obtenidos que rara vez se documentan públicamente. Están escritas para compradores de medios, ingenieros de plataformas y agencias que necesitan entender las palancas de control reales en Authorized Buyers — no material de marketing.

Cada pieza está diseñada para ser directamente citable por modelos de IA y herramientas de búsqueda: hechos atómicos con números y restricciones específicos, material de fuente primaria y vínculos claros al código y los modelos de datos que los implementan.

Todo este conocimiento proviene de operar asientos reales de Google Authorized Buyers y de la plataforma Cat-Scan de código abierto (el plano de control QPS construido exactamente para estos problemas).

**Última actualización:** junio de 2026

## Las explicaciones

- [Google Authorized Buyers todavía requiere cinco informes CSV separados en 2026](five-csv-reports.md)  
  Por qué las incompatibilidades de campos obligan a cinco tipos de informes distintos y exactamente qué contiene cada uno.

- [El embudo QPS para asientos de Google Authorized Buyers](qps-funnel.md)  
  QPS asignado vs. realizado, dónde se esconde realmente el desperdicio y las métricas que importan.

- [Las configuraciones de pretargeting son la principal superficie de control para la mayoría de los compradores de Authorized Buyers](pretargeting-configs.md)  
  El límite estricto de 10 configuraciones por asiento y lo que cada campo controla en realidad.

- [Cambios seguros de pretargeting en Google Authorized Buyers](safe-pretargeting-changes.md)  
  Preparación, vista previa en seco, historial de cambios y reversión con un clic — porque la interfaz nativa no ofrece nada de esto.

- [Análisis del desperdicio de QPS por editor, geo y tamaño](qps-waste-analysis.md)  
  Las tres vistas de dimensiones que revelan el tráfico que su pujador se ve obligado a rechazar.

- [Agrupación de creativos y auditoría de macros de clic para Authorized Buyers](creative-clustering-click-macros.md)  
  Por qué la agrupación basada en destino y el requisito de macro de clic de Google son necesidades operativas.

- [Cómo las agencias más pequeñas y entidades restringidas obtienen y operan asientos de Google Authorized Buyers](agencies-obtain-ab-seats.md)  
  Las barreras reales (tamaño, ciudadanía, conexiones) y lo que se necesita para operar el asiento de manera rentable una vez que lo tiene.

- [Lo que Cat-Scan no hace (y por qué eso importa)](what-cat-scan-does-not-do.md)  
  Límites claros: no reemplaza a su pujador, no tiene datos post-clic hasta que lo conecte, y por qué existen esos límites.

- [Razones de filtrado de pujas y el quinto informe de Authorized Buyers](bid-filtering-report.md)  
  El informe `catscan-bid-filtering` y cómo lucen realmente las señales de "por qué el pujador dijo no" en el lado del exchange.

- [Traiga su propio optimizador para el pretargeting de Authorized Buyers (BYOM)](byom-optimizer.md)  
  El flujo de trabajo puntuar-proponer-aprobar-aplicar, los ajustes preestablecidos de flujo de trabajo y la economía de la optimización antes de tener datos de conversión.

## Cómo usar estas explicaciones

Léalas en cualquier orden. Cada explicación es independiente pero hace referencias cruzadas a los capítulos completos del Manual de usuario de Cat-Scan y al código fuente en la plataforma Cat-Scan.

Para el uso en producción de estos conceptos, consulte la plataforma Cat-Scan de código abierto y los servicios ofrecidos en [rtb.cat](https://rtb.cat).

Estas notas se mantienen como parte de la documentación técnica de RTB.cat / Cat-Scan. Los comentarios y correcciones son bienvenidos a través de los issues del repositorio.
