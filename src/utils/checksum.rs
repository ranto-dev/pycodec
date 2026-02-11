use sha2::{Sha256, Digest};
use std::fs;

pub fn sha256(path: &str) -> Vec<u8> {
    let data = fs::read(path).unwrap();
    let mut h = Sha256::new();
    h.update(data);
    h.finalize().to_vec()
}
