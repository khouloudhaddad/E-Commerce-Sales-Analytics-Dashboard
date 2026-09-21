# E-Commerce Sales Analytics Dashboard 🛒📊

## 📌 Présentation

**E-Commerce Sales Analytics Dashboard** est un mini-projet de Data Science consacré à l’analyse de ventes e-commerce simulées.

Le projet met en pratique les principales étapes d’un workflow Data Analyst :

- génération de données avec **NumPy** ;
- structuration et nettoyage avec **Pandas** ;
- calcul de métriques et analyses statistiques ;
- visualisation avec **Matplotlib** et **Seaborn** ;
- interprétation des résultats et formulation d’une recommandation stratégique.

Le projet est basé sur un jeu de données simulé de **500 commandes**, avec une graine aléatoire fixée à `42` afin de garantir la reproductibilité des résultats.

## 🎯 Objectifs

L’objectif est de construire une analyse complète à partir de données de transactions e-commerce, depuis la simulation des données brutes jusqu’à la création d’un tableau de bord graphique.

Les principales questions étudiées sont :

- Quel est le chiffre d’affaires total ?
- Quelle catégorie génère le plus gros chiffre d’affaires ?
- Quel est le panier moyen selon le mode de livraison ?
- Comment se répartit le montant total des commandes ?
- Existe-t-il une corrélation entre le montant d’une commande et la satisfaction client ?
- Quel mode de livraison présente le panier moyen le plus élevé ?

## 🧰 Technologies utilisées

- **Python**
- **NumPy** — génération et calculs numériques
- **Pandas** — manipulation, nettoyage et agrégation des données
- **Matplotlib** — visualisation
- **Seaborn** — visualisations statistiques

## 📊 Données simulées

Le dataset contient **500 commandes** avec les variables suivantes :

| Variable | Description |
|---|---|
| `Commande_ID` | Identifiant unique de la commande, de 1001 à 1500 |
| `Prix_Unitaire` | Prix unitaire compris entre 15 € et 150 € |
| `Quantite` | Quantité commandée, de 1 à 5 unités |
| `Frais_Livraison` | Frais de livraison générés selon une distribution normale |
| `Satisfaction_Client` | Score de satisfaction de 1 à 5 |
| `Categorie` | Électronique, Vêtements, Maison ou Livres |
| `Mode_Livraison` | Standard, Express ou Point Relais |
| `Montant_Total` | Montant total de la commande |

### Calcul du montant total

```text
Montant_Total = (Prix_Unitaire × Quantite) + Frais_Livraison
```

## 🧹 Nettoyage des données

Environ **5 %** des valeurs de `Satisfaction_Client` sont volontairement remplacées par des valeurs manquantes (`NaN`).

Ces valeurs sont ensuite imputées avec la **médiane de satisfaction calculée par catégorie de produit**.

## 📈 Analyses réalisées

Le projet calcule notamment :

- le **chiffre d’affaires total** ;
- le chiffre d’affaires par catégorie ;
- le **panier moyen par mode de livraison** ;
- les **25e, 50e et 75e percentiles** du `Montant_Total` ;
- la matrice de corrélation entre les variables numériques.

## 📊 Tableau de bord

Le tableau de bord est composé de quatre visualisations :

### 1. CA total par catégorie
Un **barplot Seaborn** permettant de comparer le chiffre d’affaires des différentes catégories.

### 2. Distribution du montant total par mode de livraison
Un **boxplot Seaborn** permettant de comparer la distribution des montants selon le mode de livraison.

### 3. Distribution des frais de livraison
Un **histogramme avec KDE** permettant d’observer la distribution des frais de livraison.

### 4. Matrice de corrélation
Une **heatmap Seaborn** présentant les corrélations entre les variables numériques.

## 📁 Structure recommandée

```text
ecommerce-sales-analytics/
│
├── README.md
├── ecommerce_sales_analysis.ipynb
├── requirements.txt
└── data/
    └── README.md
```

Comme les données sont simulées, aucun fichier de données externe n’est nécessaire au départ.

## 🚀 Installation

Cloner le projet :

```bash
git clone <URL_DU_REPOSITORY>
cd ecommerce-sales-analytics
```

Installer les dépendances :

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

Lancer Jupyter Notebook :

```bash
jupyter notebook
```

Puis ouvrir :

```text
ecommerce_sales_analysis.ipynb
```

## 🔬 Méthodologie

Le projet suit les étapes suivantes :

```text
Simulation des données
        ↓
Création du DataFrame
        ↓
Nettoyage & imputation
        ↓
Calcul du Montant_Total
        ↓
Analyses statistiques
        ↓
Visualisations
        ↓
Interprétation
        ↓
Recommandation stratégique
```

## 📝 Livrable

Le livrable attendu est un **script Python ou un notebook Jupyter** contenant :

1. la génération des données ;
2. la construction et le nettoyage du DataFrame ;
3. les analyses statistiques ;
4. le tableau de bord graphique ;
5. l’interprétation des résultats ;
6. une recommandation stratégique basée sur les résultats obtenus.

## 👨‍🏫 Contexte pédagogique

**Mini-Projet Data Science — Analyse des Ventes E-Commerce**

- Niveau : **Intermédiaire**
- Durée estimée : **1h30 à 2h**
- Enseignant : **Ali Saidi**

## 📚 Références

- NumPy — https://numpy.org/
- Pandas — https://pandas.pydata.org/
- Matplotlib — https://matplotlib.org/
- Seaborn — https://seaborn.pydata.org/

## 📄 Licence

Projet pédagogique destiné à l’apprentissage et à la mise en pratique des fondamentaux de l’analyse de données avec Python.
