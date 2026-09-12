print("Jocelyn Emrich Tip Calculator App") # Display a welcome message
print() # Show an empty line for readability

costOfMeal = float(input("Cost of meal:\t")) # Ask the user how much their meal
                                             # cost
tipPercentage = float(input("Tip percentage:\t")) # Ask how much they want to
                                                  # tip their server
print() # Show a blank line for readability

tipAmount = costOfMeal * (tipPercentage / 100) # Calculate how much money the
                                               # server will receive
tipAmount = round(tipAmount, 2) # Round result to the nearest cent
print(f"Tip amount:\t{tipAmount}") # Show answer to the screen

totalCost = costOfMeal + tipAmount # Find how much the user's meal will cost
                                   # with the tip
totalCost = round(totalCost, 2) # Round result to the nearest cent
print(f"Total amount:\t{totalCost}") # Show answer to the screen
