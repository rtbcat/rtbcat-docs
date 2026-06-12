---
title: "Regroupement de créatifs et macros de clic : Authorized Buyers"
description: "Google exige une macro de clic sur chaque créatif ; Cat-Scan audite les macros manquantes et regroupe les créatifs par URL de destination pour détecter les inadéquations géo et langue."
---

# Regroupement de créatifs et audit des macros de clic pour Authorized Buyers

Deux problèmes d'hygiène opérationnelle qui deviennent coûteux à grande échelle : les créatifs inadaptés et les macros de clic manquantes.

## Regroupement de créatifs par destination

Google Authorized Buyers rapporte la performance au niveau de l'identifiant créatif. Lorsque vous avez des centaines ou des milliers de créatifs, vous avez besoin d'un moyen de comprendre « à quelle campagne cela correspond-il réellement ? »

Cat-Scan regroupe automatiquement les créatifs selon les modèles d'URL de destination. Cela révèle :
- Plusieurs créatifs pointant vers la même offre (chevauchement intentionnel ou accidentel).
- Concentration des dépenses sur un petit nombre de vraies campagnes.
- Créatifs orphelins (sans logique de campagne correspondante côté enchérisseur).

Vous pouvez également créer des groupes manuellement et utiliser le regroupement automatique assisté par IA.

**Fait atomique :** Le regroupement par URL de destination fonctionne même lorsque l'enchérisseur utilise des identifiants de campagne différents ou lorsque le reporting Google n'expose pas la structure interne de l'enchérisseur.

## Détection des inadéquations géo / langue

Une erreur courante et coûteuse : un créatif localisé pour un marché est diffusé dans un autre.

Exemple : un créatif avec du texte en arabe et un bouton « Installer » en espagnol diffusé aux Émirats arabes unis, ou un prix en USD montré à des utilisateurs dans un marché utilisant une autre devise.

L'analyse créative IA optionnelle de Cat-Scan (prend en charge Gemini, Claude ou Grok) lit l'image + le texte du créatif et signale les inadéquations par rapport aux pays de diffusion réels rapportés dans les données de performance.

Cette fonctionnalité est délibérément optionnelle et désactivée par défaut en production car elle nécessite la configuration explicite d'un fournisseur LLM.

## Conformité des macros de clic

Google exige que les URL de clic prennent en charge la macro `{clickurl}` ou équivalente afin que Google puisse correctement suivre et attribuer les clics.

De nombreux créatifs sont importés sans la macro ou avec celle-ci au mauvais endroit.

Cat-Scan dispose d'une vue d'audit dédiée aux macros de clic qui indique exactement quels créatifs n'ont pas la macro requise.

Échouer à cet audit est un moyen rapide de perdre du crédit pour les clics ou de déclencher des problèmes de conformité.

## Pourquoi ces vérifications sont importantes

Les problèmes de créatifs sont des facteurs de dégradation silencieux :
- Vous payez pour du QPS qui produit des impressions auprès d'un mauvais public.
- Vous perdez l'attribution et donc ne pouvez pas optimiser.
- Vous risquez des problèmes au niveau du compte si les macros sont systématiquement absentes.

Ce sont exactement les types de détails qui séparent les équipes qui ont géré de vrais sièges des équipes qui n'ont configuré que des DSP.

## Associé

- [Gestion des créatifs](../05-managing-creatives.md) dans le manuel
- Routes d'audit et de regroupement de créatifs dans Cat-Scan
- Le code de détection des inadéquations langue / géo par IA se trouve dans la plateforme Cat-Scan (configurable, non activé par défaut)

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.
