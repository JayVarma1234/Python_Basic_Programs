def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number:"))
if n<0:
    print("Number is negetive")
else:
    print(f"factorial of {n} is {fact(n)}")
    
