# core/compress.py
import pickle
from compressor.lz77 import compress as lz77_compress
from core.file_utils import check_file_size, read_chunks
import os


def compress_file(input_path, output_path):
    original_size = check_file_size(input_path)

    with open(input_path, "rb") as f, open(output_path, "wb") as out:
        for chunk in read_chunks(f):
            tokens = lz77_compress(chunk)
            pickle.dump(tokens, out)

    compressed_size = os.path.getsize(output_path)
    return original_size, compressed_size
