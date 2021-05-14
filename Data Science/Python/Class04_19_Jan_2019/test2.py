#~ Syntax:
	#~ def <function_name>(<argumnet1>,<argumnet2>,...):
		#~ <statements>
		#~ .
		#~ .
		#~ return() # This is optional, if not used then "None" will be returned

def Add(a,b,**kwarg):
	print(a)
	print(b)
	print(kwarg)
	c = a+b+kwarg["t"]
	print(c)

def Sub(a,b,*arg,**kwarg):
	print(a)
	print(b)
	print(arg)
	print(kwarg)
	c = a+b+arg[0]+kwarg["t"]
	print(c)

#~ Add(1,2)
#~ Sub(1,2,10,30,e=3,t=4)
Sub(1,2,10,e=3,t=4,30)
