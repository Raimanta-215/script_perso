# README

## Description projet Gestion des Stocks via CSV

Ce projet permet de consolider des fichiers CSV, rechercher des produits, générer des rapports récapitulatifs, et plus encore. Il utilise Python, pandas pour la manipulation de données, et argparse pour les commandes en ligne.

## Fonctionnalités
 - Consolidation des fichiers CSV: Fusionne tous les fichiers CSV d'un répertoire en un fichier consolidé.
 - Recherche de produits: Permet de chercher des produits dans le fichier consolidé par nom, catégorie, ou prix.
 - Génération de rapport: Crée un rapport récapitulatif des produits avec des statistiques clés comme la quantité totale, la valeur totale et le prix moyen par catégorie.

## Installation
1. Clonez le dépôt:  `git clone https://github.com/votrenom/gestion-stocks.git cd gestion-stocks`
2. Créez un environnement virtuel: `python -m venv .venv`
3. Activez l'environnement virtuel: `# Windows : .venv\Scripts\activate # MacOS/Linux source .venv/bin/activate`
4. Installez les dépendances: `pip install -r requirements.txt`


## Utilisation
### Commandes disponibles
 - Consolidation: `python main.py merge --input-dir <répertoire-des-fichiers-csv> --output-file <fichier-consolide.csv>`
 - Recherche: `python main.py search --product-name "Produit A" --category "Catégorie 1" --price-max 20`
 - Gestion des rapports: `python main.py report --input-file <fichier-consolide.csv> --output-file <rapport.pdf>`
   
