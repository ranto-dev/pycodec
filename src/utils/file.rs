use std::fs;

pub fn size(path: &str) -> u64 {
    fs::metadata(path).unwrap().len()
}
