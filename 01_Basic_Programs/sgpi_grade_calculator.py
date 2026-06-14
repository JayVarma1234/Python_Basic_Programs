sgpi = float(input("Enter your sgpi:"))
if 9.00 <= sgpi <= 10.00:
    print("Grade:O")
elif 8.00 <= sgpi <= 9.00:
    print("Grade:A+")
elif 7.00 <= sgpi <= 8.00:
    print("Grade:A")
elif 6.00 <= sgpi <= 7.00:
    print("Grade:B+")
elif 5.50 <= sgpi <= 6.00:
    print("Grade:B")
elif 5.00 <= sgpi <= 5.50:
    print("Grade:C")
elif 4.00 <= sgpi <= 5.00:
    print("Grade:P")
elif sgpi < 4.00:
    print("Fail")
else:
    print("Invalid sgpi entered")
