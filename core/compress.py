import os, pickle
from rich.console import Console
from ui.progress import progress_bar
from algorithms import lz77, mtf, arithmetic, bwt_block

console = Console()
MIN_SIZE = 100 * 1024 * 1024

def compress_file(input_path, output_path):
    size = os.path.getsize(input_path)
    if size <= MIN_SIZE:
        raise ValueError("Fichier ≤ 100 Mo refusé")

    console.print("[green]Compression démarrée[/green]")

    with open(input_path, "rb") as f:
        data = f.read()

    with progress_bar() as p:
        t = p.add_task("LZ77", total=4)
        lz = lz77.compress(data)
        p.advance(t)

        mtf_data = mtf.encode(bytes(x[2] for x in lz))
        p.advance(t)

        code, freq, length = arithmetic.encode(mtf_data)
        p.advance(t)

        bwt = bwt_block.bwt_block_encode(pickle.dumps((code, freq, length)))
        p.advance(t)

    with open(output_path, "wb") as f:
        pickle.dump(bwt, f)

    console.print("[bold green]✔ Compression terminée[/bold green]")
