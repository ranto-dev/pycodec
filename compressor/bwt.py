def bwt_transform(s):
    s += '\0'
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations.sort()
    last_column = ''.join(row[-1] for row in rotations)
    index = rotations.index(s)
    return last_column, index


def bwt_inverse(r, index):
    table = [''] * len(r)
    for _ in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))
    return table[index].rstrip('\0')
