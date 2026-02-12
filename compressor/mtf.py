def mtf_encode(data):
    symbols = list(range(256))
    result = []
    for char in data:
        idx = symbols.index(char)
        result.append(idx)
        symbols.pop(idx)
        symbols.insert(0, char)
    return result


def mtf_decode(data):
    symbols = list(range(256))
    result = []
    for idx in data:
        char = symbols[idx]
        result.append(char)
        symbols.pop(idx)
        symbols.insert(0, char)
    return bytes(result)
