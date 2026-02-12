import os

MIN_SIZE = 100 * 1024 * 1024  # 100 Mo

def check_file_size(path):
    size = os.path.getsize(path)
    if size <= MIN_SIZE:
        raise ValueError(
            f"Fichier refusé : {size / (1024*1024):.2f} Mo. "
            "La taille minimale requise est strictement > 100 Mo."
        )
    return size
