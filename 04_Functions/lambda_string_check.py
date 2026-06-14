start_with = lambda s, ch: s.startswith(ch)
text = input("Enter your Name: ")
char = input("Enter your character: ")
print("startwith", char + ":", start_with(text, char))
