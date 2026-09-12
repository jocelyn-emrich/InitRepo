#!/usr/bin/env python3
print("Jocelyn Emrich's MPG App") # Display student name

print("The Miles Per Gallon program") # Display a welcome message
print() # Print a blank line for readability

# Every answer should be in decimal form, with adequate spacing
# Ask the user how many miles they have driven (the M in MPG)
miles_driven= float(input("Enter miles driven:\t\t"))
# Ask the user how many gallons they used when they drove (the G in MPG)
gallons_used = float(input("Enter gallons of gas used:\t"))
# Ask the user how much each gallon cost
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# Using the given input, calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1) # Simplify the result

# Calculate how much all the gallons cost
total_gas_cost = cost_per_gallon * gallons_used
total_gas_cost = round(total_gas_cost, 1) # Simplify the result

# Calculate how much the user paid to drive each mile
cost_per_mile = total_gas_cost / miles_driven
cost_per_mile = round(cost_per_mile, 1) # Simplify the result

# Every answer should be in text form, with adequate spacing            
print() # Add a blank line to the screen for readability
# Display the results of the first calculation
print("Miles Per Gallon:\t\t" + str(mpg))
# Display the results of the next calculation
print("Total Gas Cost:\t\t\t" + str(total_gas_cost))
# Display the results of the last calculation
print("Cost Per Mile:\t\t\t" + str(cost_per_mile))
print() # Display a blank line for readability
print("Bye") # Show a farewell message and end the program


