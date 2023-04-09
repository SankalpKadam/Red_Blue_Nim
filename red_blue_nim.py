#References - https://www.geeksforgeeks.org/python-infinity/ , https://www.youtube.com/watch?v=zp3VMe0Jpf8
import argparse

# Each node in tree is generated using this class.
class State():
    def __init__(self,red_stones, blue_stones,action):
        self.red_stones = red_stones
        self.blue_stones = blue_stones
        self.action = action
    def return_data(self):
        return f"Red: {self.red_stones}, Blue: {self.blue_stones}, parent_state: {self.parent_state}, action : {self.action}"

#Utility function to calculate values of terminal states.
def utility_function(state, caller):
    if caller == "max":
        return 2*state.red_stones + 3*state.blue_stones
    else:
        return -(2*state.red_stones + 3*state.blue_stones)

#Generates successors for current state.
def possible_actions(state):
    possible_states = list()
    take_from_red = State(state.red_stones-1,state.blue_stones,"Take from red")
    possible_states.append(take_from_red)
    take_from_blue = State(state.red_stones,state.blue_stones-1,"Take from blue")
    possible_states.append(take_from_blue)
    return possible_states

#Maximizes the value for result of performing actions on current state.
def alpha_beta_decision(state):
    alpha = float('-inf')
    beta = float('inf')
    successors_of_current_State = possible_actions(state)
    current_winning = float('-inf')
    winning_state = successors_of_current_State[0]
    for s in successors_of_current_State:
        v = Min_Value(s,alpha,beta)
        alpha = v
        if v > current_winning:
            current_winning = v
            winning_state = s
    return winning_state

#Max node in minmax.
def Max_Value(state,alpha,beta):
    #Check for terminal state
    if state.red_stones == 0 or state.blue_stones == 0:
        return utility_function(state,"max")
    v = float('-inf') #Assign infinity value to v
    #find successors of s
    successors_of_given_state = possible_actions(state)
    for s in successors_of_given_state:
        current_value = Min_Value(s,alpha,beta)
        if v < current_value:
            v = current_value
        if current_value >= beta:
            return v
        if current_value > alpha:
            alpha = current_value
    return v

#Min node in minmax.
def Min_Value(state,alpha,beta):
    #Check for terminal state
    if state.red_stones == 0 or state.blue_stones == 0:
        return utility_function(state,"min")
    v = float('inf') #Assign infinity value to v
    #find successors of s
    successors_of_given_state = possible_actions(state)
    for s in successors_of_given_state:
        current_value = Max_Value(s,alpha,beta)
        if current_value < v:
            v = current_value
        if current_value <= alpha:
            return v
        if current_value < beta:
            beta = current_value
    return v

#Perform minmax for current game state.
def Do_Min_Max(current_state):
    move = alpha_beta_decision(current_state)
    return move.action

#Perform computer move after deciding using minmax.
def Make_Computer_Move(current_state, move_to_be_done):
    if move_to_be_done == "Take from red":
        print("Computer took a red ball")
        current_state.red_stones -= 1
    elif move_to_be_done == "Take from blue":
        print("Computer took a blue ball")
        current_state.blue_stones -= 1
    print(f"\nCurrent state is: Red Balls {current_state.red_stones} Blue Balls {current_state.blue_stones}\n")
    return current_state

#Check if game is over.
def Check_If_Game_Over(game_state, player):
    if (game_state.red_stones == 0 or game_state.blue_stones == 0) and player == "Human":
        print(f"Computer won with score : {game_state.red_stones*2 + game_state.blue_stones*3}")
        return True
    elif (game_state.red_stones == 0 or game_state.blue_stones == 0) and player == "Computer":
        print(f"Human Wins with score : {game_state.red_stones*2 + game_state.blue_stones*3}")
        return True
    else:
        return False

#Get move from human.
def Get_Human_Move():
    human_move = input("Enter color to pick either red or blue ball: ")
    return human_move.lower()

#Perform move given by human.
def Perform_Human_Move(current_state, move_to_be_done):
    if move_to_be_done == "red":
        current_state.red_stones -= 1
        print(f"\nCurrent state is: Red Balls {current_state.red_stones} Blue Balls {current_state.blue_stones}\n")
        return current_state
    elif move_to_be_done == "blue":
        current_state.blue_stones -= 1
        print(f"\nCurrent state is: Red Balls {current_state.red_stones} Blue Balls {current_state.blue_stones}\n")
        return current_state
    else:
        move_to_be_done = input("Enter a valid color: ")
        return Perform_Human_Move(current_state, move_to_be_done)
        
#Executed if computer is the first player.
def computer_plays_first(initial_state):
    updated_game_state_by_human = None
    while True:
        move_selected_by_computer = Do_Min_Max(initial_state)
        if updated_game_state_by_human:
            updated_game_state_by_computer = Make_Computer_Move(updated_game_state_by_human, move_selected_by_computer)
        else:
            updated_game_state_by_computer = Make_Computer_Move(initial_state, move_selected_by_computer)

        if Check_If_Game_Over(updated_game_state_by_computer, "Computer"):
            break
        move_selected_by_human = Get_Human_Move()
        updated_game_state_by_human = Perform_Human_Move(updated_game_state_by_computer, move_selected_by_human)
        if Check_If_Game_Over(updated_game_state_by_human, "Human"):
            break
        print("--------------------------------------------")

#Executed if human is the first player.
def human_plays_first(initial_state):
    updated_game_state_by_computer=None
    while True:
        move_selected_by_human = Get_Human_Move()
        if updated_game_state_by_computer:
            updated_game_state_by_human = Perform_Human_Move(updated_game_state_by_computer, move_selected_by_human)
        else:
            updated_game_state_by_human=Perform_Human_Move(initial_state, move_selected_by_human)
        if Check_If_Game_Over(updated_game_state_by_human, "Human"):
            break
        move_selected_by_computer = Do_Min_Max(initial_state)
        updated_game_state_by_computer = Make_Computer_Move(updated_game_state_by_human, move_selected_by_computer)
        if Check_If_Game_Over(updated_game_state_by_computer, "Computer"):
            break
        print("---------------------------------------------")


if __name__ == "__main__":
    #Creating a parser for command line arguments and specifying all the different options that can be used.
    parser = argparse.ArgumentParser(prog="red_blue_nim.py", description="Uses MinMax with alpha-beta pruning to play red-blue nim game.")
    parser.add_argument("red_stones", type=int)
    parser.add_argument("blue_stones", type=int)
    parser.add_argument("-p", "--player", default="computer",
                        help="Use this option to specify who plays first")
    commandline_args = parser.parse_args()
    initial_state=State(commandline_args.red_stones,commandline_args.blue_stones,None)
    print("---------------------------------------------")
    print(f"Initial State is : Red {initial_state.red_stones} Blue {initial_state.blue_stones}\n")
    if commandline_args.player.lower() == "computer":
        computer_plays_first(initial_state)
    else:
        human_plays_first(initial_state)
