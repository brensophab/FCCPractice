#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while '_' in display:
    guess = input("Guess a letter: ").lower()
    wrong_guess = 0
#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(display)
        # elif letter is not guess :
        #     wrong_guess += 1
        #     lives_left = 6 - wrong_guess
        #     print(f"Wrong guess! you have {lives_left} lives left") ATTEMTPTED LIVES RESOLUTION
        #     if lives_left < 0:
        #         print(f"Game over! the correct word was {chosen_word} ")
print(f"Congratulations! Your word was {chosen_word}")