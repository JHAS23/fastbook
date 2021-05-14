#~ Write a function which takes number as input from 0 to 9
#~ and filter even and odd and return as dictionary 
#~ {Even:<num_list>,Odd:<num_list>}

def filter_Even_Odd(inputNum):
	Even = []
	Odd = []
	
	for num in inputNum:
		if int(num)%2 == 0:
			Even.append(num)
		else:
			Odd.append(num)
	return {"Odd":Odd,"Even":Even}


ip = input("Enter some random number from 0-9...")
print(filter_Even_Odd(ip))