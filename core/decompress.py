import pickle
from rich.console import Console
from algorithms import lz77, mtf, arithmetic, bwt_block

console = Console()

def decompress_file(input_path, output_path):
    console.print("[yellow]Décompression démarrée[/yellow]")

    with open(input_path, "rb") as f:
        blocks = pickle.load(f)

    data = bwt_block.bwt_block_decode(blocks)
    code, freq, length = pickle.loads(data)

    mtf_data = arithmetic.decode(code, freq, length)
    mtf_bytes = mtf.decode(mtf_data)

    lz_data = [(0, 0, b) for b in mtf_bytes]
    text = lz77.decompress(lz_data)

    with open(output_path, "wb") as f:
        f.write(text)

    console.print("[bold green]✔ Décompression terminée[/bold green]")
