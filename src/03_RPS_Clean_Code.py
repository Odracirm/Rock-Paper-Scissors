import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2

  

class GameStats:
    def __init__(self, use_Rock, use_Paper, use_Scissors, round, use_Rock2, use_Paper2, use_Scissors2):
        self.rocks_use = use_Rock
        self.paper_use = use_Paper
        self.scissors_use = use_Scissors
        self.round = round
        self.rocks_memory = use_Rock2
        self.paper_memory = use_Paper2
        self.scissors_memory = use_Scissors2

stater = GameStats(0,0,0,0,0,0,0)

def assess_game(user_action, computer_action):
    if user_action == computer_action:
        if user_action == GameAction.Rock:
            stater.rocks_use += 1
        elif user_action == GameAction.Paper:
            stater.paper_use += 1
        elif user_action == GameAction.Scissors:
            stater.scissors_use += 1
        print(f"User and computer picked {user_action.name}. Draw game!")
        
    # You picked Rock
    elif user_action == GameAction.Rock:
        stater.rocks_use += 1
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
        else:
            print("Paper covers rock. You lost!")
                
    # You picked Paper
    elif user_action == GameAction.Paper:
        stater.paper_use += 1
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
        else:
            print("Scissors cuts paper. You lost!")
        
    # You picked Scissors
    elif user_action == GameAction.Scissors:
        stater.scissors_use += 1
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
        else:
            print("Scissors cuts paper. You won!")
        
    stater.round += 1
    

def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    if stater.round < 5:
        print(f"Computer picked {computer_action.name}.")
    if stater.round == 5:
        if (stater.rocks_use >= 3) or (stater.rocks_use == stater.paper_use == 2):
            stater.rocks_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
                        
        elif (stater.paper_use >= 3) or (stater.paper_use == stater.scissors_use == 2):
            stater.paper_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
                
        elif (stater.scissors_use >= 3) or (stater.scissors_use == stater.rocks_use == 2):
            stater.scissors_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
     
                    
    if stater.round >= 5 and stater.round < 10:
        if stater.rocks_memory == 1:
            computer_action = GameAction.Paper
            print("Computer picked Paper")
        elif stater.paper_memory == 1:
            computer_action = GameAction.Scissors
            print("Computer picked Scissors")
        elif stater.scissors_memory == 1:
            computer_action = GameAction.Rock
            print("Computer picked Rock")
    
    if stater.round == 9:
        if stater.rocks_memory > 0:
            stater.rocks_memory = 0
        elif stater.paper_memory > 0:
            stater.paper_memory = 0
        elif stater.scissors_memory > 0:
            stater.scissors_memory = 0
        stater.round = 4
    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break

main()
