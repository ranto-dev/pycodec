use colored::*;
use std::fs;

pub fn run(input: String) {
    let size = fs::metadata(&input).unwrap().len();

    println!("{}", "📦 RNT File Info\n".bold());
    println!("File        : {}", input.cyan());
    println!("Algorithms  : BWT → LZ77 → Huffman");
    println!("Size        : {:.2} MB", size as f64 / 1024.0 / 1024.0);
}
