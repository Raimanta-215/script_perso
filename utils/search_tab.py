import pandas as pd


def search_products(args, file):
    """
    Recherche des produits dans un fichier CSV consolidé.

    PRE : -args (str) : Arguments passés par la ligne de commande.
           - file (str) : Chemin du fichier CSV

    POST : Affiche en console les produits recherchés

    RAISES : FileNotFoundError si le fichier n'existe pas


    """
    try:
        df = pd.read_csv(file)
        filters = []

        if args.product_name:
            filters.append(df['nom_produit'].str.contains(args.product_name, case=False, na=False))
        if args.category:
            filters.append(df['categorie'] == args.category)
        if args.price_min is not None:
            filters.append(df['prix'] >= args.price_min)
        if args.price_max is not None:
            filters.append(df['prix'] <= args.price_max)

        if filters:
            filtered_df = df[filters[0]]
            for f in filters[1:]:
                filtered_df = filtered_df[f]
            print(filtered_df)
        else:
            print("Aucun filtre spécifié, veuillez ajouter des critères de recherche.")
    except FileNotFoundError:
        print(f"Le fichier consolidé {file} est introuvable. Veuillez le générer d'abord.")
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")
