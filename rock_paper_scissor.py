# Import the random module to let the computer make a random choice
import random

# Computer randomly picks one of the three options
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# Ask the user for their choice
user_choice = input('Do you want rock, paper, or scissors?')

# Show what the computer picked
print('Computer Choice:', computer_choice)

# Compare choices and determine the outcome
if computer_choice == user_choice:
    print('TIE')   # Same choice = no winner
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')   # Rock beats scissors
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')   # Paper beats rock
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN')   # Scissors beats paper
else:
    print('You lose, computer wins :)')   # Any other case = user loses

