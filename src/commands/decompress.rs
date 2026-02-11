use std::{
    fs::File,
    io::{Read, Write},
};

use crate::algorithms::{bwt_block::inverse_bwt_block, huffman, lz77};

pub fn run(path: &str) {
    let mut input = File::open(path).unwrap();
    let mut output = File::create(path.replace(".rnt", "")).unwrap();

    loop {
        let mut index_buf = [0u8; 4];
        if input.read_exact(&mut index_buf).is_err() {
            break;
        }
        let index = u32::from_be_bytes(index_buf) as usize;

        let mut size_buf = [0u8; 4];
        input.read_exact(&mut size_buf).unwrap();
        let size = u32::from_be_bytes(size_buf) as usize;

        let mut encoded = vec![0u8; size];
        input.read_exact(&mut encoded).unwrap();

        let lz_bytes = huffman::decode(&encoded);
        let lz = lz77::deserialize(&lz_bytes);
        let bwt = lz77::decompress(&lz);
        let original = inverse_bwt_block(&bwt, index);

        output.write_all(&original).unwrap();
    }
}
