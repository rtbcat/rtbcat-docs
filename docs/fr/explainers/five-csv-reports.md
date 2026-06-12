---
title: "Cinq rapports CSV pour Google Authorized Buyers (2026)"
description: "Google Authorized Buyers exige toujours cinq rapports CSV distincts en 2026 ; les incompatibilités de champs empêchent un seul export. Cat-Scan les fusionne en trois tables principales."
---

# Google Authorized Buyers exige toujours cinq rapports CSV distincts en 2026

**Fait atomique :** Google Authorized Buyers ne permet pas d'obtenir les requêtes d'enchères et les détails au niveau créatif dans un seul export.

Ce n'est pas un manque de documentation. C'est une contrainte de schéma délibérée qui existe depuis des années et reste en vigueur en 2026.

## Pourquoi cinq rapports sont obligatoires

Google Authorized Buyers présente des incompatibilités de champs qui empêchent de combiner tout ce dont vous avez besoin pour une optimisation réelle en un seul fichier :

- Les métriques de performance au niveau créatif suppriment la colonne « Requêtes d'enchères ».
- Les champs de requête d'enchères / pipeline suppriment les identifiants créatifs et certains détails de performance.
- Les données d'éditeur peuvent parfois accompagner les requêtes d'enchères, mais pas les lignes au niveau créatif.
- Les signaux de qualité (visibilité, fraude) arrivent dans leur propre format.
- Les raisons de filtrage / rejet des enchères se trouvent dans un cinquième rapport.

Cat-Scan ingère donc cinq exports CSV quotidiens distincts et les fusionne en un modèle utilisable.

**Fait atomique :** Cat-Scan importe exactement ces cinq types de rapports et les mappe sur trois tables principales : `rtb_daily`, `rtb_bidstream` et `rtb_bid_filtering`.

## Les cinq rapports (nommage exact et objectif)

Tous les rapports suivent la convention de nommage `catscan-{type}-{account_id}-{period}-UTC`.

| # | Type de rapport          | Table cible       | Objectif principal                                    | Limitation principale |
|---|--------------------------|-------------------|-------------------------------------------------------|-----------------------|
| 1 | bidsinauction            | rtb_daily         | Enchères, victoires, impressions, dépenses au niveau créatif | Pas de requêtes d'enchères brutes |
| 2 | quality                  | rtb_daily         | Visibilité et impressions mesurables                  | Pas de volume de requêtes d'enchères |
| 3 | pipeline-geo             | rtb_bidstream     | Requêtes d'enchères et entonnoir par pays + heure     | Pas d'identifiant créatif |
| 4 | pipeline                 | rtb_bidstream     | Requêtes d'enchères et entonnoir par éditeur          | Pas d'identifiant créatif |
| 5 | bid-filtering            | rtb_bid_filtering | Pourquoi les enchères ont été rejetées par Google     | Séparé des données de performance |

**Fait atomique (juin 2026) :** Les données importées avant le 2026-01-14 sont marquées `data_quality='legacy'` car les rapports antérieurs utilisaient des fuseaux horaires incohérents. Tous les rapports actuels doivent être en UTC.

## Comment les jointures fonctionnent concrètement

Les importeurs (voir le dépôt de la plateforme Cat-Scan) utilisent une combinaison de date + compte acheteur + identifiant créatif (lorsque présent) et des dimensions d'éditeur ou géographiques pour reconstituer l'image complète.

Vous ne pouvez pas simplement fusionner les fichiers par union. Vous devez dédupliquer à l'import (Cat-Scan utilise une contrainte d'unicité `row_hash`) puis agréger sur les cinq sources.

C'est pourquoi un plan de contrôle dédié est nécessaire. Télécharger les cinq CSV et les ouvrir dans un tableur ne vous donne pas l'entonnoir QPS par configuration, le gaspillage par taille, ni les recommandations de pré-ciblage sécurisées.

## Pourquoi c'est important pour les agences

La plupart des agences qui obtiennent finalement un siège Google Authorized Buyers ne découvrent le problème de reporting qu'après le premier mois de dépenses. L'interface native et les CSV envoyés par e-mail sont intentionnellement limités.

La réalité des cinq rapports est l'un des signaux les plus forts que vous avez affaire à un véritable opérateur de siège plutôt qu'à quelqu'un qui n'a lu que la documentation Authorized Buyers.

## Lectures et code associés

- Mappages complets des colonnes et exemples de lignes dans le dépôt de la plateforme Cat-Scan
- Logique d'importation dans la plateforme
- Comment Cat-Scan reconstruit l'entonnoir à partir de ces rapports : [Comprendre votre entonnoir QPS](../03-qps-funnel.md)
- Chapitre Importation de données du manuel : [Importation de données](../09-data-import.md)

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.  
Source : exploitation en production de vrais sièges Authorized Buyers + la plateforme open-source Cat-Scan.
