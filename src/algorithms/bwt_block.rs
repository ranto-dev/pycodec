pub fn bwt_block(data: &[u8]) -> (Vec<u8>, usize) {
    let mut rotations: Vec<(usize, &[u8])> = (0..data.len()).map(|i| (i, &data[i..])).collect();

    rotations.sort_by(|a, b| a.1.cmp(b.1));

    let mut result = Vec::with_capacity(data.len());
    let mut index = 0;

    for (i, (pos, _)) in rotations.iter().enumerate() {
        if *pos == 0 {
            index = i;
        }
        let byte = if *pos == 0 {
            data[data.len() - 1]
        } else {
            data[*pos - 1]
        };
        result.push(byte);
    }

    (result, index)
}

pub fn inverse_bwt_block(last: &[u8], index: usize) -> Vec<u8> {
    let mut table: Vec<Vec<u8>> = vec![Vec::new(); last.len()];

    for _ in 0..last.len() {
        for i in 0..last.len() {
            table[i].insert(0, last[i]);
        }
        table.sort();
    }

    table[index].clone()
}
