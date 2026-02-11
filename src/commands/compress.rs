use colored::*;
use indicatif::{ProgressBar, ProgressStyle};
use std::{fs, time::Duration};
use crate::{algorithms::*, utils::*};

pub fn run(input: String, output: Option<String>) {
    println!("{}", "✔ RNT-ZIP Compressor\n".green().bold());

    let output = output.unwrap_or(format!("{}.rnt", input));
    let size = fs::metadata(&input).unwrap().len();

    if size <= 100 * 1024 * 1024 {
        eprintln!("{}", "✖ File must be strictly larger than 100MB".red());
        return;
    }

    println!("📄 Input   : {}", input.cyan());
    println!("📦 Output  : {}", output.cyan());
    println!("📏 Size    : {:.2} MB", size as f64 / 1024.0 / 1024.0);

    let pb = ProgressBar::new(100);
    pb.set_style(
        ProgressStyle::with_template(
            "{spinner:.green} [{bar:40.cyan/blue}] {percent}% {msg}",
        )
        .unwrap(),
    );

    let text = fs::read_to_string(&input).unwrap();

    pb.set_message("Applying BWT...");
    let (bwt_data, index) = bwt::transform(&text);
    pb.inc(30);
    std::thread::sleep(Duration::from_millis(200));

    pb.set_message("Applying LZ77...");
    let lz = lz77::compress(&bwt_data);
    pb.inc(40);
    std::thread::sleep(Duration::from_millis(200));

    pb.set_message("Encoding...");
    let encoded = huffman::encode(&format!("{:?}|{}", lz, index));
    pb.finish_with_message("Done");

    fs::write(&output, encoded).unwrap();

    println!("{}", "✔ Compression completed successfully".green());
}
