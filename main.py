import sys
from ui.banner import show_banner
from core.compress import compress_file
from core.decompress import decompress_file

show_banner()

if len(sys.argv) != 4:
    print("Usage:")
    print("  python main.py compress <input.txt> <output.rnt>")
    print("  python main.py decompress <output.rnt> <restored.txt>")
    sys.exit(1)

mode, inp, out = sys.argv[1:]

if mode == "compress":
    compress_file(inp, out)
elif mode == "decompress":
    decompress_file(inp, out)
else:
    print("❌ Mode inconnu")
