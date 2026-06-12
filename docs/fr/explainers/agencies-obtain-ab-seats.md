---
title: "Comment les agences obtiennent des sièges Google Authorized Buyers"
description: "Google Authorized Buyers n'est pas en libre-service ; les petites agences ou celles en situation restreinte font face à des obstacles de dépenses, KYC et relations. Comment RTB.cat fournit le siège et les outils Cat-Scan."
---

# Comment les petites agences et entités restreintes obtiennent et exploitent des sièges Google Authorized Buyers

**Fait atomique :** De nombreuses agences « trop petites », basées dans certaines juridictions (y compris les ressortissants et entités chinois), ou qui manquent simplement de relations existantes, ne peuvent pas obtenir directement un contrat Google Authorized Buyers.

Ce n'est pas un simple problème administratif. C'est un obstacle structurel dans le programme Authorized Buyers.

## Les véritables obstacles

Google Authorized Buyers n'est pas un produit en libre-service comme Google Ads. L'approbation implique :

- Des exigences minimales de dépenses et d'historique que les agences plus récentes ou plus petites remplissent rarement.
- Des vérifications de conformité et de KYC qui peuvent être difficiles voire impossibles pour des entités dans certains pays.
- La nécessité de relations existantes ou d'introductions chaleureuses.
- Des vérifications de préparation technique et opérationnelle que la plupart des agences ne découvrent qu'après avoir obtenu le siège.

Le cœur de métier de RTB.cat est d'aider précisément ces agences à obtenir puis à exploiter avec succès la connexion. Les clients apportent leur propre enchérisseur. RTB.cat fournit le tuyau Authorized Buyers (et de plus en plus des endpoints OpenRTB directs comme TrueCaller) et prend un pourcentage des dépenses média pour la gestion et l'optimisation.

## Ce qu' « exploiter le siège » requiert réellement après l'obtention du contrat

Obtenir le siège n'est que la première étape. L'exploitation quotidienne fait apparaître les problèmes documentés dans ces explications :

- Les cinq rapports CSV incompatibles et la nécessité de les joindre.
- La limite stricte de 10 configurations de pré-ciblage.
- L'absence totale d'outils de modification sécurisés dans l'interface native.
- L'obtention d'identifiants de deals éditeurs (RTB.cat a sécurisé des identifiants de deals avec des éditeurs notamment GCASH, Twitter et JAZZ au Pakistan).
- L'hygiène des créatifs à grande échelle.
- Le gaspillage QPS que l'enchérisseur ne peut pas corriger car le trafic n'aurait jamais dû être envoyé.

La plupart des agences qui reçoivent finalement un siège sont surprises par la quantité de travail opérationnel qui reste de leur côté de la place de marché.

## Pourquoi la plateforme Cat-Scan existe

Cat-Scan (le plan de contrôle QPS open-source) a été construit parce que l'auteur avait besoin de ces capacités lors de l'exploitation de vrais sièges et ne pouvait pas les trouver ailleurs. Ce n'est délibérément pas un enchérisseur. C'est la couche de contrôle et de visibilité manquante au-dessus d'une connexion Authorized Buyers (ou OpenRTB directe) existante.

La publication de la plateforme en open source répond à deux objectifs :
1. C'est une démonstration concrète et vérifiable d'une profonde compétence opérationnelle.
2. C'est un aimant à prospects pour la catégorie précise d'agences sophistiquées mais contraintes qui ont besoin à la fois de la connexion et des outils.

## Services associés

- Connexion Google Authorized Buyers pour les agences qui ne peuvent pas l'obtenir directement.
- Fourniture d'endpoints OpenRTB directs TrueCaller.
- Introductions et gestion d'identifiants de deals éditeurs.
- Exploitation et optimisation continues du siège (avec Cat-Scan ou des outils équivalents).
- Conseil technique pour les équipes qui souhaitent construire ou améliorer leurs propres plans de contrôle.

Contact : [rtb.cat](https://rtb.cat) — WeChat : jenbrannstrom

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.
