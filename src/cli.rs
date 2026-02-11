use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(
    name = "rnt",
    version = "1.0",
    about = "RNT-ZIP — Modern lossless text compression for large files (>100MB)"
)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Commands,
}

#[derive(Subcommand)]
pub enum Commands {
    /// Compress a text file into .rnt
    Compress {
        input: String,
        #[arg(short, long)]
        output: Option<String>,
    },

    /// Decompress a .rnt file
    Decompress {
        input: String,
        #[arg(short, long)]
        output: Option<String>,
    },

    /// Show information about a .rnt file
    Info { input: String },
}
