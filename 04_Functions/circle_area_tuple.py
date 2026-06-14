import math

#function to calculate area and circumference
def circle_details(r):
    area = math.pi * r * r
    circ = 2 * math.pi * r
    return (area,circ)

#Accept radius from user
radius = float(input("Enter radius:"))

#call function
result = circle_details(radius)

#Display result
print("Area:",result[0])
print("Circumference:",result[1])
