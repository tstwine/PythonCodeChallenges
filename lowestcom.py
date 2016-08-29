# Find the lowest Common Multiple of two numbers
# I am creating 2 list and I'm looking for the lowest 2 numbers have in common. 

userInput1 = int(input("Please enter a number "))
userInput2 = int(input("Please enter a number "))

listOne = []
listTwo = []

for number in range(1,(userInput1 * userInput2) +1):
	if (userInput1 * number) % userInput1 == 0:
		listOne.append(userInput1 * number)
	if (userInput1 * number) % userInput1 == 0:
		listTwo.append(userInput2 * number)	

print(listOne)
print(listTwo)


for x in listOne:
	if x in listTwo:
		print("LCM is: %s" %x)
		break		






