use colored::*;
use std::fs;
use crate::{algorithms::*, utils::*};

pub fn run(input: String, output: Option<String>) {
    println!("{}", "✔ RNT-ZIP Decompressor\n".green().bold());

    let output = output.unwrap_or("output.txt".to_string());
    let data = fs::read(&input).unwrap();

    let decoded = huffman::decode(&data);
    let parts: Vec<&str> = decoded.split('|').collect();

    let lz_data = lz77::parse(parts[0]);
    let index: usize = parts[1].parse().unwrap();

    let bwt_text = lz77::decompress(&lz_data);
    let original = bwt::inverse(&bwt_text, index);

    fs::write(&output, original).unwrap();

    println!("{}", "✔ Decompression completed successfully".green());
}
