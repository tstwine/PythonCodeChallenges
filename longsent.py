

userInput = input("Please enter the longest word in the sentence: ")


wordList = userInput.split(" ")
longest_word = ""

for word in wordList:
	if len(word) > len(longest_word):
		longest_word = word

print("The longest word in the sentence is: %s" %longest_word)		



# wordList.len(" ")
# wordList = len.longest_word()
# newWord = ''longest_word(wordList)
# print("longest_word")






# write a program to find the longest word in the sentence inout by the user

# Input- Users entera s sentence
# Process-Program that finds the longest word in sentence
# OUtput- THe longest word in the sentence. 
