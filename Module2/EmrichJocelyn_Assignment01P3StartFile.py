# Name: Jocelyn Emrich
# Class: INFO 1200
# Section: X01
# Professor: Dr. AlSobeh
# Date: 09/05/2026
# Assignment: Assignment 1
# By submitting this assignment, I declare that the source code contained
# in this assignment was written solely by me unless it was specifically
# provided in the assignment. I attest that no part of this assignment,
# in whole or in part, was directly created by generative AI unless its
# use was explicitly permitted in the assignment instructions. I also
# attest that the work was not obtained from a subscription or solution
# service. I understand that unauthorized copying of source code or use
# of generative AI constitutes an academic-integrity violation and may
# result in a score of zero.

firstName = 'Jocelyn' # Define a variable called "firstName" and put a string in it
print('Hello, my name is ' + firstName) # Print a short introductory message

school = 'Utah Valley University' # Define a variable called "school" and put a string in it
print('I go to ' + school) # Print another short introductory message using the school variable

credits = 3 # Each class is 3 credit hours
classes = 6 # I am taking 6 classes
totalCredits = credits * classes # Calculate the number of credits I am taking this semester

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalCredits) + ' credits') # Show the results

print('I would like to save money by taking this many credits.') # Print a short message explaining why this information is important

maxCredits = 12 # After a student takes 12 credits, all other classes are free
costPerClass = 350 # Each class up to 12 credits costs $350
classFee = 20 # Each class has a required additional fee of $20

totalCostPerSemester = ((totalCredits - maxCredits) / credits) * (costPerClass + classFee) # Calculate how much money I will save by taking more than 12 classes

# Announce the result
print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.')

totalCostPerYear = totalCostPerSemester * 3 # Estimate how much money I will save per year if I take 6 courses each semester

print('That is a wopping $' + str(totalCostPerYear) + ' a year!') # Announce the results

print('This was a very informative and worth while Python assignment!') # Conclude and thank the professor
