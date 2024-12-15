import sqlite3
import pandas as pd
from fpdf import FPDF
import os

# Chemin de la base SQLite
DATABASE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),'db', 'magasin.db')

# Fonction pour générer un rapport CSV
def generate_csv_report(output_file):
    """
    Génère un rapport CSV des stocks consolidés.

    Args:
        output_file (str): Chemin du fichier de sortie.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)

        # Charger les données depuis la base SQLite
        query = "SELECT * FROM stocks"
        df = pd.read_sql_query(query, conn)

        # Sauvegarder en CSV
        df.to_csv(output_file, index=False)
        print(f"Rapport CSV généré : {output_file}")

    except Exception as e:
        print(f"Erreur lors de la génération du rapport CSV : {e}")

    finally:
        conn.close()

# Fonction pour générer un rapport PDF
def generate_pdf_report(output_file):
    """
    Génère un rapport PDF récapitulatif des stocks.

    Args:
        output_file (str): Chemin du fichier de sortie.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Calculer des résumés
        query_summary = """
        SELECT category, COUNT(*) as total_products, SUM(quantity * unit_price) as total_value
        FROM stocks
        GROUP BY category
        """
        cursor.execute(query_summary)
        summaries = cursor.fetchall()

        # Créer le PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Titre
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Rapport des Stocks", ln=True, align="C")
        pdf.ln(10)

        # Ajouter le résumé par catégorie
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Résumé par catégorie :", ln=True)

        for category, total_products, total_value in summaries:
            pdf.cell(200, 10, txt=f"Catégorie: {category}, Produits: {total_products}, Valeur totale: {total_value:.2f} €", ln=True)

        pdf.ln(10)

        # Ajouter les produits en faible stock
        pdf.cell(200, 10, txt="Produits en faible stock (< 5 unités) :", ln=True)
        query_low_stock = "SELECT product_name, quantity, category FROM stocks WHERE quantity < 5"
        cursor.execute(query_low_stock)
        low_stock_products = cursor.fetchall()

        if low_stock_products:
            for product_name, quantity, category in low_stock_products:
                pdf.cell(200, 10, txt=f"- {product_name} ({category}): {quantity} unités", ln=True)
        else:
            pdf.cell(200, 10, txt="Aucun produit en faible stock.", ln=True)

        # Sauvegarder le PDF
        pdf.output(output_file)
        print(f"Rapport PDF généré : {output_file}")

    except Exception as e:
        print(f"Erreur lors de la génération du rapport PDF : {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    # Générer le rapport CSV
    generate_csv_report("rapport_stocks.csv")

    # Générer le rapport PDF
    generate_pdf_report("rapport_stocks.pdf")
