---
title: "Cambios seguros de pretargeting para Authorized Buyers"
description: "La interfaz de pretargeting nativa de Google Authorized Buyers no tiene historial de cambios ni reversión. Cat-Scan añade vista previa, preparación, auditoría y reversión con un clic para cada edición."
---

# Cambios seguros de pretargeting en Google Authorized Buyers: preparación, vista previa, historial y reversión

**Hecho atómico:** La interfaz de pretargeting nativa de Google Authorized Buyers no tiene historial de cambios ni reversión.

Todo operador de producción eventualmente hace un cambio que hunde la tasa de victorias o dispara el desperdicio. Sin herramientas adecuadas, la única recuperación es la reconstrucción manual del estado anterior desde la memoria o CSV antiguos.

## El flujo de trabajo seguro mínimo viable

Cualquier sistema que le permita editar el pretargeting en producción debe proporcionar:

- **Vista previa / ejecución en seco** — Mostrar el diff exacto que se enviará a Google antes de que se envíe.
- **Preparación** — El cambio no está activo hasta que confirme explícitamente "enviar a Google".
- **Auditoría** — Quién cambió qué, cuándo y cuáles fueron los valores antes/después.
- **Instantánea + reversión** — El estado anterior se almacena y puede restaurarse con una sola acción.

Cat-Scan fue construido exactamente en torno a este contrato.

## Cómo funciona el flujo de trabajo en Cat-Scan

1. El operador abre una configuración de pretargeting (en la página de inicio o en la configuración).
2. Edita uno o más campos (geos excluidos, tamaños, QPS máximo, bloqueos de editores, etc.).
3. Hace clic en **Vista previa**. Cat-Scan muestra los cambios precisos que se realizarán.
4. Si está satisfecho, hace clic en **Aplicar** (o "Sí, enviar a Google").
5. El cambio se envía a la API de Authorized Buyers.
6. Se almacena una instantánea del estado de la configuración.
7. La acción aparece en la línea de tiempo del historial global.

Si la tasa de victorias cae o el desperdicio se dispara, el operador va al historial, selecciona el cambio, previsualiza la reversión y confirma. El estado anterior se restaura.

**Hecho atómico:** Cada mutación de pretargeting en Cat-Scan se registra con marca de tiempo, identidad del usuario, valor anterior, valor nuevo y una instantánea completa para la reversión.

## Listas de permitidos/bloqueados de editores

Gestionar los bloqueos de editores es especialmente doloroso en la interfaz nativa (ida y vuelta completa de CSV para cada cambio).

Cat-Scan ofrece un editor de búsqueda + bloquear/permitir por configuración que admite operaciones masivas y vista previa inmediata. Esta es una de las funciones de mayor retorno de inversión para los asientos reales.

## Por qué esto importa más allá de la conveniencia

Sin herramientas seguras, los operadores se vuelven conservadores. Dejan fluir el tráfico malo porque "cambiar la configuración es arriesgado y difícil de deshacer." Ese conservadurismo cuesta dinero directamente en QPS desperdiciado y costo de oportunidad.

La existencia de vista previa + instantánea + reversión cambia el cálculo de riesgo. Los operadores hacen más cambios, más rápido, con resultados medibles.

## Referencias de implementación

- Capítulo del manual con capturas de pantalla: [Configuración de pretargeting](../06-pretargeting.md)
- Flujos de interfaz de usuario de historial de cambios y reversión
- Lógica de instantánea y aplicación del backend en la plataforma Cat-Scan

Este flujo de trabajo es una de las demostraciones más claras de que el equipo detrás de Cat-Scan ha operado realmente asientos de Authorized Buyers a escala, no solo ha leído los documentos de la API.

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.
