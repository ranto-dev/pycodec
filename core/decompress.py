import pickle
from compressor.lz77 import decompress_stream
from compressor.arithmetic import ArithmeticDecoder


def decompress_file(input_path, output_path):
    window = b""

    with open(input_path, "rb") as f, open(output_path, "wb") as out:
        while True:
            try:
                code, freq, length = pickle.load(f)

                decoder = ArithmeticDecoder()
                flat = decoder.decode(code, freq, length)

                tokens = []
                for i in range(0, len(flat), 3):
                    tokens.append((flat[i], flat[i+1], flat[i+2]))

                data, window = decompress_stream(tokens, window)
                out.write(data)

            except EOFError:
                break
