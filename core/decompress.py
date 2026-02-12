import pickle
from rich.console import Console
from algorithms.lz77 import decompress as lz77_decompress
from algorithms.huffman import decompress as huff_decompress

console = Console()

def decompress_file(input_path, output_path):
    console.print("[bold yellow]▶ Décompression démarrée[/bold yellow]")

    with open(input_path, "rb") as fin:
        encoded, tree = pickle.load(fin)

    lz_data = pickle.loads(huff_decompress(encoded, tree))
    original = lz77_decompress(lz_data)

    with open(output_path, "wb") as fout:
        fout.write(original)

    console.print("[bold green]✔ Décompression terminée[/bold green]")
