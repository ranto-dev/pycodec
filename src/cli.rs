use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(
    name = "RNT-ZIP",
    version = "1.0",
    about = "Modern lossless text compression for large files (>100MB)"
)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Commands,
}

#[derive(Subcommand)]
pub enum Commands {
    Compress { input: String },
    Decompress { input: String },
}
