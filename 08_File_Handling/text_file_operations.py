

with open("example.txt", "w") as f:
    f.write("Hello Students!\nWelcome to Python File Handling.")

with open("example.txt", "r") as f:
    content = f.read()
    print("Text File Content:\n", content)
