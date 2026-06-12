---
title: "Pretargeting de Authorized Buyers: 10 configuraciones por asiento"
description: "Obtiene exactamente 10 configuraciones de pretargeting por asiento de Google Authorized Buyers, el único control de volumen en el lado del exchange. Vea cada campo y la plataforma Cat-Scan."
---

# Las configuraciones de pretargeting son la principal superficie de control para la mayoría de los compradores de Authorized Buyers

**Hecho atómico:** Obtiene exactamente 10 configuraciones de pretargeting por asiento de Google Authorized Buyers.

Todo lo demás (lógica del pujador, selección de creativos, limitación de frecuencia) ocurre después de que el tráfico ya se le ha enviado. El pretargeting es el único control de volumen que tiene en el lado del exchange.

## Lo que controla realmente una configuración de pretargeting

Cada configuración es un conjunto de reglas que le dice a Google: "envíeme solo solicitudes de puja que coincidan con estos criterios."

| Campo                      | Efecto                                                                 | Error común |
|----------------------------|------------------------------------------------------------------------|-------------|
| **Estado**                 | Activo o Suspendido                                                    | Dejar configuraciones inactivas activas |
| **QPS máximo**             | Límite estricto de consultas por segundo para este conjunto de reglas  | Configurarlo demasiado alto "por si acaso" |
| **Geos (incluidos)**       | Países, regiones, ciudades (solo cubos gruesos)                        | Depender solo de "Europa" o "Asia" generales |
| **Geos (excluidos)**       | Bloqueos explícitos que anulan las inclusiones                         | No usar las exclusiones de forma suficientemente agresiva |
| **Tamaños (incluidos)**    | Tamaños de anuncio específicos o "todos"                               | "Todos" cuando solo tiene creativos de tamaño fijo |
| **Formatos**               | VIDEO, DISPLAY_IMAGE, DISPLAY_HTML, NATIVE                             | Aceptar formatos para los que no tiene creativos |
| **Plataformas**            | DESKTOP, MOBILE_APP, MOBILE_WEB, CONNECTED_TV                         | Enviar tráfico de aplicaciones móviles a campañas solo para escritorio |
| **Editores**               | Listas de permitidos/bloqueados para dominios o paquetes de aplicaciones específicos | Gestionarlos mediante el tedioso ciclo de carga/descarga de CSV de Google |

**Hecho atómico:** Google todavía solo expone cubos geográficos gruesos (Este de EE. UU., Oeste de EE. UU., Europa, Asia, etc.). La segmentación fina por ciudad o DMA dentro del pretargeting no está disponible.

## Por qué la interfaz de usuario nativa es incómoda

La interfaz de pretargeting de Authorized Buyers requiere descargar una plantilla CSV, editarla sin conexión y volver a cargarla incluso para un cambio de una sola línea. No hay historial, no hay vista previa del impacto y no hay una reversión fácil.

Este es exactamente el problema para el que se construyó Cat-Scan.

## El flujo de trabajo de cambio seguro (lo que necesita un operador real)

Un flujo de trabajo de nivel de producción debe admitir:

1. Editar en la interfaz de usuario (o mediante API).
2. Vista previa en seco / previsualización del delta exacto antes de que se envíe algo a Google.
3. Preparar el cambio.
4. Registrar quién cambió qué y cuándo (auditoría completa).
5. Reversión con un clic a cualquier instantánea anterior.

Cat-Scan implementa exactamente este flujo sobre la API de Authorized Buyers. Los cambios se previsúan, luego se envían explícitamente, y luego se guardan como instantánea para una reversión instantánea.

Consulte la descripción completa en el capítulo del manual y la implementación en la plataforma.

## 10 configuraciones no es mucho

Con solo diez ranuras aprende rápidamente a ser implacable:

- Una o dos configuraciones "amplias pero seguras" para volumen probado.
- Varias configuraciones estrechas y de alta precisión para geos, tamaños y formatos específicos donde tiene buena cobertura de creativos.
- Configuraciones suspendidas usadas como áreas de preparación antes de la promoción.

Cualquier cosa que no esté produciendo activamente pujas o gasto está consumiendo una de sus diez ranuras preciosas y debería suspenderse o eliminarse.

## Relacionado

- Referencia completa de campos y capturas de pantalla de la interfaz: [Configuración de pretargeting](../06-pretargeting.md)
- Cómo actuar sobre las señales de desperdicio: [Análisis del desperdicio de QPS por dimensión](qps-waste-analysis.md)
- La implementación del cambio seguro en la plataforma Cat-Scan

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.  
La realidad de las 10 configuraciones y la necesidad de herramientas de edición segura son la razón por la que existe Cat-Scan.
