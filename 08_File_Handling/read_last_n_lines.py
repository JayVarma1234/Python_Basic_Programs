#read last n lines of a file
def read_last_n_lines(filename,n):
    with open(filename,"r")  as f:
        lines = f.readlines()
    return lines[-n:]  # get last n lines

#file name and n values
file_name = "example.txt" 
n = int(input("Enter number of last lines of read: "))

#read and print lines
last_lines = read_last_n_lines(file_name, n)
print("\nLast" , n, "lines:")

for line in last_lines:
    print(line.strip())
