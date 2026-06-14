import time

start = time.time()

total = 0
for i in range(1, 1000001):
    total += i
end = time.time()

print("Execution time:", end - start, "seconds")
