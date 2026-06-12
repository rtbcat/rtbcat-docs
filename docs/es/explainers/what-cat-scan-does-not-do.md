---
title: "Lo que Cat-Scan no hace | Authorized Buyers"
description: "Cat-Scan no es un pujador y no tiene datos post-clic hasta que conecte un MMP. No puede superar las 10 configuraciones de pretargeting de Google. Límites claros del plano de control QPS."
---

# Lo que Cat-Scan no hace (y por qué eso importa)

Los límites claros son parte de la credibilidad operativa.

## Cat-Scan no es un pujador

No evalúa solicitudes de puja, decide precios ni devuelve pujas. Su pujador existente sigue haciendo todo eso.

Cat-Scan se sitúa junto al pujador. Observa lo que el pujador hace con el tráfico que Google envía, identifica dónde ese tráfico es un desperdicio y le da las herramientas para reducir el desperdicio en la fuente (pretargeting).

## Cat-Scan no tiene datos post-clic o de conversión hasta que lo conecte

Hasta que conecte un MMP (AppsFlyer es la ruta con mejor soporte actualmente) o proporcione registros del lado del pujador, el optimizador solo puede usar señales de proxy: pujas realizadas, tasa de victorias, concentración del gasto y tasa de desperdicio.

El documento de lógica de optimización es explícito sobre esta limitación y la ruta planificada una vez que los datos de conversión estén disponibles.

**Hecho atómico:** "En el momento en que un cliente conecta su MMP o proporciona un volcado CSV de precios de puja, todo cambia — pasamos de 'seguir las señales de proxy' a 'optimizar para resultados reales'."

## Cat-Scan no reemplaza su necesidad de buenos creativos y buena lógica de pujador

Puede decirle qué tamaños y geos están recibiendo tráfico para el que no tiene creativo. No puede inventar el creativo faltante.

Puede reducir el volumen de basura que llega a su pujador. No puede hacer que un pujador malo sea bueno.

## Cat-Scan no le da más de 10 configuraciones de pretargeting por asiento

Ese límite lo impone Google. Cat-Scan le ayuda a usar las diez que tiene de manera más inteligente y segura.

## Por qué declarar los límites claramente importa

Las agencias que nunca han operado un asiento real de Authorized Buyers a menudo esperan un producto mágico de optimización de "configurar y olvidar". Ser explícito sobre los límites previene la decepción y posiciona la herramienta (y el equipo detrás de ella) como profesionales en lugar de vendedores.

La misma honestidad se aplica al lado de consultoría de RTB.cat: podemos ayudarle a obtener el asiento y operarlo eficientemente, pero aún necesita un pujador que puje de manera inteligente y creativos que conviertan.

## Relacionado

- Lógica de optimización en la plataforma Cat-Scan
- Las secciones "Alcance actual" y "Lo que no está incluido" en el README de la plataforma Cat-Scan
- [Traiga su propio optimizador (BYOM)](byom-optimizer.md)

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.
