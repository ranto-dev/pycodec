def compress(data, window=2048):
    i = 0
    result = []

    while i < len(data):
        match_len = 0
        match_dist = 0

        for j in range(max(0, i - window), i):
            k = 0
            while i + k < len(data) and data[j + k] == data[i + k]:
                k += 1
            if k > match_len:
                match_len = k
                match_dist = i - j

        next_char = data[i + match_len] if i + match_len < len(data) else 0
        result.append((match_dist, match_len, next_char))
        i += match_len + 1

    return result


def decompress(data):
    out = bytearray()
    for dist, length, char in data:
        for _ in range(length):
            out.append(out[-dist])
        out.append(char)
    return bytes(out)
