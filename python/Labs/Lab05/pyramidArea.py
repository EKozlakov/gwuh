# Author: Eugene Kozlakov
# Date: 9/29/2023
# Description: Caculates the surface area of a pyramid via several different function implementations.

import math

# function definitions
def calcBaseArea(side):
    return side**2

# add your function definition for calcSideArea here
def calcSideArea(side, height): #allsides
    return (2*side)*math.sqrt(((side**2)/4) + (height**2))
    
# add your function definition for prntSurfArea here
def printSurfArea(base_area, side_area):
    print(format(base_area + side_area, ".3f"), end = "")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print("Base surface area of the square pyramid is %f square feet.", format(base_area, ".3f"))

    side_area = calcSideArea(side, height)
    print("Surface area of all four triangular sides is", format(side_area, ".3f"), "sq. ft. Surface area of one side is", format(side_area/4, ".3f"),"sq. ft.")

    print("Total surface area: ", end = "")
    printSurfArea(base_area, side_area)
    print(" sq. ft.")
    # add your function to calculate the side area and assign
    # the result to side_area, then print the result

    # add your function call to print the total surface area


main()
