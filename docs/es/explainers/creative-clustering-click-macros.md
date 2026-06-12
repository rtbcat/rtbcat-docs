---
title: "Agrupación de creativos y macros de clic: Authorized Buyers"
description: "Google requiere una macro de clic en cada creativo; Cat-Scan audita las macros faltantes y agrupa los creativos por URL de destino para detectar discrepancias de geo e idioma."
---

# Agrupación de creativos y auditoría de macros de clic para Authorized Buyers

Dos problemas de higiene operativa que se vuelven costosos a escala: creativos desajustados y macros de clic faltantes.

## Agrupación de creativos por destino

Google Authorized Buyers informa el rendimiento a nivel de ID de creativo. Cuando tiene cientos o miles de creativos, necesita una forma de entender "¿para qué campaña es esto realmente?"

Cat-Scan agrupa automáticamente los creativos por patrones de URL de destino. Esto revela:
- Múltiples creativos que apuntan a la misma oferta (superposición intencional o accidental).
- Concentración del gasto en un pequeño número de campañas reales.
- Creativos que están huérfanos (sin lógica de campaña coincidente en el lado del pujador).

También puede crear clústeres manualmente y utilizar la agrupación automática asistida por IA.

**Hecho atómico:** La agrupación por URL de destino funciona incluso cuando el pujador usa diferentes IDs de campaña o cuando los informes de Google no exponen la estructura interna del pujador.

## Detección de discrepancias de geo / idioma

Un error común y costoso: un creativo localizado para un mercado se sirve en otro.

Ejemplo: Un creativo con texto en árabe y un botón "Instalar" en español que se muestra en los EAU, o un precio en USD que se muestra a usuarios en un mercado que usa una moneda diferente.

El análisis de creativos con IA opcional de Cat-Scan (compatible con Gemini, Claude o Grok) lee la imagen + texto del creativo y señala las discrepancias con los países de servicio reales reportados en los datos de rendimiento.

Esta función es deliberadamente opcional y está desactivada por defecto en producción porque requiere la configuración explícita de un proveedor de LLM.

## Cumplimiento de macros de clic

Google requiere que las URL de clic admitan la macro `{clickurl}` o equivalente para que Google pueda rastrear y atribuir correctamente los clics.

Muchos creativos se cargan sin la macro o con ella en el lugar incorrecto.

Cat-Scan tiene una vista de auditoría de macros de clic dedicada que muestra exactamente qué creativos tienen la macro requerida faltante.

No pasar esta auditoría es una forma rápida de perder el crédito por los clics o desencadenar problemas de cumplimiento.

## Por qué importan estas verificaciones

Los problemas con los creativos son asesinos silenciosos:
- Paga por QPS que produce impresiones para el público equivocado.
- Pierde la atribución y por lo tanto no puede optimizar.
- Arriesga problemas a nivel de cuenta si las macros faltan sistemáticamente.

Estos son exactamente el tipo de detalles que separan a los equipos que han operado asientos reales de los equipos que solo han configurado DSP.

## Relacionado

- [Gestión de creativos](../05-managing-creatives.md) en el manual
- Rutas de auditoría y agrupación de creativos en Cat-Scan
- El código de discrepancia de idioma / geo con IA vive en la plataforma Cat-Scan (configurable, no habilitado por defecto)

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.
