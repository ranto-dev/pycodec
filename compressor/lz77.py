# compressor/lz77.py
WINDOW_SIZE = 4096


def compress(data: bytes):
    i = 0
    output = []

    while i < len(data):
        best_offset = 0
        best_length = 0

        start = max(0, i - WINDOW_SIZE)
        for j in range(start, i):
            length = 0
            while (i + length < len(data) and
                   data[j + length] == data[i + length]):
                length += 1

            if length > best_length:
                best_length = length
                best_offset = i - j

        next_byte = data[i + best_length] if i + best_length < len(data) else 0
        output.append((best_offset, best_length, next_byte))
        i += best_length + 1

    return output


def decompress(tokens):
    result = bytearray()

    for offset, length, byte in tokens:
        for _ in range(length):
            result.append(result[-offset])
        result.append(byte)

    return bytes(result)
