# core/decompress.py
import pickle
from compressor.lz77 import decompress as lz77_decompress


def decompress_file(input_path, output_path):
    with open(input_path, "rb") as f, open(output_path, "wb") as out:
        while True:
            try:
                tokens = pickle.load(f)
                out.write(lz77_decompress(tokens))
            except EOFError:
                break
