from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def show_banner():
    title = Text("TEXTZIP", style="bold bright_cyan", justify="center")
    desc = Text(
        "Lossless Text Compression CLI\n"
        "LZ77 • MTF • Arithmetic Coding • Block BWT",
        style="white",
        justify="center"
    )

    panel = Panel(
        Align.center(title + "\n\n" + desc),
        border_style="cyan",
        padding=(1, 6),
        title="[bold green]Compression Tool[/bold green]",
        subtitle="Academic Project"
    )
    console.print(panel)
