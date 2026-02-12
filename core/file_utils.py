# core/file_utils.py
import os

MIN_SIZE = 100 * 1024 * 1024  # 100 Mo
CHUNK_SIZE = 1024 * 1024     # 1 Mo


def check_file_size(path):
    size = os.path.getsize(path)
    if size <= MIN_SIZE:
        raise ValueError(
            f"Fichier refusé : {size / (1024*1024):.2f} Mo. "
            "La taille minimale doit être strictement > 100 Mo."
        )
    return size


def read_chunks(file):
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        yield chunk
