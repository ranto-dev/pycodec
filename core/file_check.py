"""
programme pour check la taille du fichier entrante (input file)
"""

import os

MIN_SIZE = 100 * 1024 * 1024  # taille de fichier de 100 MB

def check_file_size(path):
    size = os.path.getsize(path)
    if size < MIN_SIZE:
        raise SystemExit(
            f"\nERREUR : votre fichier trop petit, seulement ({size/1024/1024:.2f} Mo)\n"
            "Le programme accepte uniquement des fichiers texte de taille superieur ou égale à 100Mo.\n"
        )
    return size
