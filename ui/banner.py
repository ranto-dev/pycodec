from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def show_banner():
    title = Text("PYCODEC", style="bold bright_cyan", justify="center")
    subtitle = Text(
        "Lossless Text Compression Tool\n"
        "LZ77 • Huffman Coding",
        style="white",
        justify="center"
    )
    footer = Text(
        "Academic Project • Large Files Only (≥ 100 MB)",
        style="dim cyan",
        justify="center"
    )

    panel = Panel(
        Align.center(title + "\n\n" + subtitle + "\n\n" + footer),
        border_style="bright_blue",
        padding=(1, 6),
        title="[bold green]CLI Application[/bold green]",
        subtitle="Data Compression"
    )

    console.print(panel)
