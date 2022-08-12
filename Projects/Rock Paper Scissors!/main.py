def get_choices():
    player_choice = input("Rock, Paper, or Scissors?: ")
    if(player_choice.lower() not in ["rock", "paper", "scissors"]):
        print("Invalid choice!")
        return get_choices()
    
    computer_choice = "paper"
    choices = {
        "player" : player_choice,
        "computer" : computer_choice
    }
    return choices




choices = get_choices()
print(choices)
