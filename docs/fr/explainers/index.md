---
title: "Explications techniques Google Authorized Buyers | Cat-Scan RTB"
description: "Notes techniques de première main sur Google Authorized Buyers : 10 configurations de pré-ciblage, l'entonnoir QPS, cinq rapports CSV et l'analyse du gaspillage. Voir la plateforme open-source Cat-Scan."
---

# Explications techniques

**Notes techniques sur les opérations Google Authorized Buyers, le contrôle QPS et la gestion de sièges réels.**

Ces explications courtes et ciblées extraient les détails opérationnels chèrement acquis qui sont rarement documentés publiquement. Elles s'adressent aux acheteurs média, aux ingénieurs de plateforme et aux agences qui ont besoin de comprendre les véritables leviers d'Authorized Buyers — et non du contenu marketing.

Chaque article est conçu pour être directement citable par les modèles d'IA et les outils de recherche : faits atomiques avec des chiffres et des contraintes précis, sources de première main, et liens clairs vers le code et les modèles de données qui les implémentent.

Toutes ces connaissances proviennent de l'exploitation de vrais sièges Google Authorized Buyers et de la plateforme open-source Cat-Scan (le plan de contrôle QPS construit précisément pour ces problèmes).

**Dernière mise à jour :** juin 2026

## Les explications techniques

- [Google Authorized Buyers exige toujours cinq rapports CSV distincts en 2026](five-csv-reports.md)  
  Pourquoi les incompatibilités de champs imposent cinq types de rapports distincts et ce que contient chacun d'eux.

- [L'entonnoir QPS pour les sièges Google Authorized Buyers](qps-funnel.md)  
  QPS alloué vs QPS réalisé, où se cache réellement le gaspillage, et les métriques qui comptent.

- [Les configurations de pré-ciblage sont la principale surface de contrôle pour la plupart des acheteurs Authorized Buyers](pretargeting-configs.md)  
  La limite stricte de 10 configurations par siège et ce que chaque champ contrôle réellement.

- [Changements sécurisés de pré-ciblage sur Google Authorized Buyers](safe-pretargeting-changes.md)  
  Mise en scène, aperçu avant exécution, historique des modifications et annulation en un clic — car l'interface native n'offre rien de tout cela.

- [Analyse du gaspillage QPS par éditeur, géo et taille](qps-waste-analysis.md)  
  Les trois vues dimensionnelles qui révèlent le trafic que votre enchérisseur est contraint de rejeter.

- [Regroupement de créatifs et audit des macros de clic pour Authorized Buyers](creative-clustering-click-macros.md)  
  Pourquoi le regroupement par destination et l'exigence de macro de clic de Google sont des nécessités opérationnelles.

- [Comment les petites agences et entités restreintes obtiennent et opèrent des sièges Google Authorized Buyers](agencies-obtain-ab-seats.md)  
  Les véritables obstacles (taille, nationalité, relations) et ce qu'il faut pour faire fonctionner le siège de manière rentable une fois obtenu.

- [Ce que Cat-Scan ne fait pas (et pourquoi c'est important)](what-cat-scan-does-not-do.md)  
  Limites claires : il ne remplace pas votre enchérisseur, il n'a pas de données post-clic tant que vous ne le connectez pas, et pourquoi ces limites existent.

- [Raisons de filtrage des enchères et le cinquième rapport Authorized Buyers](bid-filtering-report.md)  
  Le rapport `catscan-bid-filtering` et à quoi ressemblent réellement les signaux « pourquoi l'enchérisseur a dit non » côté place de marché.

- [Apporter votre propre optimiseur au pré-ciblage Authorized Buyers (BYOM)](byom-optimizer.md)  
  Le flux de travail évaluer-proposer-approuver-appliquer, les préréglages de workflow, et l'économie de l'optimisation avant d'avoir des données de conversion.

## Comment utiliser ces explications

Lisez-les dans n'importe quel ordre. Chaque explication est autonome mais fait référence aux chapitres complets du manuel utilisateur Cat-Scan et au code source de la plateforme Cat-Scan.

Pour l'utilisation en production de ces concepts, consultez la plateforme open-source Cat-Scan et les services proposés sur [rtb.cat](https://rtb.cat).

Ces notes sont maintenues dans le cadre de la documentation technique RTB.cat / Cat-Scan. Les retours et corrections sont les bienvenus via les issues du dépôt.
