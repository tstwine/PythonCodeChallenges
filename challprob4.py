sentence = input("Please enter a sentence: ")

wordToChange = input("Which word you like to change? ").lower()

sentList = sentence.lower().split(" ")

while wordToChange not in sentList:
	print('"%s" is not a word in the following sentence:' %wordToChange.lower())
	print("\"%s\"" %sentence)
	wordToChange = input("Please choose a word form the sentence above: ").lower

replaceWord = input("What would you like to change it with? ")

sentList.insert(sentList.index(wordToChange), replaceWord)
sentList.pop(sentList.index(wordToChange))


print(''.join(sentList).capitalize() ) #joinf adds all the items.
#print(sentList.index(wordToChange))

# print(newSent)
	

	