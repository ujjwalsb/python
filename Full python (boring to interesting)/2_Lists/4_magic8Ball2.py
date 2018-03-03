# OK, do you remember the last program with the same name where we have done
# it using the functions, now we will try doing here wit the lists.

import random

messages = ['It is certain',
			'It is decidely so',
			'Yes definitely',
			'Reply hazy try again',
			'Ask again later',
			'Concentrate and ask again',
			'My reply is no',
			'Outlook not so good',
			'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])