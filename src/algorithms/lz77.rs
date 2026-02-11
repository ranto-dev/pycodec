pub type Token = (usize, usize, u8);

/// Compression LZ77 naïve (fonctionne bloc par bloc)
pub fn compress(data: &[u8]) -> Vec<Token> {
    let mut out = Vec::new();
    let mut i = 0;

    while i < data.len() {
        let mut best_len = 0;
        let mut best_dist = 0;

        for j in 0..i {
            let mut len = 0;
            while i + len < data.len() && data[j + len] == data[i + len] {
                len += 1;
            }
            if len > best_len {
                best_len = len;
                best_dist = i - j;
            }
        }

        let next = if i + best_len < data.len() {
            data[i + best_len]
        } else {
            0
        };

        out.push((best_dist, best_len, next));
        i += best_len + 1;
    }

    out
}

/// Décompression LZ77
pub fn decompress(tokens: &Vec<Token>) -> Vec<u8> {
    let mut out = Vec::new();

    for &(dist, len, byte) in tokens {
        if dist > 0 {
            let start = out.len() - dist;
            for i in 0..len {
                out.push(out[start + i]);
            }
        }
        out.push(byte);
    }

    out
}

/// Sérialisation manuelle pour sauvegarder les tokens en bytes
pub fn serialize(tokens: &Vec<Token>) -> Vec<u8> {
    let mut out = Vec::new();
    for &(dist, len, byte) in tokens {
        out.extend_from_slice(&(dist as u32).to_be_bytes());
        out.extend_from_slice(&(len as u32).to_be_bytes());
        out.push(byte);
    }
    out
}

/// Désérialisation pour reconstruire les tokens depuis bytes
pub fn deserialize(data: &[u8]) -> Vec<Token> {
    let mut tokens = Vec::new();
    let mut i = 0;
    while i + 9 <= data.len() {
        let dist = u32::from_be_bytes(data[i..i + 4].try_into().unwrap()) as usize;
        let len = u32::from_be_bytes(data[i + 4..i + 8].try_into().unwrap()) as usize;
        let byte = data[i + 8];
        tokens.push((dist, len, byte));
        i += 9;
    }
    tokens
}
