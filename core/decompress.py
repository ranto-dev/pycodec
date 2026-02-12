# core/decompress.py
import pickle
from compressor.lz77 import decompress_stream


def decompress_file(input_path, output_path):
    window = b""

    with open(input_path, "rb") as f, open(output_path, "wb") as out:
        while True:
            try:
                tokens = pickle.load(f)
                data, window = decompress_stream(tokens, window)
                out.write(data)
            except EOFError:
                break
