

myPets = ['zophie', 'pooka', 'fat-tail']
print('Enter a pet name: ')
name = input()

if name not in myPets:
	print ('I don\'t have a pet named '+name)
else:
	print (name+ ' is my pet.')