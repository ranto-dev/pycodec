BLOCK_SIZE = 100_000

def bwt_block_encode(data):
    blocks = []
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i+BLOCK_SIZE]
        block += b'\0'
        rotations = sorted(block[j:] + block[:j] for j in range(len(block)))
        index = rotations.index(block)
        last = bytes(r[-1] for r in rotations)
        blocks.append((index, last))
    return blocks


def bwt_block_decode(blocks):
    out = bytearray()
    for index, last in blocks:
        table = [b"" for _ in last]
        for _ in last:
            table = sorted(last[i:i+1] + table[i] for i in range(len(last)))
        out.extend(table[index][:-1])
    return bytes(out)
