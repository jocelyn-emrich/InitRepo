print("Jocelyn Emrich Pay Check Calculator App") # Display a welcome message
print() # Show a blank line for readability

hoursWorked = float(input("Hours worked:\t")) # Ask the user how many hours they
                                              # worked
payRate = float(input("Hourly pay rate: ")) # Ask the user how much they're paid
                                            # per hour
print() # Show a blank line for readability

grossPay = hoursWorked * payRate # Calculate payment before tax
print(f"Gross Pay:\t{grossPay}") # Show the result

taxRate = 18 # All employees are taxed on 18% of their pay
print(f"Tax Rate:\t{taxRate}%") # Tell the user about this
taxAmount = grossPay * (taxRate / 100) # Calculate how much tax is owed on the
                                       # user's pay
print(f"Tax Amount:\t{taxAmount}") # Show the result
print() # Add an extra line for readability

takeHomePay = grossPay - taxAmount # Calculate how much money the user has left
takeHomePay = round(takeHomePay, 2) # The result must rounded to the nearest
                                    # cent
print(f"Take Home Pay:\t{takeHomePay}") # Show the answer
