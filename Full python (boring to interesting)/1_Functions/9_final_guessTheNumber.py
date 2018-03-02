# Guess the number game and the final file from functions.

import random

secretNumber = random.randint(1,20)
print ('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
print ('You can only choose upte 6 times')
for guessesTaken in range(1,7):
	print ('Take a guess.')
	guess = int(input())

	if guess < secretNumber:
		print ('Your guess is too low ! (Tried: '+str(guessesTaken)+ ' of 6 times)')
	elif guess > secretNumber:
		print ('Your guess is too high ! (Tried: '+str(guessesTaken)+ ' of 6 times)')
	else:
		break			#This condition is the correct guess !


if guess == secretNumber:
	print ('Good job! You guessed my number in '+ str(guessesTaken) + ' guesses!')
else:
	print ('Nope. The number i was thinking of was '+ str(secretNumber))