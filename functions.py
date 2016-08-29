def menuOptions():
	print("********************************************************************")
	print("Menu Options")
	print("1. Zodiac Description")
	print("2. Zodiac Dates")
	print("3. Zodiac Element")
	print("4. Zodiac Compatibility")
	print("5. Zodiac Ideal Cities")
	print("6. Zodiac Strengths")
	print("7. Zodiac Weaknesses")
	print("8. Zodiac Likes")
	print("9. Zodiac Dislikes")
	print("10. Zodiac Body Parts")
	print("11. Daily Horoscope")
	print("12. Weekly Horoscope")
	print("13. Monthly Horoscope")
	print("14. Yearly Horoscope")
	print("********************************************************************")


def bdayFinder():
    month = int(input("please enter the month in which you were born:  "))
    while month <= 0 or month > 12:
        input("please enter the month in which you were born:  ")
    else:
        day = int(input("please enter the day in which you were born:  "))
        while day <= 0 or day > 31:
            day = input("Your entry, was not valid, Please enter the day in which you were born:  ")

    month = str(month)

    if day < 10:
        day = str(day)
        day = "0" + day
    else:
        day = str(day)

    LookUpValue = month + "." + day

    return float(LookUpValue)

def zodiacFinder(LookUpValue):
    zodiacSign = " "

    if  3.21 <= LookUpValue <= 3.31 or 4.01 <= LookUpValue <=4.19:
        zodiacSign = "Aries"
    elif 4.20 <= LookUpValue <= 4.30 or 5.01 <= LookUpValue <=5.20:
        zodiacSign = "Taurus"
    elif 5.21 <= LookUpValue <= 5.30 or 6.01 <= LookUpValue <=6.20:
        zodiacSign = "Gemini"
    elif 6.21 <= LookUpValue <= 6.30 or 7.01 <= LookUpValue <=7.22:
        zodiacSign = "Cancer"
    elif 7.23 <= LookUpValue <= 7.31 or 8.01 <= LookUpValue <=8.22:
        zodiacSign = "Leo"
    elif 8.23 <= LookUpValue <= 8.31 or 9.01 <= LookUpValue <=9.22:
        zodiacSign = "Virgo"
    elif 9.23 <= LookUpValue <= 9.30 or 10.01 <= LookUpValue <=10.22:
        zodiacSign = "Libra"
    elif 10.23 <= LookUpValue <= 10.31 or 11.01 <= LookUpValue <=11.21:
        zodiacSign = "Scorpio"
    elif 11.22 <= LookUpValue <= 11.30 or 12.01 <= LookUpValue <=12.20:
        zodiacSign = "Sagittarius"
    elif 12.22<= LookUpValue <= 12.31 or 1.01 <= LookUpValue <=1.19:
        zodiacSign = "Capricorn"
    elif 1.20 <= LookUpValue <= 1.31 or 2.01 <= LookUpValue <=2.18:
        zodiacSign = "Aquarius"
    elif 2.19 <= LookUpValue <= 2.29 or 3.01 <= LookUpValue <=3.20:
        zodiacSign = "Pisces"

    return zodiacSign