import hashlib


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


print("Original   :", sha256("file.txt"))
print("Restauré   :", sha256("file_out.txt"))
