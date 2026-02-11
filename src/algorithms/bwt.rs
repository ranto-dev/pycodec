pub fn transform(input: &str) -> (String, usize) {
    let mut rotations = Vec::new();
    let n = input.len();

    for i in 0..n {
        rotations.push(format!("{}{}", &input[i..], &input[..i]));
    }

    rotations.sort();
    let last = rotations.iter().map(|r| r.chars().last().unwrap()).collect();
    let index = rotations.iter().position(|r| r == input).unwrap();

    (last, index)
}

pub fn inverse(last: &str, index: usize) -> String {
    let n = last.len();
    let mut table = vec![String::new(); n];

    for _ in 0..n {
        for i in 0..n {
            table[i] = format!("{}{}", last.chars().nth(i).unwrap(), table[i]);
        }
        table.sort();
    }
    table[index].clone()
}
