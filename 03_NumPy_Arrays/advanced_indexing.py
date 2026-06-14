import numpy as np
arr = np.array ([[10,20,30],
                [40,50,60],
                [70,80,90]])
print("Element at (1,2):", arr[1,2])
print("Sliced (rows 0-1):",arr[0:2, :])
print("Sliced (col 1):", arr[:,1])
rows= [0,2]
cols= [1,2]
print("Advanced index (0,1)&(2,2):", arr[rows, cols])
print("Element>50:", arr[arr>50])
