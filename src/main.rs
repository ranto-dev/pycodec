mod cli;
mod commands;
mod algorithms;

use cli::Cli;
use clap::Parser;

fn main() {
    let cli = Cli::parse();

    match cli.command {
        cli::Commands::Compress { input } => {
            commands::compress::run(&input);
        }
        cli::Commands::Decompress { input } => {
            commands::decompress::run(&input);
        }
    }
}
