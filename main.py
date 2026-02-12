# main.py
import sys
from core.compress import compress_file
from core.decompress import decompress_file


def usage():
    print("""
Usage:
  Compression   : python main.py compress <input_file> <output_file>
  Décompression : python main.py decompress <input_file> <output_file>
""")
    sys.exit(1)


if len(sys.argv) != 4:
    usage()

mode, input_file, output_file = sys.argv[1:]

if mode == "compress":
    try:
        original, compressed = compress_file(input_file, output_file)
        taux = (1 - compressed / original) * 100

        print("✅ Compression terminée")
        print(f"Taille originale   : {original / (1024*1024):.2f} Mo")
        print(f"Taille compressée  : {compressed / (1024*1024):.2f} Mo")
        print(f"Taux de compression: {taux:.2f} %")

    except ValueError as e:
        print(f"❌ {e}")

elif mode == "decompress":
    decompress_file(input_file, output_file)
    print("✅ Décompression terminée")

else:
    usage()
