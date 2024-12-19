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
5. Lancer l'application : Vous pouvez maintenant exécuter l'application en mode interactif avec la commande suivante : `python main.py`


## Utilisation
Lorsque l'application démarre en mode interactif, vous pouvez entrer différentes commandes pour gérer les fichiers CSV. Voici quelques exemples de commandes :
### Commandes disponibles
 - Consolidation: `merge --input-dir <path> --output-file <file>`
   - --input-dir : Dossier contenant les fichiers CSV à consolider.
   - --output-file : Fichier CSV de sortie consolidé.
 - Recherche: `search --file <file> --product-name <nom du produit> --category <catégorie> --price-min <prix minimum> --price-max <prix maximum>`
   - --file : Fichier CSV consolidé dans lequel rechercher.
   - --product-name : Nom du produit à rechercher (optionnel).
   - --category : Catégorie du produit à rechercher (optionnel).
   - --price-min : Prix minimum pour la recherche (optionnel).
   - --price-max : Prix maximum pour la recherche (optionnel).
 - Gestion des rapports: `report --input-file <file> --output-file <report_file>`
   - --input-file : Fichier CSV consolidé pour générer le rapport.
   - --output-file : Fichier rapport de sortie.

