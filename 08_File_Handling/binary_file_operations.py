

with open("example.bin", "wb") as bf:
    data = b"This is binary data"
    bf.write(data)

with open("example.bin", "rb") as bf:
     b_content = bf.read()
     print("Binary File Content:\n", b_content)
