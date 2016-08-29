#Write a program that ask the user for a number and a multiple then display the product of the numbers up 
# to the multiple and including multiple. 

userInput = int(input('Please enter a number: '))
multiple = int(input('Please enter a multiple '))

userInput * multiple

for x in range(1, (multiple+1) ):
	print("%s * %s = %s" % )

numSum = 0

for x in range(1, (userInput+1)):
    numSum += x
    print(numSum)

print numSum    