---
title: "Rapports CSV Authorized Buyers : 5 rapports dont Cat-Scan a besoin"
description: "Google Authorized Buyers ne dispose pas d'API de reporting, aussi Cat-Scan reconstruit l'entonnoir à partir de cinq rapports CSV planifiés. Référence complète des métriques, dimensions et étapes de configuration."
---

# Configuration de vos rapports CSV

*Public : acheteurs média, chefs de compte*

Avant que Cat-Scan puisse analyser quoi que ce soit, il a besoin de données. Google Authorized Buyers
ne dispose pas d'API de reporting, aussi toutes les données transitent par **cinq rapports CSV planifiés**
que vous créez une seule fois dans votre compte Google AB.

!!! warning "Pourquoi cinq rapports distincts ?"
    Les colonnes de reporting de Google ne sont pas toutes compatibles entre elles. Par exemple,
    « Requêtes d'enchères » ne peut pas figurer dans le même rapport que « Identifiant d'application mobile »
    ou « Identifiant créatif + Identifiant de facturation ». Pour obtenir une visibilité complète de l'entonnoir,
    vous avez besoin de cinq rapports que Cat-Scan joint automatiquement.

## Les cinq rapports en un coup d'œil

| # | Nom du rapport | Ce qu'il indique à Cat-Scan | Colonnes clés |
|---|----------------|----------------------------|---------------|
| 1 | **Quality** | Performance au niveau créatif avec visibilité | Billing ID, Creative ID, Impressions, Spend, Active View |
| 2 | **Bids in Auction** | Pipeline d'enchères au niveau créatif (enchères -> victoires) | Creative ID, Bids, Bids in auction, Auctions won |
| 3 | **Pipeline -- Geo** | Entonnoir complet du flux d'enchères par pays | Bid requests, Country, Reached queries, Impressions |
| 4 | **Pipeline -- Publisher** | Entonnoir complet du flux d'enchères par éditeur | Bid requests, Publisher ID, Publisher name |
| 5 | **Bid Filtering** | Pourquoi Google rejette vos enchères | Filtering reason, Bids, Opportunity cost |

---

## Référence complète des métriques

Chaque métrique que Cat-Scan ingère, sa signification, et quel rapport la contient.

### Métriques d'entonnoir (pipeline du flux d'enchères)

Ces métriques suivent la progression d'une requête d'enchère à travers le système d'enchères de Google.
Présentes dans les rapports **Pipeline -- Geo** et **Pipeline -- Publisher**.

| Métrique | Définition | Unité | Rapport(s) |
|----------|-----------|-------|------------|
| **Bid requests** | Total des requêtes d'enchères que Google a envoyées à votre endpoint d'enchérisseur. C'est le volume entrant brut — le haut de l'entonnoir. Inclut les requêtes auxquelles votre enchérisseur n'a peut-être pas répondu à temps. | nombre | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | Requêtes d'enchères qui ont effectivement atteint votre enchérisseur et obtenu une réponse (réussie ou non). Inférieur à « Bid requests » si votre enchérisseur a des problèmes de latence ou des délais d'attente. | nombre | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | Requêtes pour lesquelles votre enchérisseur a trouvé un inventaire correspondant (un créatif adapté à la requête). C'est le premier filtre : si vous n'avez aucun créatif pour la taille/le format demandé, le processus s'arrête ici. | nombre | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | Requêtes pour lesquelles votre enchérisseur a retourné une réponse d'enchère valide et analysable (HTTP 200 avec une enchère bien formée). Exclut les délais d'attente, les erreurs et les non-enchères. | nombre | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | Réponses d'enchères réelles placées par votre enchérisseur. Un sous-ensemble des réponses réussies — votre enchérisseur peut répondre avec succès mais choisir de ne pas enchérir (réponse de non-enchère). | nombre | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | Enchères que Google a acceptées dans la vente aux enchères. Les enchères peuvent être rejetées avant l'entrée en enchère en raison de règles de filtrage (désapprobation de créatif, violations de politique, prix plancher, exclusions de pré-ciblage). L'écart entre « Bids » et « Bids in auction » est indiqué dans le rapport Bid Filtering. | nombre | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | Enchères qui ont remporté la vente aux enchères. Vous payez pour celles-ci. L'écart entre « Bids in auction » et « Auctions won » représente la concurrence — d'autres acheteurs vous ont surenchéri. | nombre | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | Publicités réellement affichées dans le navigateur ou l'application d'un utilisateur après avoir remporté la vente aux enchères. Légèrement inférieur à « Auctions won » en raison des échecs de rendu d'annonce, des navigations de page avant le rendu et des interférences de bloqueurs de publicité. | nombre | Les cinq rapports |
| **Clicks** | Interactions des utilisateurs (appuis/clics) sur vos annonces diffusées. | nombre | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### Métriques de dépenses et de coût

| Métrique | Définition | Unité | Rapport(s) |
|----------|-----------|-------|------------|
| **Spend** | Total des sommes dépensées pour les impressions remportées sur la période. C'est votre coût média réel. Libellé dans la devise de votre compte (généralement USD). | devise (micros dans les données brutes, dollars dans l'interface) | Quality |
| **Opportunity cost** | Revenus estimés perdus parce que Google a filtré vos enchères avant qu'elles entrent dans la vente aux enchères. Calculé par Google sur la base des taux de victoire historiques et des CPM pour un inventaire similaire. Utile pour hiérarchiser les raisons de filtrage à corriger en priorité. | devise | Bid Filtering |

### Métriques de qualité et de visibilité

Ce sont des métriques au niveau créatif du rapport **Quality**. Elles mesurent
ce qui se passe *après* la diffusion de l'impression.

| Métrique | Définition | Unité | Rapport(s) |
|----------|-----------|-------|------------|
| **Active View viewable** | Impressions ayant respecté le standard de visibilité MRC : au moins 50 % des pixels de l'annonce étaient dans la zone visible du navigateur pendant au moins 1 seconde continue (2 secondes pour la vidéo). C'est le standard industriel pour « cette annonce a-t-elle été réellement vue ». | nombre | Quality |
| **Active View measurable** | Impressions pour lesquelles la visibilité *pouvait* être mesurée. Certains environnements (certaines applications, iframes cross-domain, anciens navigateurs) bloquent la mesure. Taux de visibilité = Active View viewable / Active View measurable. | nombre | Quality |
| **Video starts** | Nombre de fois qu'un créatif vidéo a commencé à jouer. Uniquement renseigné pour les créatifs au format vidéo. | nombre | Quality |
| **Video completions** | Nombre de fois qu'un créatif vidéo a joué jusqu'à 100 % de son achèvement (ou jusqu'au point d'ignorance si ignorable). Taux de complétion vidéo = completions / starts. | nombre | Quality |

### Métriques de filtrage des enchères

Provenant du rapport **Bid Filtering**. Ces métriques vous indiquent *pourquoi* les enchères sont
rejetées avant d'entrer dans la vente aux enchères.

| Métrique | Définition | Unité | Rapport(s) |
|----------|-----------|-------|------------|
| **Bids** | Total des enchères placées par votre enchérisseur (même définition que ci-dessus). Dans ce rapport, utilisé comme dénominateur pour calculer les taux de filtrage. | nombre | Bid Filtering |
| **Bids in auction** | Enchères ayant survécu au filtrage et entré dans la vente aux enchères. `Bids - Bids in auction` = total des enchères filtrées. | nombre | Bid Filtering |
| **Opportunity cost** | Voir les métriques de dépenses ci-dessus. Dans ce rapport, ventilé par raison de filtrage afin que vous puissiez voir quelle raison vous coûte le plus. | devise | Bid Filtering |

### Dimensions (colonnes de regroupement)

Les dimensions ne sont pas des métriques — ce sont les axes selon lesquels les métriques sont
ventilées. Cat-Scan les utilise pour segmenter vos données.

| Dimension | Ce que c'est | Quels rapports |
|-----------|-------------|----------------|
| **Day** | Date du calendrier (UTC). Requise dans tous les rapports. Cat-Scan l'utilise pour la déduplication et l'affichage des séries temporelles. | Les cinq |
| **Hour** | Heure du jour (0--23, UTC). Permet une granularité horaire dans l'analyse du pipeline. | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | Code pays ISO à deux lettres (ex. US, DE, IL). L'origine géographique de la requête d'enchère. | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering (optionnel) |
| **Billing ID (Pretargeting config)** | Identifiant numérique de la configuration de pré-ciblage qui a accepté ce trafic. Mappe 1:1 vers une carte de configuration dans Cat-Scan. | Quality |
| **Creative ID** | Identifiant numérique Google du créatif. Lie vers la galerie de créatifs dans Cat-Scan. | Quality, Bids in Auction, Bid Filtering (optionnel) |
| **Creative size** | Dimensions en pixels du créatif (ex. `300x250`, `728x90`). Utilisé pour l'analyse du gaspillage par taille. | Quality |
| **Creative format** | Le format d'annonce : `DISPLAY_IMAGE`, `DISPLAY_HTML`, `VIDEO`, `NATIVE`. | Quality (optionnel) |
| **Platform** | Plateforme de l'appareil : `DESKTOP`, `MOBILE_APP`, `MOBILE_WEB`, `CONNECTED_TV`. | Quality (optionnel) |
| **Environment** | Où l'annonce a été diffusée : `WEB`, `APP`. | Quality (optionnel) |
| **App ID** | Identifiant du bundle d'application mobile (ex. `com.example.app`). Uniquement renseigné pour l'inventaire in-app. | Quality (optionnel) |
| **App name** | Nom de l'application lisible par l'humain. | Quality (optionnel) |
| **Publisher ID** | Identifiant numérique de l'éditeur (site web ou application). | Quality (optionnel), Pipeline -- Publisher |
| **Publisher name** | Nom de l'éditeur lisible par l'humain. | Quality (optionnel), Pipeline -- Publisher |
| **Publisher domain** | Le domaine du site web de l'éditeur (ex. `news.example.com`). | Quality (optionnel) |
| **Buyer account ID** | L'identifiant de votre compte acheteur / siège. Nécessaire lorsque vous gérez plusieurs sièges. | Bids in Auction, Bid Filtering (optionnel) |
| **Filtering reason** | Le code de raison de Google pour lequel une enchère a été filtrée avant d'entrer dans la vente aux enchères (ex. `CREATIVE_NOT_APPROVED`, `BID_BELOW_AUCTION_FLOOR`, `DISAPPROVED_BY_EXCHANGE`). | Bid Filtering |

---

## Étape par étape : créer chaque rapport

### 1. Rapport Quality

C'est votre rapport de performance au niveau créatif avec les données de visibilité et de dépenses.

**Dans Google Authorized Buyers -> Reporting -> Nouveau rapport :**

| Paramètre | Valeur |
|-----------|--------|
| Type de rapport | RTB |
| Plage de temps | Hier (planifié quotidiennement) |
| Dimensions | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| Dimensions optionnelles | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| Métriques | Reached queries, Impressions, Clicks, Spend |
| Métriques optionnelles | Video starts, Video completions, Active View viewable, Active View measurable |

**Nom de fichier suggéré :** `catscan-quality`

!!! note
    Ce rapport ne doit **pas** inclure « Bid requests », « Bids » ou « Bids in
    auction » — ces colonnes sont incompatibles avec « Billing ID » dans le reporting de Google.

---

### 2. Rapport Bids in Auction

Ce rapport capture le pipeline d'enchères au niveau créatif, en complétant les
métriques que le rapport Quality ne peut pas inclure.

| Paramètre | Valeur |
|-----------|--------|
| Type de rapport | RTB |
| Plage de temps | Hier (planifié quotidiennement) |
| Dimensions | Day, Country, Creative ID, Buyer account ID |
| Métriques | Bids in auction, Auctions won, Bids, Impressions |

**Nom de fichier suggéré :** `catscan-bidsinauction`

!!! info "Comment Cat-Scan les joint"
    Quality + Bids in Auction sont joints sur `(Day, Creative ID)` pour vous donner
    une image complète : des enchères placées aux impressions servies et aux dépenses engagées.

---

### 3. Rapport Pipeline -- Geo

C'est votre rapport de haut de l'entonnoir : combien de requêtes d'enchères Google vous envoie
par pays, et combien survivent à chaque étape de l'entonnoir.

| Paramètre | Valeur |
|-----------|--------|
| Type de rapport | RTB |
| Plage de temps | Hier (planifié quotidiennement) |
| Dimensions | Day, Country, Hour |
| Métriques | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Nom de fichier suggéré :** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    N'ajoutez **pas** Creative ID, Billing ID ou App ID à ce rapport. Ces
    colonnes sont incompatibles avec « Bid requests ».

---

### 4. Rapport Pipeline -- Publisher

Identique à Pipeline -- Geo, mais ventilé par éditeur plutôt que (ou en plus de) la géographie.

| Paramètre | Valeur |
|-----------|--------|
| Type de rapport | RTB |
| Plage de temps | Hier (planifié quotidiennement) |
| Dimensions | Day, Country, Hour, Publisher ID, Publisher name |
| Métriques | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**Nom de fichier suggéré :** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Rapport Bid Filtering

Ce rapport vous indique *pourquoi* Google filtre vos enchères avant qu'elles entrent dans la
vente aux enchères — indispensable pour diagnostiquer les problèmes de pré-ciblage.

| Paramètre | Valeur |
|-----------|--------|
| Type de rapport | RTB |
| Plage de temps | Hier (planifié quotidiennement) |
| Dimensions | Day, Filtering reason |
| Dimensions optionnelles | Country, Buyer account ID, Creative ID |
| Métriques | Bids, Bids in auction, Opportunity cost |

**Nom de fichier suggéré :** `catscan-bid-filtering`

### Raisons de filtrage courantes

Voici les valeurs que vous verrez dans la dimension **Filtering reason**. Chacune
vous indique une raison spécifique pour laquelle Google a rejeté votre enchère avant l'entrée en vente aux enchères.

| Raison de filtrage | Ce que cela signifie | Que faire |
|-------------------|---------------------|-----------|
| `CREATIVE_NOT_APPROVED` | Le créatif n'a pas passé la vérification de Google, ou a été désapprouvé | Vérifiez le statut du créatif dans Google AB. Corrigez les violations de politique. |
| `BID_BELOW_AUCTION_FLOOR` | Votre prix d'enchère était inférieur au CPM minimum de l'éditeur | Augmentez l'enchère ou excluez l'inventaire de faible valeur via le pré-ciblage |
| `DISAPPROVED_BY_EXCHANGE` | La politique au niveau de la place de marché de Google a bloqué l'enchère | Consultez les politiques publicitaires de Google pour le créatif spécifique |
| `FILTERED_BY_PRETARGETING` | Vos propres règles de pré-ciblage ont exclu ce trafic | Intentionnel si vos règles sont correctes ; à vérifier si inattendu |
| `NO_MATCHING_CREATIVE` | La requête d'enchère demandait une taille/format que vous n'avez pas | Importez des créatifs pour les tailles manquantes, ou excluez ces tailles dans le pré-ciblage |
| `CREATIVE_SIZE_MISMATCH` | Les dimensions du créatif ne correspondent pas à l'emplacement publicitaire | Vérifiez la taille du créatif par rapport à ce que l'éditeur demande |
| `LANDING_PAGE_DISAPPROVED` | L'URL de destination a échoué à la vérification de Google | Corrigez la page de destination ou utilisez une URL différente |
| `SSL_REQUIRED` | L'éditeur exige HTTPS mais votre créatif ou page de destination utilise HTTP | Passez tous les assets et URL en HTTPS |
| `FREQUENCY_CAPPED` | L'utilisateur a déjà vu ce créatif trop de fois | Comportement attendu ; ajustez les plafonds de fréquence s'ils sont trop agressifs |

---

## Planification de la livraison

Pour chacun des cinq rapports :

1. Cliquez sur **Planifier** dans Google Authorized Buyers.
2. Définissez la fréquence sur **Quotidien**.
3. Définissez la méthode de livraison :
      - **E-mail** — envoyez au compte Gmail connecté à Cat-Scan (active
        l'import automatique). Voir [Importation de données](09-data-import.md) pour la
        configuration de l'import automatique Gmail.
      - **Manuel** — si vous préférez télécharger et importer vous-même les CSV via
        `/import`.

!!! tip "Utilisez l'import automatique Gmail"
    Planifier les cinq rapports pour les envoyer par e-mail à un compte Gmail connecté signifie que
    Cat-Scan les importe automatiquement chaque jour. Aucun import manuel nécessaire
    après la configuration initiale.

## Vérification de votre configuration

Après avoir importé votre premier jeu de CSV (manuellement ou via Gmail) :

1. Accédez à `/import` dans Cat-Scan.
2. Vérifiez la **Grille de fraîcheur des données** — vous devriez voir « importé » pour les cinq
   types de rapports pour la date d'hier.
3. Si des cellules affichent « manquant », le rapport correspondant n'a pas encore été reçu.

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

Une fois que les cinq colonnes affichent le vert pour hier, Cat-Scan dispose de données complètes et
chaque fonctionnalité (entonnoir, analyse du gaspillage, recommandations, optimiseur) fonctionnera.

## Détection automatique

Vous n'avez pas besoin d'indiquer à Cat-Scan quel rapport vous importez. Le système d'import
détecte automatiquement le type de rapport à partir des en-têtes de colonnes :

- Contient **Bid filtering reason** ? -> Bid Filtering
- Contient **Bid requests** + **Publisher ID** ? -> Pipeline -- Publisher
- Contient **Bid requests** (sans Publisher ID) ? -> Pipeline -- Geo
- Contient **Creative ID** + **Billing ID** ? -> Quality
- Contient **Creative ID** + **Bids in auction** ? -> Bids in Auction

## Comment Cat-Scan utilise chaque métrique

Ceci mappe les métriques CSV brutes à ce que vous voyez dans l'interface Cat-Scan.

| Fonctionnalité de l'interface | Métriques utilisées | Rapport(s) source |
|------------------------------|--------------------|--------------------|
| **Entonnoir QPS** (page d'accueil) | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline (les deux) + Quality |
| **Calcul du % de gaspillage** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **Taux de victoire** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | Tout rapport contenant les deux |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **Taux de visibilité** | `Active View viewable / Active View measurable` | Quality |
| **Taux de complétion vidéo** | `Video completions / Video starts` | Quality |
| **Analyse du gaspillage géo** (`/qps/geo`) | Bid requests, Impressions, Spend par Country | Pipeline -- Geo + Quality |
| **Gaspillage par éditeur** (`/qps/publisher`) | Bid requests, Impressions, Spend par Publisher | Pipeline -- Publisher + Quality |
| **Gaspillage par taille** (`/qps/size`) | Impressions, Spend par Creative size | Quality |
| **Raisons de filtrage** (`/qps/filtering`) | Bids, Bids in auction, Opportunity cost par Filtering reason | Bid Filtering |
| **Métriques de la carte de configuration** | Reached queries, Impressions, Spend par Billing ID | Quality |
| **Performance des créatifs** | Impressions, Clicks, Spend, Active View viewable par Creative ID | Quality |
| **Scoring de l'optimiseur** | Toutes les métriques pipeline + quality, agrégées par segment | Les cinq |

## Erreurs courantes

| Erreur | Ce qui se passe | Correction |
|--------|----------------|------------|
| Ajouter « Bid requests » au rapport Quality | Google génère des erreurs ou retourne des données incomplètes | Supprimez « Bid requests » — incompatible avec « Billing ID » |
| Oublier le rapport Bid Filtering | Cat-Scan ne peut pas vous montrer *pourquoi* les enchères sont rejetées | Créez le 5e rapport avec la dimension « Filtering reason » |
| Utiliser « 7 derniers jours » au lieu de « Hier » | Données chevauchantes, fichiers plus grands, imports plus lents | Définissez sur « Hier » et planifiez quotidiennement |
| Ne pas planifier — uniquement des exports manuels | Les données deviennent obsolètes, les vérifications de santé échouent | Planifiez la livraison quotidienne par e-mail |
| Dimension « Hour » manquante dans les rapports Pipeline | Pas de granularité horaire dans l'analyse QPS | Ajoutez Hour à Pipeline -- Geo et Pipeline -- Publisher |
| Métriques optionnelles manquantes dans le rapport Quality | Pas de données de visibilité ou vidéo dans Cat-Scan | Ajoutez Active View viewable, Active View measurable, Video starts, Video completions |

## Étapes suivantes

- [Navigation admin](02-navigating-the-dashboard.md) : disposition de la barre latérale et
  liste de vérification de configuration
- [Importation de données](09-data-import.md) : mécanismes d'import détaillés, imports
  fragmentés et dépannage
- [Entonnoir QPS](03-qps-funnel.md) : une fois les données en circulation, commencez l'analyse
