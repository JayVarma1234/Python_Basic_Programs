import numpy as np
arr=np.array ([10,20,30,40,501])
print("Original Array:",arr)
print("Array+5:",arr+5)
print("Array*2:",arr*2)
print("Sum of all elements:",arr.sum())

print("Firsyt element:",arr[0])
print("Last element:",arr[-1])

print("Elements from index 1 to 3:", arr[1:4])
print("Elements from start to index 2:",arr[:3])
print("Elements from index2 to end:",arr[2:])
