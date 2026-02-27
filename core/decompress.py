"""
controller pour la decompression
"""

import pickle
import struct
from rich.console import Console
from algorithms.lz77 import decompress as lz77_decompress
from algorithms.huffman import decompress as huff_decompress

console = Console()

def decompress_file(input_path, output_path):
    console.print("[bold yellow]▶ Décompression démarrée[/bold yellow]")

    with open(input_path, "rb") as fin:
        # Licture de la  taille originale des données LZ sérialisées
        original_size = struct.unpack(">Q", fin.read(8))[0]

        # Chargement des données resultat de la compression de Huffman
        encoded, tree = pickle.load(fin)

    # Application de la décompression avec Huffman
    decoded_bytes = huff_decompress(encoded, tree)
    decoded_bytes = decoded_bytes[:original_size]

    # Reconstruction de la structure LZ77
    lz_data = pickle.loads(decoded_bytes)

    # Applicationde la décompression avec LZ77
    original = lz77_decompress(lz_data)

    # Sauvegarder le fichier text output de la décompression
    with open(output_path, "wb") as fout:
        fout.write(original)

    console.print("[bold green] Décompression terminée[/bold green]")