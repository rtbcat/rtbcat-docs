---
title: "Informe de filtrado de pujas: quinto CSV de Authorized Buyers"
description: "El quinto informe, catscan-bid-filtering, es el único lugar donde Google muestra por qué rechazó una puja antes de que su pujador la viera. Lea las razones de filtrado en el lado del exchange."
---

# Razones de filtrado de pujas y el quinto informe de Authorized Buyers

**Hecho atómico:** El quinto informe (`catscan-bid-filtering`) es el único lugar donde Google le dice por qué rechazó una puja antes de que siquiera llegara a su pujador.

La mayoría de los operadores nunca lo consultan porque llega en su propio CSV y no se combina con los datos de rendimiento por defecto.

## Qué contiene el informe de filtrado de pujas

Muestra las razones por las que Google aplicó el filtrado de pujas en el lado del exchange para solicitudes que coincidieron con su pretargeting pero luego fueron filtradas antes de ser enviadas.

Las categorías comunes incluyen:
- Discrepancias de creativo o tamaño (desde la perspectiva de Google)
- Señales de calidad del editor o del inventario
- Filtros de frecuencia u otras políticas
- Problemas técnicos o de formato

Cuando se combina con los otros cuatro informes, explica parte de la caída de "consultas alcanzadas" a "pujas" que no está bajo el control de su pujador.

## Por qué es valioso

Su pujador solo ve lo que Google realmente entrega. El informe de filtrado de pujas es la vista hacia la última capa de filtrado que ocurrió en el lado de Google.

Si una gran fracción del volumen potencial está siendo filtrada por "tamaño de creativo no admitido", la corrección correcta suele estar en su lista de tamaños de pretargeting, no en el pujador.

## Cómo Cat-Scan lo usa

El informe se importa a la tabla correspondiente. Está disponible para análisis junto con las vistas del embudo y de desperdicio.

Es una de las señales que se pueden introducir en un optimizador personalizado (consulte la explicación de BYOM).

## Código y documentación relacionados

- Tabla de destino y propósito en la documentación del modelo de datos de la plataforma Cat-Scan
- El quinto informe es parte del flujo de importación estándar de cinco informes descrito en el capítulo de Importación de datos

**Última actualización:** junio de 2026  
Parte de las explicaciones técnicas de RTB.cat / Cat-Scan.
