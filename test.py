import os

originale = os.path.getsize("text.txt")
after_decimpression = os.path.getsize("out.txt")

if originale == after_decimpression:
    print("IDENTIQUE")
    print(f"- Original: {originale}\n- Apres decompression: {after_decimpression}")
else:
    print("DIFFÉRENT")
    print(f"- Original: {originale}\n- Apres decompression: {after_decimpression}")