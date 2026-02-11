use colored::*;
use indicatif::{ProgressBar, ProgressStyle};
use std::{fs, time::Duration};
use crate::algorithms::{bwt, huffman, lz77};

pub fn run(input: String, output: Option<String>) {
    println!("{}", "✔ RNT-ZIP Compressor\n".green().bold());

    let output = output.unwrap_or(format!("{}.rnt", input));
    let metadata = fs::metadata(&input).expect("Cannot read file metadata");
    let size = metadata.len();

    if size <= 100 * 1024 * 1024 {
        eprintln!("{}", "✖ File must be strictly larger than 100MB".red());
        return;
    }

    println!("📄 Input   : {}", input.cyan());
    println!("📦 Output  : {}", output.cyan());
    println!("📏 Size    : {:.2} MB", size as f64 / 1024.0 / 1024.0);

    let pb = ProgressBar::new(100);
    pb.set_style(
        ProgressStyle::with_template("{spinner:.green} [{bar:40.cyan/blue}] {percent}% {msg}")
            .unwrap(),
    );

    /* =====================
       Lecture binaire
    ===================== */
    pb.set_message("Reading file...");
    let data = fs::read(&input).expect("Cannot read input file");
    pb.inc(5);
    std::thread::sleep(Duration::from_millis(100));

    /* =====================
       BWT
    ===================== */
    pb.set_message("Applying Burrows-Wheeler Transform...");
    let (bwt_data, bwt_index) = bwt::transform(&data);
    pb.inc(35);
    std::thread::sleep(Duration::from_millis(150));

    /* =====================
       LZ77
    ===================== */
    pb.set_message("Applying LZ77 compression...");
    let lz_data = lz77::compress(&bwt_data);
    pb.inc(30);
    std::thread::sleep(Duration::from_millis(150));

    /* =====================
       Sérialisation LZ77
    ===================== */
    pb.set_message("Serializing LZ77 data...");
    let mut serialized = Vec::new();

    serialized.extend((bwt_index as u64).to_be_bytes());

    for (dist, len, byte) in lz_data {
        serialized.extend((dist as u16).to_be_bytes());
        serialized.extend((len as u16).to_be_bytes());
        serialized.push(byte);
    }

    pb.inc(10);

    /* =====================
       Huffman réel
    ===================== */
    pb.set_message("Encoding with Huffman...");
    let encoded = huffman::encode(&serialized);
    pb.finish_with_message("Compression done");

    fs::write(&output, encoded).expect("Cannot write output file");

    println!("{}", "✔ Compression completed successfully".green());
}
