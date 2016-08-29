#Write a program that gets an integer from the user. Count from 0 to that number. 
#Use a for loop to do it. 


# userInput = input("Please enter an integer")

# for counter in range(0, 50, 1):
# 	print(counter)

userInput = int(input("Please enter number: "))
for number in range((userInput + 1)):
	print(number)
