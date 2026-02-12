import pickle
from compressor.bwt import bwt_inverse
from compressor.mtf import mtf_decode
from compressor.lz77 import decompress as lz77_decompress

def decompress_file(input_path, output_path):
    with open(input_path, "rb") as f:
        index, lz = pickle.load(f)

    mtf = lz77_decompress(lz)
    bwt = mtf_decode(mtf).decode("latin1")
    text = bwt_inverse(bwt, index)

    with open(output_path, "wb") as f:
        f.write(text.encode("latin1"))
