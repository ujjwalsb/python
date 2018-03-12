

def spam():
	global eggs
	eggs = 'spam'	#This is global

def becon():
	eggs = 'becon'	#This is local

def ham():
	print(eggs)		#This is global

eggs = 42			#This is global
spam()
print(eggs)	