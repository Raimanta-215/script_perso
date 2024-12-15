import sqlite3
import argparse
import os

# Chemin de la base SQLite
DATABASE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),'db', 'magasin.db')


# Fonction pour rechercher des produits par différents critères
def search_products(criteria, value):
    """
    Recherche des produits dans la base selon un critère donné.

    Args:
        criteria (str): Le critère de recherche ("product_name", "category", etc.).
        value (str): La valeur à rechercher.

    Returns:
        list: Liste des résultats correspondants.
    """
    query = f"SELECT * FROM stocks WHERE {criteria} LIKE ?"

    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Exécuter la requête
        cursor.execute(query, (f"%{value}%",))
        results = cursor.fetchall()

        # Afficher les résultats
        for row in results:
            print(row)

        return results

    except sqlite3.Error as e:
        print(f"Erreur de base de données : {e}")

    finally:
        conn.close()


# Fonction principale pour l'interface CLI
def main():
    parser = argparse.ArgumentParser(description="Rechercher des produits dans la base de données.")

    parser.add_argument("--name", help="Rechercher par nom de produit.", type=str)
    parser.add_argument("--category", help="Rechercher par catégorie.", type=str)
    parser.add_argument("--price", help="Rechercher par prix maximum.", type=float)

    args = parser.parse_args()

    if args.name:
        print(f"Recherche de produits par nom contenant : {args.name}")
        search_products("product_name", args.name)

    if args.category:
        print(f"Recherche de produits dans la catégorie : {args.category}")
        search_products("category", args.category)

    if args.price:
        print(f"Recherche de produits avec un prix maximum de : {args.price}")
        query = "SELECT * FROM stocks WHERE unit_price <= ?"

        try:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()

            # Exécuter la requête
            cursor.execute(query, (args.price,))
            results = cursor.fetchall()

            for row in results:
                print(row)

        except sqlite3.Error as e:
            print(f"Erreur de base de données : {e}")

        finally:
            conn.close()


if __name__ == "__main__":
    main()
