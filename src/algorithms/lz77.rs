pub fn compress(input: &str) -> Vec<(usize, usize, char)> {
    let chars: Vec<char> = input.chars().collect();
    let mut i = 0;
    let mut out = Vec::new();

    while i < chars.len() {
        let mut best = (0, 0);

        for d in 1..=i {
            let mut l = 0;
            while i + l < chars.len() && chars[i + l] == chars[i - d + l] {
                l += 1;
            }
            if l > best.1 {
                best = (d, l);
            }
        }

        let next = chars.get(i + best.1).copied().unwrap_or('\0');
        out.push((best.0, best.1, next));
        i += best.1 + 1;
    }

    out
}

pub fn decompress(data: &Vec<(usize, usize, char)>) -> String {
    let mut out = Vec::new();
    for &(d, l, c) in data {
        if d > 0 {
            let start = out.len() - d;
            for i in 0..l {
                out.push(out[start + i]);
            }
        }
        if c != '\0' {
            out.push(c);
        }
    }
    out.into_iter().collect()
}

pub fn parse(_: &str) -> Vec<(usize, usize, char)> {
    Vec::new()
}
