 # Write a program that gets an integer from the user and counts from 1 to that number,
 # but uses "*" as a
 # to represent the number. Instead of printing the number, you print the asterik. 

stars = ('*')

userInput = int(input("Please enter number: "))
for number in range(1,(userInput + 1)):
 	print("&" * number)