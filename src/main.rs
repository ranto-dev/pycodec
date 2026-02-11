mod algorithms;
mod cli;
mod commands;
mod utils;

use clap::Parser;
use cli::Cli;

fn main() {
    let cli = Cli::parse();

    match cli.command {
        cli::Commands::Compress { input, output } => {
            commands::compress::run(input, output);
        }
        cli::Commands::Decompress { input, output } => {
            commands::decompress::run(input, output);
        }
        cli::Commands::Info { input } => {
            commands::info::run(input);
        }
    }
}
