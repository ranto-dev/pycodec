use indicatif::{ProgressBar, ProgressStyle};
use std::{
    fs::File,
    io::{Read, Write},
};

use crate::algorithms::{bwt_block::bwt_block, huffman, lz77};

const BLOCK_SIZE: usize = 1_000_000;

pub fn run(path: &str) {
    let mut file = File::open(path).expect("Cannot open file");
    let size = file.metadata().unwrap().len();

    if size <= 100 * 1024 * 1024 {
        panic!("File must be strictly larger than 100MB");
    }

    let pb = ProgressBar::new(size);
    pb.set_style(ProgressStyle::with_template("{spinner} {bytes}/{total_bytes} {msg}").unwrap());

    let mut output = File::create(format!("{}.rnt", path)).unwrap();

    loop {
        let mut buffer = vec![0u8; BLOCK_SIZE];
        let read = file.read(&mut buffer).unwrap();
        if read == 0 {
            break;
        }
        buffer.truncate(read);

        pb.set_message("BWT block");
        let (bwt, index) = bwt_block(&buffer);

        pb.set_message("LZ77");
        let lz = lz77::compress(&bwt);
        let lz_bytes = lz77::serialize(&lz);

        pb.set_message("Huffman");
        let encoded = huffman::encode(&lz_bytes);

        output.write_all(&(index as u32).to_be_bytes()).unwrap();
        output
            .write_all(&(encoded.len() as u32).to_be_bytes())
            .unwrap();
        output.write_all(&encoded).unwrap();

        pb.inc(read as u64);
    }

    pb.finish_with_message("Compression complete");
}
