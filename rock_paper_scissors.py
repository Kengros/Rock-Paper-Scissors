# Rock Paper Scissors Game

""""Goal
		~Ask the player if they pick rock paper or scissors
		~Have the computer chose its move
		~Compare the choices and decide who wins
		~Print the results
	Subgoals
		~Let the player play again
		~Keep a record of the score e.g. (Player: 3 / Computer: 6)"""
new_round = ("yes")
while new_round	== ("yes"):
	computer_score = 0		
	player_score = 0
	game_round = 1
	while game_round < 4:
		print (("Round:") , (game_round))
		print("")
		game_round = game_round + 1
		print ("Pick a move: Rock, Paper or Scissors!")
		command = input()
		print ("")
		if command in ["Rock" , "rock" , "ROCK"]:
			print ("You threw Rock!")
		elif command in ["Paper" , "paper" , "PAPER"]:
			print ("You threw Paper!")
		elif command in ["Scissors" , "scissors" , "SCISSORS"]:
			print ("You threw Scissors!")
		else:
			print (("You can't throw ") + (command) + ("!"))
		print ("and")
		import random
		move = ["Rock", "Paper", "Scissors"]
		computer_move = random.choice(move)
		print (("Opponent threw ") + (computer_move) + ("!"))
		print ("")

		if command in ("Rock", "rock" , "ROCK") and computer_move == "Rock":
			print ("Tie, You Gain No Points")
		elif command in ("Paper" , "paper" , "PAPER") and computer_move == "Paper":
			print ("Tie, You Gain No Points")
		elif command in ("Scissors" , "scissors" , "SCISSORS") and computer_move == "Scissors":
			print ("Tie, You Gain No Points")
		elif command in ("Rock", "rock" , "ROCK") and computer_move == "Paper":
			computer_score = computer_score + 1
			print ("You Lose 1 Point")
		elif command in ("Rock", "rock" , "ROCK") and computer_move == "Scissors":
			player_score = player_score + 1
			print ("You Win 1 Point")
		elif command in ("Paper" , "paper" , "PAPER") and computer_move == "Rock":
			player_score = player_score + 1
			print ("You Win 1 Point")
		elif command in ("Paper" , "paper" , "PAPER") and computer_move == "Scissors":
			computer_score = computer_score + 1
			print ("You Lose 1 Point")
		elif command in ("Scissors" , "scissors" , "SCISSORS") and computer_move == "Rock":
			computer_score = computer_score + 1
			print ("You Lose 1 Point")
		elif command in ("Scissors" , "scissors" , "SCISSORS") and computer_move == "Paper":
			player_score = player_score + 1
			print ("You Win 1 Point")
	print ("")
	print ("RESULTS")
	print (("Player Score:") , (player_score))
	print (("Opponent Score:") , (computer_score))
	if player_score > computer_score:
		print ("You Win!")
	elif computer_score > player_score:
		print ("You Lose!")
	else:
		print ("It's a Draw")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("Do you want to play again")
	print ("yes or no")
	new_round = input()
	yes = "yes"
