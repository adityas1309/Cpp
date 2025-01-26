# Question: Day 27: Calculate the hypotenuse of a right-angled triangle given other two sides.
import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print(f"{hypotenuse(3, 4):.2f}")  # 5.00
