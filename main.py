import argparse

from utils.csv_handler import consolidate_csv
from utils.search_tab import search_products
from utils.report_file import generate_report



def main():
    parser = argparse.ArgumentParser(description="Gestion des stocks via fichiers CSV")
    subparsers = parser.add_subparsers(dest="command", help="Commande à exécuter")

    # Commande de consolidation
    merge_parser = subparsers.add_parser("merge", help="Consolider plusieurs fichiers CSV")
    merge_parser.add_argument("--input-dir", required=True, help="Dossier contenant les fichiers CSV")
    merge_parser.add_argument("--output-file", required=True, help="Fichier CSV de sortie consolidé")

    # Commande de recherche
    search_parser = subparsers.add_parser("search", help="Rechercher des produits dans les stocks")
    search_parser.add_argument("--product-name", help="Nom du produit")
    search_parser.add_argument("--category", help="Catégorie du produit")
    search_parser.add_argument("--price-min", type=float, help="Prix minimum")
    search_parser.add_argument("--price-max", type=float, help="Prix maximum")

    # Commande de rapport
    report_parser = subparsers.add_parser("report", help="Générer un rapport récapitulatif")
    report_parser.add_argument("--input-file", required=True, help="Fichier CSV consolidé")
    report_parser.add_argument("--output-file", required=True, help="Fichier rapport de sortie")

    args = parser.parse_args()

    if args.command == "merge":
        consolidate_csv(args.input_dir, args.output_file)
    elif args.command == "search":
        search_products(args)
    elif args.command == "report":
        generate_report(args.input_file, args.output_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
