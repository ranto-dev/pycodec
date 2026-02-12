import os

MIN_SIZE = 100 * 1024 * 1024  # 100 MB

def check_file_size(path):
    size = os.path.getsize(path)
    if size < MIN_SIZE:
        raise SystemExit(
            f"\n❌ ERREUR : fichier trop petit ({size/1024/1024:.2f} Mo)\n"
            "Le programme accepte uniquement des fichiers texte ≥ 100 Mo.\n"
        )
    return size
