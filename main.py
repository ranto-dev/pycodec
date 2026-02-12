import sys
from core.compress import compress_file
from core.decompress import decompress_file

if len(sys.argv) != 4:
    print("Usage:")
    print("  python main.py compress input.txt output.rnt")
    print("  python main.py decompress input.rnt output.txt")
    sys.exit(1)

mode, src, dst = sys.argv[1:]

if mode == "compress":
    o, c = compress_file(src, dst)
    print("Compression terminée")
    print(f"Original   : {o / (1024*1024):.2f} Mo")
    print(f"Compressé  : {c / (1024*1024):.2f} Mo")
    print(f"Taux       : {(1 - c/o)*100:.2f} %")

elif mode == "decompress":
    decompress_file(src, dst)
    print("Décompression terminée")
