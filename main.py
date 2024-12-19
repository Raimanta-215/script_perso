import argparse
from utils.csv_handler import consolidate_csv
from utils.search_tab import search_products
from utils.report_file import generate_report


def interactive_mode():
    """
    Mode interactif pour permettre à l'utilisateur de saisir des commandes en boucle.
    """
    print("Bienvenue dans le gestionnaire de stocks via fichiers CSV.")
    print("Entrez 'exit' pour quitter le programme.")
    while True:
        command = input("\nEntrez votre commande : ").strip()
        if command.lower() == "exit":
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break

        args = parse_command(command.split())
        if not args:
            print("Commande invalide. Veuillez réessayer.")
            continue

        execute_command(args)


def parse_command(input_args):
    """
    Analyse les arguments donnés par l'utilisateur.

    Args:
        input_args (list): Liste des arguments fournie par l'utilisateur.

    Returns:
        Namespace: Les arguments analysés ou None en cas d'erreur.
    """
    parser = argparse.ArgumentParser(description="Gestion des stocks via fichiers CSV")
    subparsers = parser.add_subparsers(dest="command", help="Commande à exécuter")

    # Commande de consolidation
    merge_parser = subparsers.add_parser("merge", help="Consolider plusieurs fichiers CSV")
    merge_parser.add_argument("--input-dir", required=True, help="Dossier contenant les fichiers CSV")
    merge_parser.add_argument("--output-file", required=True, help="Fichier CSV de sortie consolidé")

    # Commande de recherche
    search_parser = subparsers.add_parser("search", help="Rechercher des produits dans les stocks")
    search_parser.add_argument("--file", required=True, help="Fichier CSV consolidé")
    search_parser.add_argument("--product-name", help="Nom du produit")
    search_parser.add_argument("--category", help="Catégorie du produit")
    search_parser.add_argument("--price-min", type=float, help="Prix minimum")
    search_parser.add_argument("--price-max", type=float, help="Prix maximum")

    # Commande de rapport
    report_parser = subparsers.add_parser("report", help="Générer un rapport récapitulatif")
    report_parser.add_argument("--input-file", required=True, help="Fichier CSV consolidé")
    report_parser.add_argument("--output-file", required=True, help="Fichier rapport de sortie")

    try:
        return parser.parse_args(input_args)
    except SystemExit:
        return None


def execute_command(args):
    """
    Exécute la commande spécifiée par l'utilisateur.

    Args:
        args (Namespace): Arguments analysés.
    """
    if args.command == "merge":
        consolidate_csv(args.input_dir, args.output_file)
    elif args.command == "search":
        search_products(args, args.file)
    elif args.command == "report":
        generate_report(args.input_file, args.output_file)
    else:
        print("Commande inconnue. Utilisez '--help' pour voir les options disponibles.")


if __name__ == "__main__":
    interactive_mode()
