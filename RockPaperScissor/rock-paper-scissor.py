
import random

player_score=0
computer_score=0

def check_quit():
    if player_choice == "quit":
        print("Thanks for playing!")
        if player_score > computer_score:
            print(f"You won! Final Scores: Player: {player_score}, Computer: {computer_score}")
        elif computer_score > player_score:
            print(f"Computer won! Final Scores: Player: {player_score}, Computer: {computer_score}")
        else:
            print(f"It's a tie! Final Scores: Player: {player_score}, Computer: {computer_score}")
        return True
    return False

while True:
    player_choice=input("Enter your choice: rock/paper/scissors or quit: ").lower()
    if check_quit():
        break
    computer_choice=random.choice(["rock","paper","scissors"])  
    """ random.choice: picks a random item from a list you give it """

    beats={
            "rock":"scissors",
            "paper":"rock",
            "scissors":"paper"
        }
    
    if player_choice not in ["rock","paper","scissors","quit"]:
        print("Invalid choice. Please try again.")
        continue
    
    elif player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")
        check_quit()

        """ key in beats: the key is the player's choice, and the value is what it beats.
            So if the player's choice beats the computer's choice, the player wins."""
    elif beats[player_choice] == computer_choice:
        print(f"{player_choice} beats {computer_choice}. You win!")
        player_score += 1
        check_quit()

    elif beats[computer_choice] == player_choice:
        print(f"{computer_choice} beats {player_choice}. Computer wins!")
        computer_score += 1
        check_quit()

    elif check_quit():
        break
