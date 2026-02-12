def compress(data, window_size=4096):
    i = 0
    result = []

    while i < len(data):
        best_len = 0
        best_dist = 0

        for j in range(max(0, i - window_size), i):
            k = 0
            while i + k < len(data) and data[j + k] == data[i + k]:
                k += 1
            if k > best_len:
                best_len = k
                best_dist = i - j

        next_byte = data[i + best_len] if i + best_len < len(data) else 0
        result.append((best_dist, best_len, next_byte))
        i += best_len + 1

    return result


def decompress(data):
    out = bytearray()
    for dist, length, byte in data:
        for _ in range(length):
            out.append(out[-dist])
        out.append(byte)
    return bytes(out)
