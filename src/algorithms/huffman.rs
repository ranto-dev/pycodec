pub fn encode(input: &str) -> Vec<u8> {
    input.as_bytes().to_vec()
}

pub fn decode(data: &[u8]) -> String {
    String::from_utf8_lossy(data).to_string()
}
