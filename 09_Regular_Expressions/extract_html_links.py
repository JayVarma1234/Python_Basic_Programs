import re

file = open("sample.html", "r")

data = file.read()

links = re.findall(r'href="(.*?)"', data)

print("Extracted Links:")

for link in links:
    print(link)

file.close()