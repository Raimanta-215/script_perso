import unittest
import os
import pandas as pd
import pdfplumber
from utils.csv_handler import consolidate_csv
from utils.report_file import generate_report


class TestCSVHandler(unittest.TestCase):
    def setUp(self):
        # Préparation des fichiers CSV pour les tests
        os.makedirs("test_data", exist_ok=True)
        pd.DataFrame({
            "nom_produit": ["Produit A", "Produit B"],
            "quantite": [10, 5],
            "prix": [15.0, 20.0],
            "categorie": ["Catégorie 1", "Catégorie 2"]
        }).to_csv("test_data/file1.csv", index=False)

        pd.DataFrame({
            "nom_produit": ["Produit C", "Produit D"],
            "quantite": [8, 12],
            "prix": [25.0, 30.0],
            "categorie": ["Catégorie 1", "Catégorie 3"]
        }).to_csv("test_data/file2.csv", index=False)

    def tearDown(self):
        # Nettoyage après les tests
        for f in os.listdir("test_data"):
            os.remove(os.path.join("test_data", f))
        os.rmdir("test_data")
        if os.path.exists("test_output.csv"):
            os.remove("test_output.csv")

    def test_consolidate_csv(self):
        # Test de consolidation de fichiers CSV
        consolidate_csv("test_data", "test_output.csv")
        self.assertTrue(os.path.exists("test_output.csv"))
        consolidated_df = pd.read_csv("test_output.csv")
        self.assertEqual(len(consolidated_df), 4)  # 2 fichiers, 4 lignes au total
        self.assertIn("nom_produit", consolidated_df.columns)


class TestSearch(unittest.TestCase):
    def setUp(self):
        # Préparation d'un fichier consolidé pour les tests
        self.consolidated_file = "test_consolidated.csv"
        pd.DataFrame({
            "nom_produit": ["Produit A", "Produit B", "Produit C"],
            "quantite": [10, 5, 8],
            "prix": [15.0, 20.0, 25.0],
            "categorie": ["Catégorie 1", "Catégorie 2", "Catégorie 1"]
        }).to_csv(self.consolidated_file, index=False)

    def tearDown(self):
        # Nettoyage après les tests
        if os.path.exists(self.consolidated_file):
            os.remove(self.consolidated_file)

    def test_search_by_category(self):
        # Test recherche par catégorie
        args = type('', (), {})()  # Simule les arguments
        args.product_name = None
        args.category = "Catégorie 1"
        args.price_min = None
        args.price_max = None
        df = pd.read_csv(self.consolidated_file)
        result = df[df['categorie'] == args.category]
        self.assertEqual(len(result), 2)

    def test_search_by_price_range(self):
        # Test réchérché par plage de prix
        args = type('', (), {})()  # Simule les arguments
        args.product_name = None
        args.category = None
        args.price_min = 10
        args.price_max = 20
        df = pd.read_csv(self.consolidated_file)
        result = df[(df['prix'] >= args.price_min) & (df['prix'] <= args.price_max)]
        self.assertEqual(len(result), 2)


class TestReport(unittest.TestCase):
    def setUp(self):
        # Préparation d'un fichier consolidé pour les tests
        self.input_file = "test_consolidated.csv"
        self.output_file = "test_report.pdf"
        pd.DataFrame({
            "nom_produit": ["Produit A", "Produit B", "Produit C"],
            "quantite": [10, 5, 8],
            "prix": [15.0, 20.0, 25.0],
            "categorie": ["Catégorie 1", "Catégorie 2", "Catégorie 1"]
        }).to_csv(self.input_file, index=False)

    def tearDown(self):
        # Nettoyage après les tests
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_report(self):
        # Test de génération de rapport PDF
        generate_report(self.input_file, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        # Lecture et vérification du contenu du fichier PDF
        with pdfplumber.open(self.output_file) as pdf:
            page = pdf.pages[0]
            content = page.extract_text()
            self.assertIn("Rapport Récapitulatif", content)
            self.assertIn("Nombre total de produits : 3", content)
            self.assertIn("Valeur totale des stocks : 450.00", content)

if __name__ == "__main__":
    unittest.main()