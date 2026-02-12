import os, pickle
from rich.console import Console
from ui.progress import progress_bar
from core.file_check import check_file_size
from algorithms.lz77 import compress as lz77_compress
from algorithms.huffman import compress as huff_compress

console = Console()
CHUNK_SIZE = 1024 * 1024  # 1 MB

def compress_file(input_path, output_path):
    original_size = check_file_size(input_path)
    console.print("[bold green]▶ Compression démarrée[/bold green]")

    with open(input_path, "rb") as fin:
        data = fin.read()

    with progress_bar() as progress:
        task = progress.add_task("Compression", total=100)

        lz = lz77_compress(data)
        progress.update(task, advance=50)

        encoded, tree = huff_compress(pickle.dumps(lz))
        progress.update(task, advance=50)

    with open(output_path, "wb") as fout:
        pickle.dump((encoded, tree), fout)

    compressed_size = os.path.getsize(output_path)
    ratio = (1 - compressed_size / original_size) * 100

    console.print("\n[bold cyan]📊 Statistiques de compression[/bold cyan]")
    console.print(f"• Taille initiale   : {original_size/1024/1024:.2f} Mo")
    console.print(f"• Taille compressée : {compressed_size/1024/1024:.2f} Mo")
    console.print(f"• Taux compression  : {ratio:.2f} %")

    console.print("[bold green]✔ Compression terminée[/bold green]")
