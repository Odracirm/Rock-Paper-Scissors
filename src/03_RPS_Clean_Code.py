import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameStats:
    def __init__(self, use_Rock, use_Paper, use_Scissors, round):
        self.rocks_use = use_Rock
        self.paper_use = use_Paper
        self.scissors_use = use_Scissors
        self.round = round

stater = GameStats(0,0,0,0)

def assess_game(user_action, computer_action):
    if user_action == computer_action:
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
    print(f"Computer picked {computer_action.name}.")
    for stater.round in range((stater.round % 5 == 0) + 1, stater.round % 5 == 0):
    #if stater.round >= 5:   
        #if stater.round % 5 == 0:
            if stater.rocks_use > stater.paper_use:
                if stater.rocks_use > stater.scissors_use or stater.paper_use == stater.scissors_use:
                    computer_action = GameAction.Paper
            elif stater.paper_use > stater.rocks_use:
                if stater.paper_use > stater.scissors_use or stater.rocks_use == stater.scissors_use:
                    computer_action = GameAction.Scissors
            elif stater.scissors_use > stater.rocks_use:
                if stater.scissors_use > stater.paper_use or stater.rocks_use == stater.paper_use:
                    computer_action = GameAction.Rock
            elif stater.rocks_use == stater.paper_use:
                if stater.scissors_use == 1:
                    computer_action = GameAction(computer_selection)
                    while computer_selection == GameAction.Scissors:
                        computer_action = GameAction(computer_selection)
            elif stater.paper_use == stater.scissors_use:
                if stater.rocks_use == 1:
                    computer_action = GameAction(computer_selection)
                    while computer_selection == GameAction.Rock:
                        computer_action = GameAction(computer_selection)
            elif stater.scissors_use == stater.rocks_use:
                if stater.paper_use == 1:
                    computer_action = GameAction(computer_selection)
                    while computer_selection == GameAction.Paper:
                        computer_action = GameAction(computer_selection)
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
