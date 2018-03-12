
birthdays = {'Alice': 'April 1',
			'bob': 'Dec 12',
			'Carol': 'March 4'}

while True:
	print('Enter a name: (Blank to quit)')
	name = input()

	if name == '':
		break

	if name in birthdays:
		print (birthdays[name]+' is the birthday of '+name)
	else:
		print ('I do not have the birthday information of '+name)
		print ('What is their birthday ?')
		bday = input()
		birthdays[name] = bday
		print ('birthday database updated !')