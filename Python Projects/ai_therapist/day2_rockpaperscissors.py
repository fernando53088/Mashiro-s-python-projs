import random # REMINDER: coding is all you have you better not quit

options = ('Rock', 'Paper', 'Scissors')
ai = random.choice(options)
game = ('Rock', 'Paper', 'Scissors')
ai_points = 0
game_points = 0
 
while True: 
 game= str(input("Rock, paper, scissors...\n")) # input becomes game, game is input.
 print(f"Player:{game}")
 print(f"AI:{ai}")
 if game.lower() == ai.lower():
     print("It's a tie")
 elif game.lower() == "rock" and ai.lower() == "paper":
    print("You lose")
    ai_points += 0
 elif game.lower() == "paper" and ai.lower() == "scissors":
    print("You lose")
    ai_points += 0
 elif game.lower() == "scissors" and ai.lower() == "rock":
    print("You lose")
    ai_points += 0
 else:
    print("You win")
    game_points += 0
 if ai_points == 3:
    print("AI wins")
    break 
 if game_points == 3:
    print("You win")
    break 