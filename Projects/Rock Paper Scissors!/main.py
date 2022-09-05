import random as rand

def get_choices():
    option = ["rock", "paper", "scissors"]
    player_choice = input("Rock, Paper, or Scissors?: ")
    if(player_choice.lower() not in option):
        print("Invalid choice!")
        return get_choices()
    
    computer_choice = rand.choice(option)
    choices = {
        "player" : player_choice,
        "computer" : computer_choice
    }
        
    return choices

def get_winner(choices):
    print("You chose: {}, computer chose: {}".format(choices["player"], choices["computer"]))
    if(choices["player"] == choices["computer"]):
        return "tie"
    elif(choices["player"] == "rock" and choices["computer"] == "scissors"):
        return "player"
    elif(choices["player"] == "paper" and choices["computer"] == "rock"):
        return "player"
    elif(choices["player"] == "scissors" and choices["computer"] == "paper"):
        return "player"
    else:
        return "computer"

    
winner = get_winner(get_choices())
print("And the winner is... {}!".format(winner))

