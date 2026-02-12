import hashlib

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

original = sha256("big.txt")
decompressed = sha256("big_out.txt")

print("Intégrité OK :", original == decompressed)
