---
title: "Rapport de filtrage des enchères : cinquième CSV Authorized Buyers"
description: "Le cinquième rapport, catscan-bid-filtering, est le seul endroit où Google vous indique pourquoi il a rejeté une enchère avant même qu'elle atteigne votre enchérisseur. Lisez les raisons de filtrage côté place de marché."
---

# Raisons de filtrage des enchères et le cinquième rapport Authorized Buyers

**Fait atomique :** Le cinquième rapport (`catscan-bid-filtering`) est le seul endroit où Google vous indique pourquoi il a rejeté une enchère avant même qu'elle ait atteint votre enchérisseur.

La plupart des opérateurs ne le consultent jamais parce qu'il arrive dans son propre CSV et n'est pas joint aux données de performance par défaut.

## Ce que contient le rapport de filtrage des enchères

Il met en évidence les raisons pour lesquelles Google a appliqué un filtrage des enchères côté place de marché pour des requêtes qui correspondaient à votre pré-ciblage mais ont ensuite été filtrées avant d'être envoyées.

Les catégories courantes comprennent :
- Inadéquations de créatif ou de taille (du point de vue de Google)
- Signaux de qualité d'éditeur ou d'inventaire
- Filtres de fréquence ou autres filtres de politique
- Problèmes techniques ou de format

Lorsqu'il est joint aux quatre autres rapports, il explique une partie de la chute entre « requêtes atteintes » et « enchères » qui n'est pas sous le contrôle de votre enchérisseur.

## Pourquoi il est précieux

Votre enchérisseur ne voit que ce que Google lui livre réellement. Le rapport de filtrage des enchères offre une vue sur la dernière couche de filtrage qui s'est produite côté Google.

Si une grande part du volume potentiel est filtrée pour « taille de créatif non prise en charge », la bonne correction se situe généralement dans votre liste de tailles de pré-ciblage, pas dans l'enchérisseur.

## Comment Cat-Scan l'utilise

Le rapport est importé dans la table appropriée. Il est disponible pour l'analyse aux côtés des vues d'entonnoir et de gaspillage.

C'est l'un des signaux qui peuvent être injectés dans un optimiseur personnalisé (voir l'explication BYOM).

## Code et documentation associés

- Table cible et objectif dans la documentation du modèle de données de la plateforme Cat-Scan
- Le cinquième rapport fait partie du flux d'import standard des cinq rapports décrit dans le chapitre Importation de données

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.
