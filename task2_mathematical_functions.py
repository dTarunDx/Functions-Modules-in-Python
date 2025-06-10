#Import Module for math
import math
from math import radians, degrees

# Define a function named calculate
def calculate(x):
    if x > 0 :
        print ("The square root of", x, "is", math.sqrt(x))
        print ("The log of", x, "is", math.log(x))
        print ("The sin of", x, "degrees is", math.sin(x))
    elif x <= 0:#if the user enters a negative number or 0
        print("The log and square root of 0 or a negative number is undefined.")
        x = float(input("Enter any number: "))
        calculate(x)

# Input from user
x = float(input("Enter any number: "))

# Calling the function:calculate(x)
calculate(x)