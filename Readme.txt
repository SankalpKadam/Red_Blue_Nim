Name - Sankalp Kadam 
UTA ID - 1002072319
Programming Language - Python 3.10.10

Structuring of code - 
Major functions in code :
    1] alpha_beta_decision - Performs minmax with alpha beta pruning to determine the best possible move for given game state.
    2] computer_plays_first/human_plays_first - Determines who plays first depending on the argument provided by the user.
    3] Check_If_Game_Over - Checks if after making a move the game ends or not.
    4] utility_function - Gives utility values for terminal states.
    5] __main__ - Takes arguments provided in the command line invocation to determine red and blue stones, first player. Calls necessary function depending on the parameters provided.
How to pass arguments through command line invocation?
    The program uses argparse to parse all the provided arguments in the command line.
    The program needs 2 necessary parameters i.e red and blue marbles so pass them as it is.
    For optional argument i.e first_player use the "-p" flag.
    A sample invocation through command line where you want to start the game with 5 red and 4 blue marbles and human plays first is : python3 red_blue_nim.py 5 4 -p human


How to RUN the code - 

    1] The code requires "argparse" package so make sure its installed in the machine. If not then use 'pip install argparse' to install the package.
    2] I would suggest you ensure that the python 3.10.10 is installed on your machine. Atleast make sure you have python 3.8 or above.
    3] The code needs 2 necessary parameters i.e no. of red and blue marbles and 1 optional argument i.e first_player. Optinal arguments can be provided using '-p' flag while invocation through command line.
    4] Use the following command to run the program - python3 red_blue_nim.py <red_marbles> <blue_marbles> -p <first_player>
        For Ex. - To start the game with 5 red and 4 blue marbles where human plays first, the command would look like this : python3 red_blue_nim.py 5 4 -p human
    5] Make sure you use the "-p" flag to specify who will be playing first, or else the computer will play first by default.