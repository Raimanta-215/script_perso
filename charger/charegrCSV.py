import os
import pandas as pd
import sqlite3

# Définir les chemins des fichiers et de la base de données
CSV_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv')
DATABASE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),'db', 'magasin.db')


# Fonction pour lire et uniformiser les fichiers CSV
def load_and_clean_csv(file_path):
    """
    Charge un fichier CSV et uniformise les colonnes.
    Args:
        file_path (str): Chemin vers le fichier CSV.

    Returns:
        pd.DataFrame: DataFrame uniformisé.
    """
    df = pd.read_csv(file_path)

    # Exemple : Renommer les colonnes pour les rendre cohérentes
    column_mapping = {
        "Nom Produit": "product_name",
        "Quantité": "quantity",
        "Prix Unitaire": "unit_price",
        "Catégorie": "category",
    }
    df.rename(columns=column_mapping, inplace=True)

    # Assurer des types cohérents
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    return df


# Fonction pour insérer des données dans SQLite
def insert_into_database(df, table_name, conn):
    """
    Insère un DataFrame dans une table SQLite.
    Args:
        df (pd.DataFrame): Les données à insérer.
        table_name (str): Nom de la table SQLite.
        conn (sqlite3.Connection): Connexion SQLite.
    """
    df.to_sql(table_name, conn, if_exists="append", index=False)


# Fonction principale pour consolider les fichiers CSV
def consolidate_csv_to_database():
    """
    Consolidation des fichiers CSV dans une base SQLite.
    """
    # Créer une connexion SQLite
    conn = sqlite3.connect(DATABASE_FILE)

    try:
        # Parcourir tous les fichiers CSV
        for file_name in os.listdir(CSV_DIRECTORY):
            if file_name.endswith(".csv"):
                file_path = os.path.join(CSV_DIRECTORY, file_name)

                print(f"Traitement du fichier : {file_name}")

                # Charger et nettoyer le fichier CSV
                df = load_and_clean_csv(file_path)

                # Insérer dans la base de données
                insert_into_database(df, "stocks", conn)

        print("Consolidation terminée avec succès !")

    except Exception as e:
        print(f"Erreur lors de la consolidation : {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    consolidate_csv_to_database()
