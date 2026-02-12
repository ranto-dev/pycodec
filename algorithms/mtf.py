def encode(data):
    table = list(range(256))
    out = []

    for b in data:
        i = table.index(b)
        out.append(i)
        table.pop(i)
        table.insert(0, b)

    return out


def decode(data):
    table = list(range(256))
    out = bytearray()

    for i in data:
        b = table[i]
        out.append(b)
        table.pop(i)
        table.insert(0, b)

    return bytes(out)
