import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

  

class GameStats:
    def __init__(self, use_Rock, use_Paper, use_Scissors, use_Lizard, use_Spock, round, use_Rock2, use_Paper2, use_Scissors2, use_Lizard2, use_Spock2):
        self.rocks_use = use_Rock
        self.paper_use = use_Paper
        self.scissors_use = use_Scissors
        self.lizard_use = use_Lizard
        self.spock_use = use_Spock
        self.round = round
        self.rocks_memory = use_Rock2
        self.paper_memory = use_Paper2
        self.scissors_memory = use_Scissors2
        self.lizard_memory = use_Lizard2
        self.spock_memory = use_Spock2

stater = GameStats(0,0,0,0,0,0,0,0,0,0,0)

def assess_game(user_action, computer_action):
    if user_action == computer_action:
        if user_action == GameAction.Rock:
            stater.rocks_use += 1
        elif user_action == GameAction.Paper:
            stater.paper_use += 1
        elif user_action == GameAction.Scissors:
            stater.scissors_use += 1
        elif user_action == GameAction.Lizard:
            stater.lizard_use += 1
        elif user_action == GameAction.Spock:
            stater.spock_use += 1
        print(f"User and computer picked {user_action.name}. Draw game!")
        
    # You picked Rock
    elif user_action == GameAction.Rock:
        stater.rocks_use += 1
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
        elif computer_action == GameAction.Lizard:
            print("Rock smashes lizard. You won!")
        elif computer_action == GameAction.Paper:
            print("Paper covers rock. You lost!")
        elif computer_action == GameAction.Spock:
            print("Spock vaporizes rock. You lost!")
                
    # You picked Paper
    elif user_action == GameAction.Paper:
        stater.paper_use += 1
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
        elif computer_action == GameAction.Spock:
            print("Paper disproves spock. You won!")
        elif computer_action == GameAction.Scissors:
            print("Scissors cuts paper. You lost!")
        elif computer_action == GameAction.Lizard:
            print("Lizard eats paper. You lost!")
        
    # You picked Scissors
    elif user_action == GameAction.Scissors:
        stater.scissors_use += 1
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
        elif computer_action == GameAction.Spock:
            print("Spock smashes scissors. You lost!")
        elif computer_action == GameAction.Paper:
            print("Scissors cuts paper. You won!")
        elif computer_action == GameAction.Lizard:
            print("Scissors decapitates lizard. You won!")

    # You picked Lizard
    elif user_action == GameAction.Lizard:
        stater.lizard_use += 1
        if computer_action == GameAction.Paper:
            print("Lizard eats paper. You won!")
        elif computer_action == GameAction.Spock:
            print("Lizard poisons spock. You won!")
        elif computer_action == GameAction.Scissors:
            print("Scissors decapitates lizard. You lost!")
        elif computer_action == GameAction.Rock:
            print("Rock smashes lizard. You lost!")
        
    # You picked Spock
    elif user_action == GameAction.Spock:
        stater.spock_use += 1
        if computer_action == GameAction.Rock:
            print("Spock vaporizes rock. You won!")
        elif computer_action == GameAction.Scissors:
            print("Spock smashes scissors. You won!")
        elif computer_action == GameAction.Paper:
            print("Paper disproves spock. You lost!")
        elif computer_action == GameAction.Lizard:
            print("Lizard poisons spock. You lost!")
        
    stater.round += 1
   

def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    if stater.round < 5:
        print(f"Computer picked {computer_action.name}.")
    if stater.round == 5:
        if (stater.rocks_use >= 3) or ((stater.rocks_use == 2) and (((stater.paper_use or stater.spock_use) == 2) or (stater.paper_use == stater.scissors_use == stater.lizard_use == 1) or (stater.paper_use == stater.scissors_use == stater.spock_use == 1) or (stater.scissors_use == stater.lizard_use == stater.spock_use == 1) or (stater.paper_use == stater.lizard_use == stater.spock_use == 1))):
            stater.rocks_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
            stater.lizard_use = 0
            stater.spock_use = 0
                                 
        elif (stater.paper_use >= 3) or ((stater.paper_use == 2) and (((stater.scissors_use or stater.lizard_use) == 2) or (stater.rocks_use == stater.scissors_use == stater.lizard_use == 1) or (stater.rocks_use == stater.scissors_use == stater.spock_use == 1) or (stater.rocks_use == stater.lizard_use == stater.spock_use == 1) or (stater.scissors_use == stater.lizard_use == stater.spock_use == 1))):
            stater.paper_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
            stater.lizard_use = 0
            stater.spock_use = 0
                
        elif (stater.scissors_use >= 3) or ((stater.scissors_use == 2) and (((stater.rocks_use or stater.spock_use) == 2) or (stater.rocks_use == stater.paper_use == stater.lizard_use == 1) or (stater.rocks_use == stater.paper_use == stater.spock_use == 1) or (stater.paper_use == stater.lizard_use == stater.spock_use == 1) or (stater.rocks_use == stater.lizard_use == stater.spock_use == 1))):
            stater.scissors_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
            stater.lizard_use = 0
            stater.spock_use = 0    
            
        elif (stater.lizard_use >= 3) or ((stater.lizard_use == 2) and (((stater.rocks_use or stater.scissors_use) == 2) or (stater.rocks_use == stater.paper_use == stater.scissors_use == 1) or (stater.rocks_use == stater.paper_use == stater.spock_use == 1) or (stater.paper_use == stater.scissors_use == stater.spock_use == 1) or (stater.rocks_use == stater.scissors_use == stater.spock_use == 1))):
            stater.lizard_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
            stater.lizard_use = 0
            stater.spock_use = 0
                
        elif (stater.spock_use >= 3) or ((stater.spock_use == 2) and (((stater.paper_use or stater.lizard_use) == 2) or (stater.rocks_use == stater.paper_use == stater.scissors_use == 1) or (stater.rocks_use == stater.paper_use == stater.lizard_use == 1) or (stater.paper_use == stater.scissors_use == stater.lizard_use == 1) or (stater.rocks_use == stater.scissors_use == stater.lizard_use == 1))):
            stater.spock_memory += 1
            stater.rocks_use = 0
            stater.paper_use = 0
            stater.scissors_use = 0
            stater.lizard_use = 0
            stater.spock_use = 0
        
    if stater.round >= 5 and stater.round < 10:
        if stater.rocks_memory == 1:
            computer_action = GameAction.Paper
            print("Computer picked Paper")
        
        elif stater.paper_memory == 1:
            computer_action = GameAction.Scissors
            print("Computer picked Scissors")
        
        elif stater.scissors_memory == 1:
            computer_action = GameAction.Spock
            print("Computer picked Spock")
            
        elif stater.lizard_memory == 1:
            computer_action = GameAction.Rock
            print("Computer picked Rock")
            
        elif stater.spock_memory == 1:
            computer_action = GameAction.Lizard
            print("Computer picked Lizard")
        else:
            print(f"Computer picked {computer_action.name}.")

    if stater.round == 9:
        if stater.rocks_memory > 0:
            stater.rocks_memory = 0
        elif stater.paper_memory > 0:
            stater.paper_memory = 0
        elif stater.scissors_memory > 0:
            stater.scissors_memory = 0
        elif stater.lizard_memory > 0:
            stater.lizard_memory = 0
        elif stater.spock_memory > 0:
            stater.spock_memory = 0
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
