import random 

rps =['rock', 'paper', 'scissors'] 

options = {"rock":"paper", "paper":"scissors", "scissors":"rock"}

play_game = True

while play_game:

	opponent = random.choice(rps)
	choose = input("\nChoose Rock, Paper, or Scissors: ") 
	player = choose.casefold()

	if player in rps:
		if opponent == options[player]:
			print("\nYour opponent chose " + opponent + "! You lose!\n")
		elif player == opponent:
			print("\nYour opponent chose " + opponent + "! It's a tie!\n")
		else:
			print("\nYour opponent chose " + opponent + "! You won!\n")
		else:
			print("\nPlease choose rock, paper, or scissors.\n")

			play_again = input("Would you like to play again? ")
			play = play_again.casefold()
			if play == 'yes':
				play_game = True
			else:
				play_game = False