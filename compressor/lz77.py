WINDOW_SIZE = 4096


def compress_stream(data, window):
    i = 0
    tokens = []

    while i < len(data):
        best_len = 0
        best_off = 0

        search = window[-WINDOW_SIZE:] + data[:i]

        for j in range(len(search)):
            k = 0
            while (i + k < len(data) and
                   j + k < len(search) and
                   search[j + k] == data[i + k]):
                k += 1
            if k > best_len:
                best_len = k
                best_off = len(search) - j

        next_byte = data[i + best_len] if i + best_len < len(data) else 0
        tokens.append((best_off, best_len, next_byte))

        window += data[i:i + best_len + 1]
        i += best_len + 1

    return tokens, window[-WINDOW_SIZE:]


def decompress_stream(tokens, window):
    out = bytearray()

    for off, length, byte in tokens:
        for _ in range(length):
            val = window[-off]
            out.append(val)
            window += bytes([val])
        out.append(byte)
        window += bytes([byte])

    return bytes(out), window[-WINDOW_SIZE:]
