import pickle
import struct
import os
from rich.console import Console
from algorithms.lz77 import compress as lz77_compress
from algorithms.huffman import compress as huff_compress

console = Console()

# MIN_SIZE = 100 * 1024 * 1024  # 100 MB
MIN_SIZE = 1024

def compress_file(input_path, output_path):
    console.print("[bold yellow]▶ Compression démarrée[/bold yellow]")

    # 🔹 Vérification taille minimale
    file_size = os.path.getsize(input_path)
    if file_size < MIN_SIZE:
        console.print(
            f"[bold red]❌ Erreur : Le fichier doit être ≥ 100 MB (actuel: {file_size / (1024*1024):.2f} MB)[/bold red]"
        )
        return

    # 🔹 Lecture fichier original
    with open(input_path, "rb") as fin:
        original_data = fin.read()

    # 🔹 Compression LZ77
    console.print("[cyan]⚙ LZ77...[/cyan]")
    lz_data = lz77_compress(original_data)

    # 🔹 Sérialisation LZ77
    lz_serialized = pickle.dumps(lz_data)

    # 🔹 Compression Huffman
    console.print("[cyan]⚙ Huffman...[/cyan]")
    encoded, tree = huff_compress(lz_serialized)

    # 🔹 Écriture fichier compressé
    with open(output_path, "wb") as fout:
        # 8 bytes → taille exacte des données LZ sérialisées
        fout.write(struct.pack(">Q", len(lz_serialized)))

        # Sauvegarde données Huffman
        pickle.dump((encoded, tree), fout)

    # 🔹 Statistiques
    compressed_size = os.path.getsize(output_path)
    rate = (1 - (compressed_size / file_size)) * 100

    console.print("[bold green]✔ Compression terminée[/bold green]")
    console.print(f"📏 Taille initiale      : {file_size / (1024*1024):.2f} MB")
    console.print(f"📦 Taille compressée   : {compressed_size / (1024*1024):.2f} MB")
    console.print(f"📉 Taux de compression : {rate:.2f} %")