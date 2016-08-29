

# <---- STring Methods ------>
string = "This is a string"


#".count() returns the number of a given character in a string. Method takes one argument and is case sensitive. This returns an int.
#Take one argument and is case sensitive.

# ".index() returns the index of a character within a string. takes one argument is case sensisitve. Returns an int."
print(string.count("t"))

print(string.index("s"))

# Returns string as all caps"
print(string.upper())

#Returns string with forst letter of each word
print(string.title())

print(string.capitalize())

print(string.swapcase())

#string1 = 
#string2 = 

#print('.'.join(string2))

filename = "my_sample_file.jpg"

newFilename = ''.join((filename.split(".")) [0].split("_"))
print(newFilename)

print(filename)
print(filename.replace('_', ''))

#print(''.join((newFileName))

#print(string.split)()

#Operations on Lists
NewList = ["one", "two", "three", "four"]

NewList.append("five")
print(NewList)

SecList = ["six", "seven", "eight"]

NewList.extend(SecList)
print(NewList)

ThirdList = NewList + SecList
print(ThirdList)

NewList.insert(0, "zero")
print(NewList)

NewList.remove("six")
print(NewList)

NewList.pop(5)
print(NewList)

NewList.sort()
print(NewList)

NumList = [1,2,3,4]


NewList.sort()
NumList.sort()

print(NewList)
print(NumList)

NewList.reverse()
NumList.reverse()

print(NewList)
print(NumList)

# <--- Dictionary Methods ---->

NewDiction = {"One": 1, "two": 2, "three": 3, "four":4}
NewDiction['five'] = 5 #append to a dictionary
print(NewDiction)

# print(NewDiction['six'])
# if NewDiction ['six'] = True
# 	print("The value is true.")

# NewDiction ['six'].
# print	


# print(NewDiction.keys())
# print(NewDiction.values)())
# print(NewDiction)

NewDiction.popitem()
print(NewDiction)

NewDiction = ['one']
print(NewDiction.get("one")
#(NewDiction['one']
#print(NewDiction)


