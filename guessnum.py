from random import randint

pinNumber = 
print pinNum ber

tries = 1
while tries <= 3:
	userInput = raw_input("Please enter yout pin number: ")
	while userInput.isdigit()  == False:
	    userInput = raw_input("Please enter your pin number: ")

	userInput = int(userInput)
	if userInput == pinNumber:
	   print("You're in")
	   break
	elif tries < 3:
	    print("Try again")
	else:
	    print          
