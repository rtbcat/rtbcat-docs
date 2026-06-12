---
title: "Analyse du gaspillage QPS par géo, éditeur, taille | Cat-Scan"
description: "Google envoie plus de 300 tailles d'annonces et des milliers d'éditeurs ; la plupart n'ont aucun créatif correspondant ni aucune enchère. Trois vues Cat-Scan transforment le gaspillage QPS en listes d'exclusion."
---

# Analyse du gaspillage QPS par éditeur, géo et taille dans Authorized Buyers

**Fait atomique :** Google vous envoie des centaines de tailles d'annonces et des milliers d'éditeurs. La plupart d'entre eux n'ont aucun créatif correspondant ou aucune enchère de votre enchérisseur.

Les trois vues dimensionnelles dans Cat-Scan (géo, éditeur, taille) transforment les chiffres bruts de l'entonnoir en listes d'exclusion actionnables.

## Les trois vues

### Gaspillage géographique

Affiche QPS, enchères, victoires, dépenses et taux de gaspillage par pays et ville.

Constatations typiques :
- QPS élevé en provenance de pays où vous n'avez aucun créatif ou aucun budget.
- Villes qui reçoivent un volume disproportionné mais presque aucune victoire.
- Régions entières que l'enchérisseur ignore complètement.

Action : Ajoutez les géos les plus problématiques à la liste d'exclusion de la configuration de pré-ciblage concernée.

### Gaspillage par éditeur

Classe les domaines et bundles d'applications par volume reçu par rapport aux enchères placées et aux dépenses.

Constatations typiques :
- Éditeurs à QPS élevé où l'enchérisseur enchérit sur moins de 5 % des requêtes.
- Applications qui génèrent du volume mais zéro victoire (souvent à cause d'un plancher ou d'une inadéquation de créatif).
- Une longue traîne d'inventaire de faible qualité qui consomme quand même votre allocation QPS.

Action : Utilisez l'éditeur de blocage/autorisation par configuration pour bloquer les moins performants. C'est nettement plus facile que le laborieux aller-retour avec le modèle CSV de Google.

**Fait atomique :** L'éditeur de blocage/autorisation des éditeurs de Cat-Scan fonctionne par configuration de pré-ciblage et prend en charge la recherche + les modifications en masse avec aperçu.

### Gaspillage par taille

Google vous enverra volontiers plus de 300 tailles d'annonces différentes, même si vous n'avez des créatifs que pour une poignée d'entre elles.

Constatation typique : plus de 80 % du QPS dans des tailles pour lesquelles vous n'avez aucun créatif.

Action : Listez explicitement uniquement les tailles que vous prenez réellement en charge dans la configuration de pré-ciblage. C'est l'un des changements uniques à plus fort effet de levier que la plupart des nouveaux sièges peuvent effectuer.

## Comment les données sont construites

Les trois vues sont calculées à partir du jeu de données des cinq rapports joints après import. Aucun appel API Google supplémentaire n'est requis pour l'analyse elle-même (la synchronisation du pré-ciblage est séparée).

Les mêmes données alimentent l'entonnoir de la page d'accueil et les propositions de l'optimiseur.

## Pourquoi cette analyse est rare

La plupart des agences ne voient jamais ces détails parce qu'elles ne joignent jamais les cinq CSV et ne construisent jamais les agrégats par dimension. Elles regardent les rapports de performance de haut niveau que Google envoie par e-mail et supposent que « l'enchérisseur s'en chargera ».

L'enchérisseur ne peut gérer que ce qui lui parvient réellement. Tout ce qui lui parvient mais est rejeté vous a déjà coûté de l'allocation QPS et de l'infrastructure.

## Associé

- [L'entonnoir QPS](qps-funnel.md)
- [Configurations de pré-ciblage](pretargeting-configs.md)
- [Changements sécurisés de pré-ciblage](safe-pretargeting-changes.md)
- Traitement complet dans le manuel : [Analyse du gaspillage par dimension](../04-analyzing-waste.md)

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.  
Ces trois vues sont disponibles en direct dans chaque déploiement Cat-Scan.
