import re

def count_word(filename, word):
    with open(filename,"r") as f:
        text = f.read()
    matches = re.findall(rf'\b{word}\b',text,re.IGNORECASE)
    return len(matches)

file_name ="example.txt"
word = input("Enter word to search:")

count = count_word(file_name, word)
print(f"'{word}' found {count} times in the file.")
