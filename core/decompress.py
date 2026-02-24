import pickle
import struct
from rich.console import Console
from algorithms.lz77 import decompress as lz77_decompress
from algorithms.huffman import decompress as huff_decompress

console = Console()


def decompress_file(input_path, output_path):
    console.print("[bold yellow]▶ Décompression démarrée[/bold yellow]")

    with open(input_path, "rb") as fin:
        # 🔹 Lire taille originale des données LZ sérialisées
        original_size = struct.unpack(">Q", fin.read(8))[0]

        # 🔹 Charger données Huffman
        encoded, tree = pickle.load(fin)

    # 🔹 Décompression Huffman
    decoded_bytes = huff_decompress(encoded, tree)

    # 🔥 Suppression padding
    decoded_bytes = decoded_bytes[:original_size]

    # 🔹 Reconstruction structure LZ77
    lz_data = pickle.loads(decoded_bytes)

    # 🔹 Décompression LZ77
    original = lz77_decompress(lz_data)

    # 🔹 Écriture fichier restauré
    with open(output_path, "wb") as fout:
        fout.write(original)

    console.print("[bold green]✔ Décompression terminée[/bold green]")