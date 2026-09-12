#!/usr/bin/env python3
print("Jocelyn Emrich's Test Scores App") # Display student and app name

print("The Test Scores program") # Display a welcome message
print() # Add a blank line for readability
print("Enter 3 test scores") # Tell the user what is expected of them
print("======================") # Display a break across the screen

total_score = 0 # Initialize the variable for accumulating scores
score1 = int(input("Enter test score: ")) # Ask for the first score and save it
total_score += score1 # Add the score to the total count
score2 = int(input("Enter test score: ")) # Ask for another score and save it
total_score += score2 # Add this score to the total count
score3 = int(input("Enter test score: ")) # Ask for the last score
total_score += score3 # Add this score to the total

# Find the average of the scores and simplify the result
average_score = round(total_score / 3)
             
print("======================") # Display a break across the screen
print("Your Scores:", score1, score2, score3) # Display the user's scores
print("Total Score:  ", total_score, # Display the total score
      "\nAverage Score:", average_score) # Show your average score on a new line
print() # Display a blank line for readability
print("Bye") # Say farewell and end


