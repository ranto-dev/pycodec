# compressor/lz77.py
WINDOW_SIZE = 4096

def compress_stream(data, window):
    i = 0
    tokens = []

    while i < len(data):
        best_offset = 0
        best_length = 0

        start = max(0, len(window) - WINDOW_SIZE)
        search = window[start:] + data[:i]

        for j in range(len(search)):
            length = 0
            while (i + length < len(data)
                   and j + length < len(search)
                   and search[j + length] == data[i + length]):
                length += 1

            if length > best_length:
                best_length = length
                best_offset = len(search) - j

        next_byte = data[i + best_length] if i + best_length < len(data) else 0
        tokens.append((best_offset, best_length, next_byte))
        window += data[i:i + best_length + 1]
        i += best_length + 1

    return tokens, window[-WINDOW_SIZE:]


def decompress_stream(tokens, window):
    result = bytearray()

    for offset, length, byte in tokens:
        for _ in range(length):
            result.append(window[-offset])
            window += bytes([window[-offset]])
        result.append(byte)
        window += bytes([byte])

    return bytes(result), window[-WINDOW_SIZE:]
