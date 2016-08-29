gpa = float(input("Please enter your gpa: "))
SAT = int(input("Please enter your SAT score: "))

if gpa > 1.8:
	if SAT > 900:
		print "Accepted"
	else: 
		print "Rejected"	

elif gpa < 1.8:
	if SAT < 900:
		print "GPA too low"

print "Rejected"		
