import pickle, os
from core.file_utils import check_file_size, read_chunks
from compressor.lz77 import compress_stream
from compressor.arithmetic import ArithmeticEncoder


def compress_file(input_path, output_path):
    original_size = check_file_size(input_path)
    window = b""

    with open(input_path, "rb") as f, open(output_path, "wb") as out:
        for chunk in read_chunks(f):
            tokens, window = compress_stream(chunk, window)

            flat = []
            for o, l, b in tokens:
                flat.extend([o & 0xFF, l & 0xFF, b])

            encoder = ArithmeticEncoder()
            code, freq = encoder.encode(bytes(flat))

            pickle.dump((code, freq, len(flat)), out)

    return original_size, os.path.getsize(output_path)
