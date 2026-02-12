from collections import Counter
from decimal import Decimal, getcontext

getcontext().prec = 50

def encode(data):
    freq = Counter(data)
    total = sum(freq.values())

    prob = {}
    low = Decimal(0)
    for sym, count in freq.items():
        prob[sym] = (low, low + Decimal(count) / total)
        low = prob[sym][1]

    l, h = Decimal(0), Decimal(1)
    for sym in data:
        r = h - l
        sym_l, sym_h = prob[sym]
        h = l + r * sym_h
        l = l + r * sym_l

    return float((l + h) / 2), freq, len(data)


def decode(code, freq, length):
    total = sum(freq.values())
    prob = {}
    low = Decimal(0)

    for sym, count in freq.items():
        prob[sym] = (low, low + Decimal(count) / total)
        low = prob[sym][1]

    value = Decimal(code)
    out = []

    for _ in range(length):
        for sym, (l, h) in prob.items():
            if l <= value < h:
                out.append(sym)
                value = (value - l) / (h - l)
                break

    return out
