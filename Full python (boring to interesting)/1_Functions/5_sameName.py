# Local and Global Variable

def spam():
	eggs = 'spam local'
	print (eggs)

def becon():
	eggs = 'becon local'
	print (eggs)
	spam()
	print (eggs)

eggs = 'global'
becon()
print ('global')


# output :

# becon local
# spam local
# becon local
# global
# [Finished in 0.0s]