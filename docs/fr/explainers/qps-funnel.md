---
title: "Entonnoir QPS pour Google Authorized Buyers | Cat-Scan"
description: "Un siège demandant 50,000 QPS en reçoit souvent bien moins, puis l'enchérisseur rejette la majorité de ce qui arrive. Cartographiez l'entonnoir QPS Authorized Buyers et le taux de gaspillage avec Cat-Scan."
---

# L'entonnoir QPS pour les sièges Google Authorized Buyers

**Fait atomique :** Un siège typique demandant 50,000 QPS en reçoit souvent bien moins, et l'enchérisseur rejette ensuite la majorité de ce qui arrive réellement.

L'écart entre ce que vous avez demandé à Google d'envoyer et ce que votre enchérisseur peut réellement utiliser est le problème économique central de l'exploitation d'un siège Authorized Buyers.

## Les étapes (ce que signifie réellement chaque chiffre)

| Étape               | Définition                                                                              | Qui paie / qui est concerné          |
|---------------------|-----------------------------------------------------------------------------------------|--------------------------------------|
| **QPS**             | Le plafond que vous définissez dans le pré-ciblage. Google limite le débit en fonction de votre niveau de compte et de vos performances récentes. | Vous payez pour la connexion ; Google décide du volume réel |
| **Requêtes d'enchères atteintes** | Requêtes qui sont effectivement arrivées à votre endpoint | Le coût de votre infrastructure |
| **Enchères**        | Requêtes sur lesquelles votre enchérisseur a choisi d'enchérir                        | La logique de votre enchérisseur     |
| **Victoires**       | Enchères remportées (vous ne payez que celles-ci)                                     | Vos dépenses média réelles           |
| **Impressions**     | Publicités diffusées après la victoire                                                 | Ce que l'utilisateur a réellement vu |
| **Clics**           | Interactions des utilisateurs avec vos publicités diffusées                            | Qualité du créatif + page de destination |
| **Dépenses**        | L'argent qui a quitté votre compte                                                     | Le seul chiffre qui compte en définitive |

**Fait atomique :** La plus grande chute dans la plupart des sièges se situe entre QPS (ou requêtes atteintes) et Enchères. C'est le gaspillage que votre configuration de pré-ciblage est censée prévenir.

## Taux de gaspillage

Taux de gaspillage = (QPS - Enchères) / QPS

Si votre taux de gaspillage dépasse 50 %, vous payez pour un flux que votre enchérisseur ignore en grande partie. Ce volume aurait pu être réalloué à des configurations où l'enchérisseur enchérit et gagne réellement.

Cat-Scan présente cela sur la page d'accueil comme diagnostic principal.

## Pourquoi l'entonnoir est plus difficile dans Authorized Buyers que dans la plupart des DSP

- Vous êtes limité à 10 configurations de pré-ciblage par siège.
- Le ciblage géographique utilise des segments très grossiers.
- Il n'existe pas d'API de reporting en temps réel ; tout provient des cinq CSV quotidiens.
- Vous ne pouvez pas voir les « raisons de non-enchère » côté enchérisseur à moins d'ingérer vous-même les journaux de l'enchérisseur.

Google effectue beaucoup de filtrage de son côté avant que le trafic ne vous parvienne. Ce qui reste est encore plein de bruit que seules vos règles de pré-ciblage et votre couverture créative peuvent corriger.

## Comment Cat-Scan rend l'entonnoir visible et actionnable

- Il reconstruit l'entonnoir complet à partir des cinq rapports.
- Il le décompose par configuration de pré-ciblage, géo, éditeur, taille et créatif.
- Il affiche le QPS alloué par rapport au volume réellement réalisé par configuration.
- Il vous permet de modifier les règles de pré-ciblage qui contrôlent le haut de l'entonnoir, avec aperçu et annulation.

Consultez l'implémentation en direct dans le tableau de bord Cat-Scan (page d'accueil + routes `/qps/*`) et le modèle de données qui alimente les calculs.

## Métriques clés dérivées de l'entonnoir

- Taux de victoire = Victoires / Enchères
- CTR = Clics / Impressions
- CPM (ce que vous avez réellement payé)
- Gaspillage effectif (le QPS demandé que vous n'avez jamais pu monétiser)

Lorsque vous connectez des données post-clic (AppsFlyer ou autre MMP), l'entonnoir acquiert une étape finale de « résultat rentable ». En attendant, vous optimisez sur les enchères + la concentration des dépenses + le taux de victoire.

## Associé

- [Comprendre votre entonnoir QPS](../03-qps-funnel.md) (chapitre complet du manuel avec captures d'écran)
- [Analyse du gaspillage par dimension](qps-waste-analysis.md) dans ces explications
- [Configurations de pré-ciblage](pretargeting-configs.md)
- Logique d'optimisation utilisée en production dans le dépôt de la plateforme Cat-Scan

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.  
Ce modèle d'entonnoir est implémenté et éprouvé en production dans la plateforme open-source Cat-Scan.
