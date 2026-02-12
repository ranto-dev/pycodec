import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(data):
    heap = [Node(c, f) for c, f in Counter(data).items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, a.freq + b.freq, a, b))
    return heap[0]


def build_codes(node, prefix="", code={}):
    if node.char is not None:
        code[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", code)
        build_codes(node.right, prefix + "1", code)
    return code
