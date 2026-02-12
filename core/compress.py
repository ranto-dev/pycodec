import os, pickle
from compressor.bwt import bwt_transform
from compressor.mtf import mtf_encode
from compressor.lz77 import compress as lz77_compress
from .file_utils import check_file_size

def compress_file(input_path, output_path):
    size = check_file_size(input_path)

    with open(input_path, "rb") as f:
        data = f.read()

    bwt_data, index = bwt_transform(data.decode("latin1"))
    mtf = mtf_encode(bwt_data.encode("latin1"))
    lz = lz77_compress(mtf)

    with open(output_path, "wb") as f:
        pickle.dump((index, lz), f)

    return size, os.path.getsize(output_path)
