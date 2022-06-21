#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]



word_choice = random.choice(word_list)
letter_array = word_choice.split()
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("guess a letter!\n").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# if guess in word_choice:
#     print("The letter is in the word!")
# else:
#     print("The letter is not in the word")
#TEACHER SOLUTION:
for letter in word_choice:
    if letter == guess:
        print("Letter is in word!")
    else:
        print("letter is not in the word!")