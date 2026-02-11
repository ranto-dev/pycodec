use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

#[derive(Debug, Clone)]
pub enum Node {
    Leaf {
        byte: u8,
        freq: usize,
    },
    Internal {
        freq: usize,
        left: Box<Node>,
        right: Box<Node>,
    },
}

/* =========================
   Ordre pour BinaryHeap
========================= */
impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        other.freq().cmp(&self.freq())
    }
}

impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Node {
    fn eq(&self, other: &Self) -> bool {
        self.freq() == other.freq()
    }
}

impl Eq for Node {}

impl Node {
    pub fn freq(&self) -> usize {
        match self {
            Node::Leaf { freq, .. } => *freq,
            Node::Internal { freq, .. } => *freq,
        }
    }
}

/* =========================
   Construction de l'arbre
========================= */
fn build_tree(freqs: &HashMap<u8, usize>) -> Node {
    let mut heap = BinaryHeap::new();

    for (&byte, &freq) in freqs {
        heap.push(Node::Leaf { byte, freq });
    }

    while heap.len() > 1 {
        let a = heap.pop().unwrap();
        let b = heap.pop().unwrap();

        heap.push(Node::Internal {
            freq: a.freq() + b.freq(),
            left: Box::new(a),
            right: Box::new(b),
        });
    }

    heap.pop().unwrap()
}

/* =========================
   Génération des codes
========================= */
fn build_codes(node: &Node, prefix: Vec<bool>, table: &mut HashMap<u8, Vec<bool>>) {
    match node {
        Node::Leaf { byte, .. } => {
            table.insert(*byte, prefix);
        }
        Node::Internal { left, right, .. } => {
            let mut l = prefix.clone();
            l.push(false);
            build_codes(left, l, table);

            let mut r = prefix;
            r.push(true);
            build_codes(right, r, table);
        }
    }
}

/* =========================
   Sérialisation arbre
========================= */
fn serialize_tree(node: &Node, out: &mut Vec<u8>) {
    match node {
        Node::Leaf { byte, .. } => {
            out.push(1);
            out.push(*byte);
        }
        Node::Internal { left, right, .. } => {
            out.push(0);
            serialize_tree(left, out);
            serialize_tree(right, out);
        }
    }
}

fn deserialize_tree(data: &[u8], pos: &mut usize) -> Node {
    let flag = data[*pos];
    *pos += 1;

    if flag == 1 {
        let byte = data[*pos];
        *pos += 1;
        Node::Leaf { byte, freq: 0 }
    } else {
        let left = deserialize_tree(data, pos);
        let right = deserialize_tree(data, pos);
        Node::Internal {
            freq: 0,
            left: Box::new(left),
            right: Box::new(right),
        }
    }
}

/* =========================
   ENCODE
========================= */
pub fn encode(input: &[u8]) -> Vec<u8> {
    let mut freqs = HashMap::new();
    for &b in input {
        *freqs.entry(b).or_insert(0) += 1;
    }

    let tree = build_tree(&freqs);

    let mut table = HashMap::new();
    build_codes(&tree, Vec::new(), &mut table);

    let mut bits = Vec::new();
    for &b in input {
        bits.extend(&table[&b]);
    }

    let mut bit_bytes = Vec::new();
    let mut current = 0u8;
    let mut count = 0;

    for bit in bits {
        current <<= 1;
        if bit {
            current |= 1;
        }
        count += 1;

        if count == 8 {
            bit_bytes.push(current);
            current = 0;
            count = 0;
        }
    }

    if count > 0 {
        current <<= 8 - count;
        bit_bytes.push(current);
    }

    let mut header = Vec::new();
    serialize_tree(&tree, &mut header);

    let mut out = Vec::new();
    out.extend((input.len() as u64).to_be_bytes());
    out.extend((header.len() as u32).to_be_bytes());
    out.extend(header);
    out.extend(bit_bytes);

    out
}

/* =========================
   DECODE
========================= */
pub fn decode(data: &[u8]) -> Vec<u8> {
    let mut pos = 0;

    let original_size = u64::from_be_bytes(data[pos..pos + 8].try_into().unwrap()) as usize;
    pos += 8;

    let tree_len = u32::from_be_bytes(data[pos..pos + 4].try_into().unwrap()) as usize;
    pos += 4;

    let tree = deserialize_tree(&data[pos..pos + tree_len], &mut 0);
    pos += tree_len;

    let mut out = Vec::with_capacity(original_size);
    let mut node = &tree;

    for &byte in &data[pos..] {
        for i in (0..8).rev() {
            let bit = (byte >> i) & 1;
            node = match node {
                Node::Internal { left, right, .. } => {
                    if bit == 0 {
                        left
                    } else {
                        right
                    }
                }
                _ => node,
            };

            if let Node::Leaf { byte, .. } = node {
                out.push(*byte);
                node = &tree;
                if out.len() == original_size {
                    return out;
                }
            }
        }
    }

    out
}
