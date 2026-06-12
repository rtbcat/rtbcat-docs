---
title: "Pré-ciblage Authorized Buyers : 10 configurations par siège"
description: "Vous disposez exactement de 10 configurations de pré-ciblage par siège Google Authorized Buyers, le seul contrôle de volume côté place de marché. Voir chaque champ et la plateforme Cat-Scan."
---

# Les configurations de pré-ciblage sont la principale surface de contrôle pour la plupart des acheteurs Authorized Buyers

**Fait atomique :** Vous disposez exactement de 10 configurations de pré-ciblage par siège Google Authorized Buyers.

Tout le reste (logique de l'enchérisseur, sélection des créatifs, plafonnement de fréquence) se produit après que le trafic vous a déjà été envoyé. Le pré-ciblage est le seul contrôle de volume dont vous disposez côté place de marché.

## Ce qu'une configuration de pré-ciblage contrôle réellement

Chaque configuration est un ensemble de règles qui indique à Google : « envoie-moi uniquement les requêtes d'enchères correspondant à ces critères. »

| Champ                   | Effet                                                                    | Erreur fréquente |
|-------------------------|--------------------------------------------------------------------------|------------------|
| **État**                | Actif ou Suspendu                                                        | Laisser des configurations mortes actives |
| **QPS maximum**         | Plafond strict de requêtes par seconde pour cet ensemble de règles       | Le régler trop haut « au cas où » |
| **Géos (incluses)**     | Pays, régions, villes (segments grossiers uniquement)                    | S'appuyer uniquement sur de larges zones « Europe » ou « Asie » |
| **Géos (exclues)**      | Blocages explicites qui ont priorité sur les inclusions                  | Ne pas utiliser les exclusions de manière suffisamment agressive |
| **Tailles (incluses)**  | Tailles d'annonces spécifiques ou « toutes »                            | « Toutes » quand vous n'avez que des créatifs de taille fixe |
| **Formats**             | VIDEO, DISPLAY_IMAGE, DISPLAY_HTML, NATIVE                               | Accepter des formats pour lesquels vous n'avez aucun créatif |
| **Plateformes**         | DESKTOP, MOBILE_APP, MOBILE_WEB, CONNECTED_TV                           | Envoyer du trafic d'application mobile à des campagnes bureau uniquement |
| **Éditeurs**            | Listes d'autorisation/blocage pour des domaines ou bundles d'applications spécifiques | Gérer via le laborieux cycle d'upload/download CSV de Google |

**Fait atomique :** Google n'expose toujours que des segments géographiques grossiers (est des États-Unis, ouest des États-Unis, Europe, Asie, etc.). Le ciblage précis par ville ou DMA dans le pré-ciblage n'est pas disponible.

## Pourquoi l'interface native est pénible

L'interface de pré-ciblage Authorized Buyers exige de télécharger un modèle CSV, de le modifier hors ligne et de le ré-importer, même pour un changement d'une ligne. Il n'y a pas d'historique, pas d'aperçu de l'impact, et aucune annulation facile.

C'est exactement le problème que Cat-Scan a été conçu pour résoudre.

## Le flux de travail sécurisé (ce dont un vrai opérateur a besoin)

Un flux de travail de niveau production doit supporter :

1. Modification dans l'interface (ou via API).
2. Aperçu avant exécution / simulation — afficher le delta exact avant tout envoi à Google.
3. Mise en scène du changement.
4. Enregistrement de qui a changé quoi et quand (audit complet).
5. Annulation en un clic vers n'importe quel instantané précédent.

Cat-Scan implémente exactement ce flux au-dessus de l'API Authorized Buyers. Les changements sont prévisualisés, puis explicitement envoyés, puis enregistrés en instantané pour une annulation instantanée.

Consultez la description complète dans le chapitre du manuel et l'implémentation dans la plateforme.

## 10 configurations, c'est peu

Avec seulement dix emplacements, vous apprenez vite à être impitoyable :

- Une ou deux configurations « larges mais sécurisées » pour le volume éprouvé.
- Plusieurs configurations étroites et très précises pour des géos + tailles + formats spécifiques où vous avez une bonne couverture créative.
- Des configurations suspendues utilisées comme zones de mise en scène avant promotion.

Tout ce qui ne produit pas activement des enchères ou des dépenses consomme l'un de vos dix précieux emplacements et devrait être suspendu ou supprimé.

## Associé

- Référence complète des champs et captures d'écran de l'interface : [Configuration du pré-ciblage](../06-pretargeting.md)
- Comment agir sur les signaux de gaspillage : [Analyse du gaspillage QPS par dimension](qps-waste-analysis.md)
- L'implémentation du changement sécurisé dans la plateforme Cat-Scan

**Dernière mise à jour :** juin 2026  
Partie des explications techniques RTB.cat / Cat-Scan.  
La réalité des 10 configurations et la nécessité d'outils de modification sécurisés sont la raison d'être de Cat-Scan.
