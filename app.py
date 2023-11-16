import random
# start app
app = True

# Create a dictionary with the options rock, paperm scissors as keys and respective numeric values from 1 to 3
options = {"rock": 1, "paper": 2, "scissors": 3, "quit": 4}

# create a game logic functions that takes the player and computer choices as arguments
def game_logic(player, computer):
    # print the player and computer choices
    print("Player choice: ", player)
    print("Computer choice: ", computer)
    # if the player choice is equal to the computer choice, it is a tie
    if player == computer:
        print("It is a tie")
    # if the player choice is 1 and the computer choice is 2, the player loses
    elif player == 1 and computer == 2:
        print("Player loses")
    # if the player choice is 1 and the computer choice is 3, the player wins
    elif player == 1 and computer == 3:
        print("Player wins")
    # if the player choice is 2 and the computer choice is 1, the player wins
    elif player == 2 and computer == 1:
        print("Player wins")
    # if the player choice is 2 and the computer choice is 3, the player loses
    elif player == 2 and computer == 3:
        print("Player loses")
    # if the player choice is 3 and the computer choice is 1, the player loses
    elif player == 3 and computer == 1:
        print("Player loses")
    # if the player choice is 3 and the computer choice is 2, the player wins
    elif player == 3 and computer == 2:
        print("Player wins")

# Define the game loop
while app:
    # start with the player 1 turn 
    print("Player turn...")
    # ask to select an option
    player1_choice = input("Select an option: rock, paper, scissors, quit: ")
    # check if the option selected is valid
    if player1_choice in options:
        # if it is valid, assign the numeric value to the variable player1_choice
        player1_choice = options[player1_choice]
        # Generate a random number between 1 and 3 for the computer
        computer_choice = random.randint(1, 3)
        # use the game logic function to check the result
        if player1_choice != 4:
            game_logic(player1_choice, computer_choice)
        else:
            app = False
        
    else:
        # if it is not valid, print an error message and start again the loop
        print("Invalid option")
        continue
