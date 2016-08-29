# def bdayFinder():
while True:	
	try:
		month = int(input("please enter the month in which you were born: "))

		if month >= 1 and month <= 12:
			while True:
				try:
					day = int(input("Please enter the day in which you were born: "))
					if 0 <= day <= 31:
						break
					else:
						print("Invalid entry, Day mest be between 1 & 31")

				except ValueError:
					print("Invalid entry. Input must be a number.")			
		   	break
		else:
				print("Invalid entry. Month must be between 1 & 12")
	except : 
		print("Invalid entry")		
		# break

if day < 10:
	LookUpValue = "%s.0%s" %(month, day)
else:
	LookUpValue = "s.%s" %(month, day)

  	return(float(LookUpValue))
	
	
print(bdayFinder())

    #print(month)
    #print(float(LookUpValue))




