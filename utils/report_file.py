import pandas as pd


def generate_report(input_file, output_file):
    """
    Génère un rapport récapitulatif basé sur un fichier CSV consolidé.

    Args:
        input_file (str): Chemin du fichier CSV d'entrée.
        output_file (str): Chemin du fichier de rapport.
    """
    try:
        df = pd.read_csv(input_file)
        total_products = len(df)
        total_quantity = df['quantite'].sum()
        total_value = (df['quantite'] * df['prix']).sum()
        avg_price_by_category = df.groupby('categorie')['prix'].mean()

        with open(output_file, "w") as report:
            report.write(f"Rapport Récapitulatif\n")
            report.write(f"Nombre total de produits : {total_products}\n")
            report.write(f"Quantité totale : {total_quantity}\n")
            report.write(f"Valeur totale des stocks : {total_value:.2f}\n")
            report.write("\nPrix moyen par catégorie :\n")
            report.write(avg_price_by_category.to_string())

        print(f"Rapport généré : {output_file}")
    except FileNotFoundError:
        print(f"Le fichier {input_file} est introuvable.")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
