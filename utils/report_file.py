import os
from fpdf import FPDF
import pandas as pd

def generate_report(input_file, output_file):
    """
    Génère un rapport récapitulatif basé sur un fichier CSV consolidé.

        PRE : - input_dir (str): Dossier contenant les fichiers CSV.
            - output_file (str): Chemin du fichier PDF de sortie.

        POST : création d'un fichier PDF de sortie.

        RAISE : FileNotFoundError : Le fichier CSV n'existe pas.'


    """
    try:
        # Charger les données CSV
        df = pd.read_csv(input_file)
        total_products = len(df)
        total_quantity = df['quantite'].sum()
        total_value = (df['quantite'] * df['prix']).sum()
        avg_price_by_category = df.groupby('categorie')['prix'].mean()

        # Création du PDF
        pdf = FPDF()
        pdf.add_page()

        # Ajouter la police DejaVu Sans (chemin relatif vers le fichier)
        font_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts', 'DejaVuSans.ttf')
        pdf.add_font('DejaVu', '', font_path, uni=True)
        pdf.set_font('DejaVu', '', 12)

        # Contenu du PDF
        pdf.cell(0, 10, "Rapport Récapitulatif", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(0, 10, f"Nombre total de produits : {total_products}", ln=True)
        pdf.cell(0, 10, f"Quantité totale : {total_quantity}", ln=True)
        pdf.cell(0, 10, f"Valeur totale des stocks : {total_value:.2f} €", ln=True)
        pdf.ln(10)
        pdf.cell(0, 10, "Prix moyen par catégorie :", ln=True)
        pdf.ln(5)
        for category, avg_price in avg_price_by_category.items():
            pdf.cell(0, 10, f"  - {category} : {avg_price:.2f} €", ln=True)

        # Sauvegarde du PDF
        pdf.output(output_file)
        print(f"Rapport généré : {output_file}")

    except FileNotFoundError:
        print(f"Le fichier {input_file} est introuvable.")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
