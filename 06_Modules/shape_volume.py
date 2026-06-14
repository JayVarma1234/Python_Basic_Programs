#first file geometry.py
import math
def squareArea(side):
    return side * side

def circleArea(radius):
    return math.pi * radius * radius
#second file 
from geometry import squareArea, circleArea

def pointyShapeVolume(x, y, squareBase):
    if squareBase:
        base_area = squareArea(x)
    else:
        base_area = circleArea(x)
    volume = (1/3) * base_area * y
    return volume

if __name__ == "__main__":
    print("Volume (Square base):", pointyShapeVolume(4, 9,True))
    print("Volume (Circular base):", pointyShapeVolume(3, 5,False))
