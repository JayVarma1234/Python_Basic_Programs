num = int(input("Enter a Number:"))
sum_digit = 0
while num > 0:
    digit=num%10
    sum_digit+=digit
    num=num//10
print("Sum of digits is:",sum_digit)
