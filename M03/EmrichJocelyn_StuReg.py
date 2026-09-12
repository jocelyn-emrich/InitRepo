# Name: Jocelyn Emrich
# Class: INFO 1200
# Section: X01
# Professor: AlSobeh
# Date: 09/12/2026
# Assignment #: 2 (M03 Project)
# By submitting this assignment, I declare that the source code contained in
# this assignment was written solely by me, unless specifically provided in the
# assignment. I attest that no part of this assignment, in whole or in part, was
# directly created by Generative AI, unless explicitly stated in the assignment
# instructions, nor obtained from a subscription service. I understand that
# copying any source code, in whole or in part, unless specifically provided in
# the assignment, constitutes cheating, and that I will receive a zero on this
# project if I am found in violation of this policy.

print("Jocelyn Emrich Registration App") # Display a welcome message
print() # Display a blank line for readability

firstName = input("First name:\t") # Ask what the user's first name is
lastName = input("Last name:\t") # Ask what the user's last name is
birthYear = input("Birth year:\t") # Ask what year the user was born

print() # Show a blank line for readability
print(f"Welcome {firstName} {lastName}") # Welcome the user by name
print("Your registration is complete") # Show that the program worked correctly

tempPassword = firstName + "*" + birthYear # Create a temporary password from
                                             # the above information
print(f"Your temporary password is: {tempPassword}") # Tell the user what their
                                                     # temporary password is
