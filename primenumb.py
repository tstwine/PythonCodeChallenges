from random import randint

randNum = str(randint(999999,10000000))
primeNumbers = []
primeTotal = 0

for x in range(len(randNum)):
	divCounter = 0
	for i in range(1,10):
		if (int(randNum[x]) % i == 0):
			divCounter += 1
	
	if divCounter == 1 or divCounter == 2:
		primeNumbers.append(int(randNum[x]))

for x in primeNumbers:
	primeTotal = primeTotal + x

print("The original number was %s.\nThe total of all prime numbers in %s is %s." %(randNum, randNum, primeTotal))