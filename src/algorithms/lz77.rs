pub type LzToken = (usize, usize, u8);

const WINDOW_SIZE: usize = 4096;
const LOOKAHEAD_SIZE: usize = 18;

/* =====================
   Compression LZ77
===================== */
pub fn compress(input: &[u8]) -> Vec<LzToken> {
    let mut i = 0;
    let mut output = Vec::new();

    while i < input.len() {
        let start = if i > WINDOW_SIZE { i - WINDOW_SIZE } else { 0 };
        let mut best_len = 0;
        let mut best_dist = 0;

        for j in start..i {
            let mut length = 0;

            while length < LOOKAHEAD_SIZE
                && i + length < input.len()
                && input[j + length] == input[i + length]
            {
                length += 1;
            }

            if length > best_len {
                best_len = length;
                best_dist = i - j;
            }
        }

        let next_byte = if i + best_len < input.len() {
            input[i + best_len]
        } else {
            0
        };

        output.push((best_dist, best_len, next_byte));
        i += best_len + 1;
    }

    output
}

/* =====================
   Décompression LZ77
===================== */
pub fn decompress(data: &Vec<LzToken>) -> Vec<u8> {
    let mut output = Vec::new();

    for &(dist, len, byte) in data {
        if dist > 0 && len > 0 {
            let start = output.len() - dist;
            for i in 0..len {
                let b = output[start + i];
                output.push(b);
            }
        }
        output.push(byte);
    }

    output
}
