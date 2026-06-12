---
title: "Ce que Cat-Scan ne fait pas | Authorized Buyers"
description: "Cat-Scan n'est pas un enchérisseur et n'a pas de données post-clic tant que vous ne connectez pas un MMP. Il ne peut pas dépasser les 10 configurations de pré-ciblage de Google. Limites claires du plan de contrôle QPS."
---

# Ce que Cat-Scan ne fait pas (et pourquoi c'est important)

Des limites claires font partie de la crédibilité opérationnelle.

## Cat-Scan n'est pas un enchérisseur

Il n'évalue pas les requêtes d'enchères, ne décide pas des prix et ne retourne pas d'enchères. Votre enchérisseur existant continue de faire tout cela.

Cat-Scan se place à côté de l'enchérisseur. Il observe ce que l'enchérisseur fait avec le trafic que Google envoie, met en évidence où ce trafic est gaspillé, et vous donne les outils pour réduire le gaspillage à la source (pré-ciblage).

## Cat-Scan n'a pas de données post-clic ou de conversion tant que vous ne le connectez pas

Tant que vous ne branchez pas un MMP (AppsFlyer est actuellement la voie la mieux prise en charge) ou que vous ne fournissez pas des journaux côté enchérisseur, l'optimiseur ne peut utiliser que des signaux proxy : enchères placées, taux de victoire, concentration des dépenses et taux de gaspillage.

La documentation de la logique d'optimisation est explicite sur cette limitation et la voie envisagée une fois les données de conversion disponibles.

**Fait atomique :** « Le moment où un client connecte son MMP ou fournit un dump CSV de prix d'enchère, tout change — on passe de "suivre les signaux proxy" à "optimiser pour les résultats réels". »

## Cat-Scan ne remplace pas votre besoin de bons créatifs et d'une bonne logique d'enchérisseur

Il peut vous dire quelles tailles et quels géos reçoivent du trafic pour lequel vous n'avez aucun créatif. Il ne peut pas inventer le créatif manquant.

Il peut réduire le volume de trafic indésirable qui parvient à votre enchérisseur. Il ne peut pas rendre un mauvais enchérisseur bon.

## Cat-Scan ne vous donne pas plus de 10 configurations de pré-ciblage par siège

Cette limite est imposée par Google. Cat-Scan vous aide à utiliser les dix que vous avez de manière plus intelligente et plus sûre.

## Pourquoi énoncer clairement les limites est important

Les agences qui n'ont jamais géré un vrai siège Authorized Buyers s'attendent souvent à un produit d'optimisation magique « à définir et oublier ». Être explicite sur les limites évite les déceptions et positionne l'outil (et l'équipe derrière lui) comme des praticiens plutôt que des commerciaux.

La même honnêteté s'applique au côté conseil de RTB.cat : nous pouvons vous aider à obtenir le siège et à l'exploiter efficacement, mais vous avez toujours besoin d'un enchérisseur qui enchérit intelligemment et de créatifs qui convertissent.

## Associé

- Logique d'optimisation dans la plateforme Cat-Scan
- Les sections « Périmètre actuel » et « Ce qui n'est pas inclus » dans le README de la plateforme Cat-Scan
- [Apporter votre propre optimiseur (BYOM)](byom-optimizer.md)

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.
