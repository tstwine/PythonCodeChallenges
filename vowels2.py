# Ronesha's example

fullName = input("What's your full name? ").lower()
nameSplit = fullName.split(" ")
vowels = ["a", "e", "i", "o", "u"]

for name in nameSplit:
	vowelCounter = 0
	for letter in range(len(name)):
		if name[letter] in vowels:
			vowelCounter += 1
	print("There are %s vowels in \"%s\"" %(vowelCounter, name.title()))




userInput = input("What is your full name? ")
nameList = userInput.split()
#nameList = ["Thomas", "Twine"] 
vowels = ["a", "e", "i", "o", "u"]

for name in nameList: 
	vowelCounter = 0
	for letter in range(len(name)): #(for the _ number of iteration of 5=Thomas, length of name), the length o
		if name[letter] in vowels: #(letter at the _ numbr index position, you can index a string)
			vowelCounter += 1

print("There are %s vowels in \"%s\"" %(vowelCounter, name.title()))
