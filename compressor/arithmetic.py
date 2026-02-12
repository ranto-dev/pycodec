from collections import defaultdict


class ArithmeticEncoder:
    def __init__(self):
        self.low = 0.0
        self.high = 1.0
        self.freq = defaultdict(int)

    def encode(self, data):
        for b in data:
            self.freq[b] += 1

        total = sum(self.freq.values())
        cum = {}
        c = 0.0
        for k, v in self.freq.items():
            cum[k] = (c, c + v / total)
            c += v / total

        for b in data:
            span = self.high - self.low
            l, h = cum[b]
            self.high = self.low + span * h
            self.low = self.low + span * l

        return (self.low + self.high) / 2, dict(self.freq)


class ArithmeticDecoder:
    def decode(self, value, freq, length):
        total = sum(freq.values())
        cum = {}
        c = 0.0
        for k, v in freq.items():
            cum[k] = (c, c + v / total)
            c += v / total

        out = []
        low, high = 0.0, 1.0

        for _ in range(length):
            span = high - low
            for sym, (l, h) in cum.items():
                if low + span * l <= value < low + span * h:
                    out.append(sym)
                    high = low + span * h
                    low = low + span * l
                    break

        return bytes(out)
