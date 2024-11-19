# The following line imports the choice function from Python's random module, which is used to randomly select an item from a list.
from random import randint
import winsound

# The following line creates a list of play options name tim
tim = ["Stone", "Paper", "Scissors"]

# The following line set player and computer scores to 0
player_score = 0
computer_score = 0
# This next line tracks player win streak.
win_streak = 0

# The following line starts an infinite loop until player enters stop.
while True:
    # The following line assign a random play to the computer
    computer = tim[randint(0, 2)]

    # The following line asks the player for their move by typing their input choices given.
    player = input("What's your play? Type: Stone, Paper, or Scissors? ('stop' to quit game) ")

    # The following line checks if the player wants to quit by typing stop.
    # if so, the game loop breaks and ends the game.
    if player.lower() == 'stop':
        break

    # The following lines checks the outcome of each game.
    if player == computer:
        print("It's a tie!")
        win_streak = 0 # This line resets win streak when there is a tie.

    elif player == "Stone":
        if computer == "Scissors":
            print("Nice choice, you win!", player, "smashes", computer)
            player_score += 1
            winsound.Beep(500, 300)  # Frequency, duration in milliseconds
            winsound.Beep(600, 400)  # Frequency, duration in milliseconds
            winsound.Beep(700, 500)
            win_streak += 1 # This line adds 1 to players winning streak total.
        else:
            print("Sorry, you lose!", computer, "covers", player)
            computer_score += 1
            winsound.Beep(300, 500)  # Frequency, duration in milliseconds
            winsound.Beep(200, 1000)  # Frequency, duration in milliseconds
            win_streak = 0  # This line resets win streak when player loses.

    elif player == "Paper":
        if computer == "Stone":
            print("Good play, you win!", player, "covers", computer)
            player_score += 1
            winsound.Beep(500, 300) # Frequency, duration in milliseconds
            winsound.Beep(600, 400)
            winsound.Beep(700, 500)
            win_streak += 1

        else:
            print("Better luck next time, you lose!", computer, "cuts", player)
            computer_score += 1
            winsound.Beep(300, 500)  # Frequency, duration in milliseconds
            winsound.Beep(200, 1000)  # Frequency, duration in milliseconds
            win_streak = 0 # This line resets win streak when player loses.

    elif player == "Scissors":
        if computer == "Paper":
            print("Excellent play, you win!", player, "cuts", computer)
            player_score += 1
            winsound.Beep(500, 300)  # Frequency, duration in milliseconds
            winsound.Beep(600, 400)
            winsound.Beep(700, 500)
            win_streak += 1

        else:
            print("You lose...", computer, "smashes", player)
            computer_score += 1
            winsound.Beep(300, 500)  # Frequency, duration in milliseconds
            winsound.Beep(200, 1000)  # Frequency, duration in milliseconds
            win_streak = 0

    # The following line prints if the player enters an invalid play.
    else:
        print("That's not a valid play. Please check your spelling!")

    # This next line checks if player has won 3 in a row.
    if win_streak == 3:
        print("You're on fire!")
        winsound.Beep(400, 500)  # Frequency, duration in milliseconds
        winsound.Beep(500, 600)  # Frequency, duration in milliseconds
        winsound.Beep(600, 700)  # Frequency, duration in milliseconds
        winsound.Beep(700, 800)  # Frequency, duration in milliseconds
        winsound.Beep(900, 900)  # Frequency, duration in milliseconds
        win_streak = 0  # Reset streak counts after outputting message.

    # The following line displays the current scores.
    print(f"Score - Player: {player_score}, Computer: {computer_score}")

# The following line displays the final scores after the player quits.
print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
print("Thanks for playing! Come back soon!")