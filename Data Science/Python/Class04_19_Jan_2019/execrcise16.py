# Write a function to count Upper and Lower case letters 
#~ and return them as dictionary

def lower_Upper_Count(inputChar):
	Upper = 0
	Lower = 0
	for Char in inputChar:
		#~ print(Char)
		if ord(Char) >=97 and ord(Char) <=122:
			Lower += 1
		elif ord(Char) >=65 and ord(Char) <=90:
			Upper += 1
	return {"Upper":Upper,"Lower":Lower}
	#~ return {Upper,Lower}
	print("Ok") # Will never be executed
ip = input("Enter some random alphabet...")
print(lower_Upper_Count(ip))