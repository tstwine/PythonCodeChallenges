userInput = input("Please enter a word: ")
letters = len(userInput)
x = 0
repeatedLetters = []

while x < letters:
	if userInput.count(userInput[x]) > 1 and userInput[x] not in repeatedLetters and userInput[x] != " ":
		print("%s is a duplicate letter with that appears %s times in the word %s." %(userInput[x], userInput.count(userInput[x]), userInput))
		repeatedLetters.append(userInput[x])		
	x+= 1