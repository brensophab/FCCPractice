# Number Guessing Game Objectives:
import random
import time
from art import logo
print(logo)
# time.sleep(2)


def clear_terminal():
    for i in range(20):
        print('\n')
    print(logo)


random_number = random.randrange(1, 100)


def correct_guess(random_number):

    print(f"Congratulations! You guessed the correct number({random_number})")
    if input("Would you like to play again?('y' or 'n'\n") == 'y':
        random_number = random.randrange(1, 100)
        clear_terminal()
        game(difficulty=input("Choose a difficulty. Type 'easy' or 'hard'. "))
    else:
        print("Thanks for playing, Goodbye!")
        exit()


def lowerThanNumber():
    print("Too Low. Guess again:\t")


def higherThanNumber():
    print("Too high. Guess again:\t")


def noMoreAttempts():
    print(
        f"Unfortunately, you did not guess the correct number({random_number}).")
    if input("Would you like to try again? 'y' or 'n'") == 'y':
        clear_terminal()
        game(difficulty=input("Choose a difficulty. Type 'easy' or 'hard'. \n"))
    else:
        print("Thanks for playing, Goodbye!")
        exit()


def game(difficulty):
    print("Welcome to the Number Guessing Game!\n I am currently thinking of a number between 1 and 100.\n")
    random_number = random.randrange(1, 100)
    print(random_number)
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    for attempt in range(attempts, 0, -1):
        guess = int(
            input(f"You have {attempt} attempt(s) left to guess the number:\t "))
        if guess == random_number:
            correct_guess(random_number)
        elif guess < random_number:
            lowerThanNumber()
        elif guess > random_number:
            higherThanNumber()
    noMoreAttempts()


game(difficulty=input("Choose a difficulty. Type 'easy' or 'hard'. "))
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
