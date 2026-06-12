---
title: "Changements sécurisés de pré-ciblage pour Authorized Buyers"
description: "L'interface native de pré-ciblage Google Authorized Buyers n'a pas d'historique des modifications ni d'annulation. Cat-Scan ajoute l'aperçu, la mise en scène, l'audit et l'annulation en un clic pour chaque modification."
---

# Changements sécurisés de pré-ciblage sur Google Authorized Buyers : mise en scène, aperçu, historique et annulation

**Fait atomique :** L'interface native de pré-ciblage Google Authorized Buyers ne dispose d'aucun historique des modifications et d'aucune fonction d'annulation.

Tout opérateur en production finit par faire un changement qui fait chuter le taux de victoire ou fait exploser le gaspillage. Sans outillage, la seule récupération est la reconstruction manuelle de l'état précédent de mémoire ou à partir d'anciens CSV.

## Le flux de travail sécurisé minimal viable

Tout système permettant de modifier le pré-ciblage en production doit fournir :

- **Aperçu / simulation** — Afficher le diff exact qui sera envoyé à Google avant qu'il ne soit envoyé.
- **Mise en scène** — Le changement n'est pas en ligne tant que vous ne confirmez pas explicitement « envoyer à Google ».
- **Audit** — Qui a changé quoi, quand, et quelles étaient les valeurs avant/après.
- **Instantané + annulation** — L'état précédent est stocké et peut être restauré en une seule action.

Cat-Scan a été conçu autour de ce contrat précis.

## Comment fonctionne le flux de travail dans Cat-Scan

1. L'opérateur ouvre une configuration de pré-ciblage (sur la page d'accueil ou dans les paramètres).
2. Il modifie un ou plusieurs champs (géos exclues, tailles, QPS maximum, blocages d'éditeurs, etc.).
3. Il clique sur **Aperçu**. Cat-Scan affiche les modifications précises qui seront apportées.
4. S'il est satisfait, il clique sur **Appliquer** (ou « Oui, envoyer à Google »).
5. Le changement est envoyé à l'API Authorized Buyers.
6. Un instantané de l'état de la configuration est stocké.
7. L'action apparaît dans la chronologie de l'historique global.

Si le taux de victoire chute ou que le gaspillage augmente, l'opérateur va dans l'historique, sélectionne le changement, prévisualise l'annulation et confirme. L'état précédent est restauré.

**Fait atomique :** Chaque mutation de pré-ciblage dans Cat-Scan est enregistrée avec horodatage, identité de l'utilisateur, ancienne valeur, nouvelle valeur, et un instantané complet pour l'annulation.

## Listes d'autorisation/blocage des éditeurs

La gestion des blocages d'éditeurs est particulièrement pénible dans l'interface native (aller-retour CSV complet pour chaque changement).

Cat-Scan offre un éditeur de recherche + blocage/autorisation par configuration qui prend en charge les opérations en masse et l'aperçu immédiat. C'est l'une des fonctionnalités au meilleur ROI pour les vrais sièges.

## Pourquoi cela dépasse le simple confort

Sans outillage sécurisé, les opérateurs deviennent conservateurs. Ils laissent circuler du mauvais trafic parce que « modifier la configuration est risqué et difficile à annuler ». Ce conservatisme coûte directement de l'argent en QPS gaspillé et en coût d'opportunité.

L'existence de l'aperçu + instantané + annulation change le calcul des risques. Les opérateurs font davantage de changements, plus rapidement, avec des résultats mesurables.

## Références d'implémentation

- Chapitre du manuel avec captures d'écran : [Configuration du pré-ciblage](../06-pretargeting.md)
- Flux d'interface de l'historique des modifications et de l'annulation
- Logique d'instantané et d'application dans la plateforme Cat-Scan

Ce flux de travail est l'une des démonstrations les plus claires que l'équipe derrière Cat-Scan a réellement exploité des sièges Authorized Buyers à grande échelle, et ne s'est pas contentée de lire la documentation de l'API.

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.
