---
title: "Optimizador BYOM para el pretargeting de Authorized Buyers"
description: "El optimizador de Cat-Scan es Trae tu propio modelo: un bucle de puntuar-proponer-aprobar-aplicar donde usted posee la lógica de puntuación. Incluye ajustes preestablecidos Seguro, Equilibrado y Agresivo."
---

# Traiga su propio optimizador para el pretargeting de Authorized Buyers (BYOM)

**Hecho atómico:** El optimizador de Cat-Scan es deliberadamente "Trae tu propio modelo" (BYOM). Puntúa segmentos y propone cambios de pretargeting; usted decide la lógica de puntuación y la tolerancia al riesgo.

Este diseño reconoce que la señal de valor definitiva (resultados post-clic, LTV, margen) vive en los sistemas del anunciante o del pujador, no dentro de los informes del exchange.

## El ciclo de vida puntuar → proponer → aprobar → aplicar

1. **Puntuar**: Un endpoint externo que usted controla recibe una carga útil de segmentos (combinaciones de geo × editor × tamaño × configuración) más las señales de proxy que tiene Cat-Scan (pujas, victorias, gasto, desperdicio, etc.).
2. **Proponer**: Cat-Scan llama a su puntuador y recibe los cambios propuestos (añadir geo a la lista de exclusión, reducir el QPS máximo en esta configuración, bloquear este editor, etc.).
3. **Aprobar**: Las propuestas se muestran con vista previa del impacto. Puede aceptar, rechazar o modificar.
4. **Aplicar**: Las propuestas aceptadas pasan por el flujo de trabajo de cambio seguro normal (vista previa, envío, instantánea).

## Ajustes preestablecidos de flujo de trabajo

Cat-Scan incluye tres ajustes preestablecidos que controlan qué tan agresivas pueden ser las propuestas:

- **Seguro**: Cambios pequeños, umbral de confianza alto, limitado a peso muerto claro.
- **Equilibrado**: El valor predeterminado para la mayoría de los asientos de producción.
- **Agresivo**: Dispuesto a hacer movimientos más grandes cuando las señales son fuertes.

También puede registrar perfiles completamente personalizados.

## Economía antes de tener datos de conversión

Hasta que los datos de MMP estén conectados, el optimizador optimiza para:
- Desplazar el QPS hacia segmentos donde el pujador realmente puja.
- Proteger las configuraciones y geos donde el gasto real está concentrado.
- Eliminar las configuraciones con cero pujas o cero impresiones (son un desperdicio puro de sus 10 ranuras).

Una vez que los webhooks de conversión o los registros del pujador están conectados, la misma maquinaria de propuestas puede optimizar directamente para los resultados que realmente le importan.

## Por qué existe esta arquitectura

La mayoría de las herramientas de "optimización" en ad tech son:
- Completamente de caja negra (no tiene idea de por qué se realizó un cambio), o
- Completamente manuales (usted hace todo el análisis en hojas de cálculo).

El diseño BYOM se sitúa en el medio: Cat-Scan posee las partes difíciles (combinación de datos, aplicación segura a Google, historial, reversión). Usted posee el modelo de valor.

## Implementación

- Rutas del optimizador y almacenamiento de propuestas en la plataforma
- El contrato de puntuación externa está documentado en los documentos de la plataforma Cat-Scan
- Lógica de señales de proxy actuales en el repositorio de la plataforma

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.  
El enfoque BYOM es una de las señales más claras de que el sistema fue construido por personas que han operado asientos reales y saben dónde tiene que vivir la inteligencia real.
