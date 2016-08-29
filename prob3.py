# Write a program that gives the user only three tries to guess the correct pin of the accont.

tries = 1
#count = 1 #start off the count
pin = 1201
userInput = int( input("Please enter your pin:") )


while userInput != pin and tries <= 3:
	userInput = int( input("Please re-enter your pin:") )
	if userInput == pin:
		tries += 1
		break
	else:
		tries += 1

if tries >= 3:
	print("You have exceeded your max tries.")		
else:
	print("Welcome person!!")	


