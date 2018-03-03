# This programs is same as the first one (1_allMyCats.py) instead it uses the list.

catNames = []
while True:
	print ('Enter the name of cat '+str(len(catNames)+1)+' (Or enter nothing to stop.):')
	name = input()
	if name == '':
		break

	catNames = catNames + [name]	#list concatination

print('The cat names are: ')
for name in catNames:
	print(' '+name)