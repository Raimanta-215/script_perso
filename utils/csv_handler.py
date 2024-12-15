import os
import pandas as pd


def consolidate_csv(input_dir, output_file):
    """
    Consolide plusieurs fichiers CSV depuis un répertoire dans un fichier unique.

    Args:
        input_dir (str): Dossier contenant les fichiers CSV.
        output_file (str): Chemin du fichier CSV de sortie.
    """
    try:
        all_files = [
            os.path.join(input_dir, f)
            for f in os.listdir(input_dir)
            if f.endswith(".csv")
        ]

        if not all_files:
            print("Aucun fichier CSV trouvé dans le dossier spécifié.")
            return

        dataframes = []
        for file in all_files:
            try:
                df = pd.read_csv(file)
                dataframes.append(df)
                print(f"Chargé : {file}")
            except Exception as e:
                print(f"Erreur lors du chargement de {file}: {e}")

        consolidated_df = pd.concat(dataframes, ignore_index=True)
        consolidated_df.to_csv(output_file, index=False)
        print(f"Fichier consolidé sauvegardé dans {output_file}")
    except Exception as e:
        print(f"Erreur lors de la consolidation : {e}")
