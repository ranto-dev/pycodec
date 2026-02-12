def compress(data, window_size=4096):
    i = 0
    output = []
    while i < len(data):
        match = (0, 0, data[i])
        for j in range(max(0, i - window_size), i):
            length = 0
            while i + length < len(data) and data[j + length] == data[i + length]:
                length += 1
            if length > match[1]:
                match = (i - j, length, data[i + length] if i + length < len(data) else 0)
        output.append(match)
        i += match[1] + 1
    return output


def decompress(data):
    result = bytearray()
    for offset, length, char in data:
        for _ in range(length):
            result.append(result[-offset])
        result.append(char)
    return bytes(result)
