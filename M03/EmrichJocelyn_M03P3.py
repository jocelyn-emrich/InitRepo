#!/usr/bin/env python3
print("Jocelyn Emrich's Rectangle App") # Show the student and app name
print() # Show a blank line for readability

print("The Rectangle program") # Display a welcome message
print() # Print a blank line for readability

# Every answer should be nicely printed and formatted as a number
length = int(input("Please enter the length:\t")) # Request length of rectangle
width = int(input("Please enter the width:\t\t")) # Request width of rectangle

area = length * width # Calculate the area of the rectangle
perimeter = length + width + length + width # Calculate perimeter of rectangle
            
# Every answer should be nicely printed and formatted as text
print() # Print a blank line for readability
print("Area:\t\t" + str(area)) # Display the area of rectangle
print("Perimeter:\t" + str(perimeter)) # Display the perimeter of rectangle
print() # Display a blank line for readability
print("Thanks for using this program!") # Show farewell message and end
