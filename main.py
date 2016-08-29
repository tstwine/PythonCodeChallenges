import functions
from zodiac import *
from horoscopes import * 


print("Welcome to the Zodiac app!")
print("********************************************************************")

play = "yes"
while play == "yes" or play == "y":
    knowLoop = True
    while knowLoop == True:
        knowZodiac = raw_input("Do you know your zodiac sign? ").lower()
        if knowZodiac == "yes" or knowZodiac == "y":
            zodiacSign = raw_input("What is your zodiac sign? ").capitalize()
            while zodiacSign not in signs.keys():
                print("Try again. Please check your spelling.")
                zodiacSign = raw_input("What is your zodiac sign? ").capitalize()
            break
        elif knowZodiac == "no" or knowZodiac == "n":
            zodiacSign = functions.zodiacFinder(functions.bdayFinder())

            while zodiacSign == " ":
                print("Zodiac Sign not found")
                zodiacSign = functions.zodiacFinder(functions.bdayFinder())
                print(zodiacSign)

            zodiacSign = zodiacSign.capitalize()
            print("You are a %s!" %zodiacSign)
            break
        else:
            print("You have entered an invalid response. ")

    more = "yes"
    while more == "yes" or more == "y":
        functions.menuOptions()
        print("")
        userInput = raw_input("Please enter a menu option by the corresponding number: ")
        while userInput.isdigit()== False:
            userInput = raw_input("Please enter a menu option by the corresponding number: ")

        userInput = int(userInput)

        if userInput == 1:
            print(signs[zodiacSign]["summary"])
        elif userInput == 2:
            print("%s - %s" %(signs[zodiacSign]["dates"]["first_day"], signs[zodiacSign]["dates"]["last_day"]))
        elif userInput == 3:
            print(signs[zodiacSign]["element-type"])
        elif userInput == 4:
            print(signs[zodiacSign]["compatibility"])
        elif userInput == 5:
            print(signs[zodiacSign]["ideal-cities"])
        elif userInput == 6:
            print(signs[zodiacSign]["strengths"])
        elif userInput == 7:
            print(signs[zodiacSign]["weaknesses"])
        elif userInput == 8:
            print(signs[zodiacSign]["likes"])
        elif userInput == 9:
            print(signs[zodiacSign]["dislikes"])
        elif userInput == 10:
            print(signs[zodiacSign]["body-representation"])
        elif userInput == 11:
            print(horoscopes[zodiacSign]["daily"])
        elif userInput == 12:
            print(horoscopes[zodiacSign]["weekly"])
        elif userInput == 13:
            print(horoscopes[zodiacSign]["monthly"])
        elif userInput == 14:
            print(horoscopes[zodiacSign]["yearly"])
        else:
            print("Invalid input.")
            more = "yes"
        more = raw_input("Interested in knowing more about this sign? ").lower()
        print("")

    play = raw_input("Do you want to learn about another sign? ").lower()
