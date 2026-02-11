use crate::algorithms::{bwt, huffman, lz77};
use colored::*;
use std::fs;

pub fn run(input: String, output: Option<String>) {
    println!("{}", "✔ RNT-ZIP Decompressor\n".green().bold());

    let output = output.unwrap_or("output.txt".to_string());

    /* =====================
       Lecture fichier .rnt
    ===================== */
    let compressed = fs::read(&input).expect("Cannot read .rnt file");

    /* =====================
       Huffman decode
    ===================== */
    let decoded = huffman::decode(&compressed);

    let mut pos = 0;

    /* =====================
       Lecture index BWT
    ===================== */
    let bwt_index = u64::from_be_bytes(decoded[pos..pos + 8].try_into().unwrap()) as usize;
    pos += 8;

    /* =====================
       Lecture LZ77
    ===================== */
    let mut lz_data = Vec::new();

    while pos + 5 <= decoded.len() {
        let dist = u16::from_be_bytes(decoded[pos..pos + 2].try_into().unwrap()) as usize;
        pos += 2;

        let len = u16::from_be_bytes(decoded[pos..pos + 2].try_into().unwrap()) as usize;
        pos += 2;

        let byte = decoded[pos];
        pos += 1;

        lz_data.push((dist, len, byte));
    }

    /* =====================
       LZ77 inverse
    ===================== */
    let bwt_data = lz77::decompress(&lz_data);

    /* =====================
       BWT inverse
    ===================== */
    let original = bwt::inverse(&bwt_data, bwt_index);

    fs::write(&output, original).expect("Cannot write output file");

    println!("{}", "✔ Decompression completed successfully".green());
}
