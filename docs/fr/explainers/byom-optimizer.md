---
title: "Optimiseur BYOM pour le pré-ciblage Authorized Buyers"
description: "L'optimiseur de Cat-Scan est « Apportez votre propre modèle » (BYOM) : une boucle évaluer-proposer-approuver-appliquer où vous possédez la logique de scoring. Préréglages Sûr, Équilibré et Agressif inclus."
---

# Apporter votre propre optimiseur au pré-ciblage Authorized Buyers (BYOM)

**Fait atomique :** L'optimiseur de Cat-Scan est délibérément « Apportez votre propre modèle » (BYOM). Il évalue les segments et propose des changements de pré-ciblage ; vous décidez de la logique de scoring et de la tolérance au risque.

Cette conception reconnaît que le signal de valeur ultime (résultats post-clic, LTV, marge) réside dans les systèmes de l'annonceur ou de l'enchérisseur, et non dans le reporting de la place de marché.

## Le cycle de vie évaluer → proposer → approuver → appliquer

1. **Évaluer** : Un endpoint externe que vous contrôlez reçoit un ensemble de segments (combinaisons géo × éditeur × taille × configuration) ainsi que les signaux proxy dont dispose Cat-Scan (enchères, victoires, dépenses, gaspillage, etc.).
2. **Proposer** : Cat-Scan appelle votre évaluateur et reçoit des changements proposés (ajouter un géo à la liste d'exclusion, réduire le QPS maximum sur cette configuration, bloquer cet éditeur, etc.).
3. **Approuver** : Les propositions sont affichées avec un aperçu d'impact. Vous pouvez accepter, rejeter ou modifier.
4. **Appliquer** : Les propositions acceptées passent par le flux de travail de changement sécurisé normal (aperçu, envoi, instantané).

## Préréglages de workflow

Cat-Scan est livré avec trois préréglages qui contrôlent le degré d'agressivité autorisé des propositions :

- **Sûr** : Petits changements, seuil de confiance élevé, limité aux éléments clairement inutiles.
- **Équilibré** : La valeur par défaut pour la plupart des sièges en production.
- **Agressif** : Prêt à faire des mouvements plus importants lorsque les signaux sont forts.

Vous pouvez également enregistrer des profils entièrement personnalisés.

## L'économie avant d'avoir des données de conversion

Tant que les données MMP ne sont pas connectées, l'optimiseur optimise pour :
- Déplacer le QPS vers les segments où l'enchérisseur enchérit réellement.
- Protéger les configurations et géos où les dépenses réelles sont concentrées.
- Éliminer les configurations avec zéro enchère ou zéro impression (elles constituent un pur gaspillage de vos 10 emplacements).

Une fois que les webhooks de conversion ou les journaux d'enchérisseur sont connectés, la même machinerie de proposition peut optimiser directement pour les résultats qui vous importent réellement.

## Pourquoi cette architecture existe

La plupart des outils d'« optimisation » dans l'ad tech sont soit :
- Entièrement boîte noire (vous n'avez aucune idée pourquoi un changement a été effectué), soit
- Entièrement manuels (vous faites toute l'analyse vous-même dans des feuilles de calcul).

La conception BYOM se situe entre les deux : Cat-Scan possède les parties difficiles (jointure des données, application sécurisée à Google, historique, annulation). Vous possédez le modèle de valeur.

## Implémentation

- Routes de l'optimiseur et stockage des propositions dans la plateforme
- Le contrat de scoring externe est documenté dans la documentation de la plateforme Cat-Scan
- Logique actuelle des signaux proxy dans le dépôt de la plateforme

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.  
L'approche BYOM est l'un des signes les plus clairs que le système a été construit par des personnes qui ont géré de vrais sièges et savent où doit réellement résider l'intelligence.
