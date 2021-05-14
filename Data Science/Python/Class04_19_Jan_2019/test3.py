#~ Syntax:
	#~ def <function_name>(<argumnet1>,<argumnet2>,...):
		#~ <statements>
		#~ .
		#~ .
		#~ return() # This is optional, if not used then "None" will be returned

def Add(a,b):
	"""
	This is an Addition function and it takes int arg a and b
	and o/p will be an int
	"""
	print(a+b)
	
print(Add.__doc__)
#~ help(Add.__doc__)
#~ Add(1,2)
