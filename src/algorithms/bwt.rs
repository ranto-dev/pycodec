pub fn transform(input: &[u8]) -> (Vec<u8>, usize) {
    let n = input.len();
    let mut rotations: Vec<Vec<u8>> = Vec::with_capacity(n);

    for i in 0..n {
        let mut rot = Vec::with_capacity(n);
        rot.extend_from_slice(&input[i..]);
        rot.extend_from_slice(&input[..i]);
        rotations.push(rot);
    }

    rotations.sort();

    let mut last_column = Vec::with_capacity(n);
    let mut index = 0;

    for (i, rot) in rotations.iter().enumerate() {
        last_column.push(rot[n - 1]);
        if rot == input {
            index = i;
        }
    }

    (last_column, index)
}

pub fn inverse(last: &[u8], index: usize) -> Vec<u8> {
    let n = last.len();
    let mut table = vec![Vec::<u8>::new(); n];

    for _ in 0..n {
        for i in 0..n {
            table[i].insert(0, last[i]);
        }
        table.sort();
    }

    table[index].clone()
}
