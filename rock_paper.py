player1 = int(input("Player 1 enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n"))
player2 = int(input("Player 2 enter your choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n"))

def compare(p1, p2):
	if p1 == p2:
		return ("The game is a tie")
	elif p1 == 1:
		if p2 == 3:
			return("Rock wins")
		else:
			return("Paper wins")
	elif p1 == 3:
		if p2 == 2:
			return("Scissors wins")
		else:
			return("Rock wins")
	elif p1 == 2:
		if p2 == 1:
			return("paper wins")
		else:
			return("Scissors wins")
	else:
		return ("You have entered an invalid choice")
print (compare(player1, player2))
