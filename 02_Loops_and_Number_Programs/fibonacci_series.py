v = int(input("\n Please enter range of Numbers:"))
a = 0
b = 1

print("Fibonacci Sequence:")
for n in range(v):
    if n <= 1:
        c = n
    else:
        c = a + b
        a = b
        b = c
    print(c)
