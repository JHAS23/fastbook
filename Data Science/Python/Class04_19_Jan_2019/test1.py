#~ Syntax:
	#~ def <function_name>(<argumnet1>,<argumnet2>,...):
		#~ <statements>
		#~ .
		#~ .
		#~ return() # This is optional, if not used then "None" will be returned

#~ def Add(a,b):
	#~ c = a+b
	#~ print(c)

#~ def Sub(a,b):
	#~ c = a-b
	#~ print(c)
	#~ return(c)

#~ Add(1,2)
#~ print(Add(1,2))
#~ print(Sub(5,1))
#~ Sub()

#~ def Mul(a,b,*arg): # Arg will hold all the extra parameter which is passed after a and b
	#~ print(a)
	#~ print(b)
	#~ print(arg)
	#~ c = a*b+arg[::-1][0]
	#~ print(c)

#~ Mul(1,2,10,100)

def Add(a,b):
	#~ b = str(b)
	print(a+str(b))

#~ Add("Hi",2)
#~ Add(2,"Hi")
Add(a="Hi",b=2)
Add(b=2,a="Hi")
	