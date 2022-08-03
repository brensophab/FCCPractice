############### Blackjack Project #####################
from operator import contains
import random
import time
from art import logo

print(logo)
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)
def playAgainPrompt():
     if(input("Would you like to play again?\n") == 'y'):
            game()
     else:
            print("Thanks for playing!")
            exit()
def game():
    computer_cards = random.choices(cards, k=2)
    computer_sum = sum(computer_cards)
    if computer_sum == 21:
        print(f"Computers cards are {computer_cards}, you lose, sorry!")
        playAgainPrompt()
            
    else:

        print(f"Computer's first card is {computer_cards[0]}")

    player_cards = random.choices(cards, k=2)
    player_sum = sum(player_cards)
    if player_sum == 21:
        print(f"Your starting cards are {player_cards}, which adds up to 21, you win!")
        playAgainPrompt()

    
    print(f"Your cards are {player_cards}, current score: {player_sum}\n\n")
    def s_behavior():
        print(f"Your final value of your hand is {player_sum}. Computer is now drawing...")
        computer_sum = sum(computer_cards)
        while(computer_sum < 16):
            
            computer_cards.append(deal_card())
            computer_sum = sum(computer_cards)
            if computer_sum > 21 and 11 in computer_cards:
                computer_sum -= 10
            last_computer_card = computer_cards[len(computer_cards) - 1]
            print(f"Computer draws {last_computer_card}\n")
            time.sleep(1)
            print(f"Computer drew {last_computer_card}. Computer total: {computer_sum}\t Computer cards: {computer_cards} ")
            compare_scores()
    def compare_scores():
        computer_sum = sum(computer_cards)
        player_sum = sum(player_cards)
        if computer_sum > 21: # Computer bust player wins
            last_computer_card = computer_cards[len(computer_cards) - 1]
            print(f"Computer drew {last_computer_card} and busted with a {computer_sum}. Player wins!\n\n Player final deck: {player_cards}\n Player final score: {player_sum}")
            playAgainPrompt()
        elif computer_sum <= 21 and computer_sum > player_sum: # Computer wins no player bust
            print(f"Computer score: {computer_sum}\t Computer cards: {computer_cards}\n\n Player score: {player_sum}\tPlayer cards:: {player_cards}. Computer wins! ")
            playAgainPrompt()
    def h_behavior():

        player_cards.append(deal_card())
        player_sum = sum(player_cards)
        last_card = player_cards[len(player_cards) - 1]
        if player_sum > 21 and 11 in player_cards:
            player_sum -= 10

        if player_sum > 21:
            print(f"You went over 21 (drew a {last_card}). You busted with a {player_sum}!")
            playAgainPrompt()
        if player_sum == 21:
            print("You drew to 21! you win!")
            playAgainPrompt()
        print(f"You drew {last_card}: \tNew value is {player_sum} (Cards on hand: {player_cards}")
        h_or_s = input("(h)it or (s)tay?\n")
        if h_or_s == 'h':
            h_behavior()
        elif h_or_s == 's':
            s_behavior()
    h_or_s = input("(h)it or (s)tay?\n")
    if h_or_s == 'h':
        h_behavior()
    elif h_or_s == 's':
        s_behavior()
    # while h_or_s.lower() == 'h':
        
    #     player_cards.append(deal_card())
    #     player_sum = sum(player_cards)
    #     last_card = player_cards[len(player_cards) - 1]
    #     if player_sum > 21 and 11 in player_cards:
    #         player_sum -= 10

    #     if player_sum > 21:
    #         print(f"You went over 21 (drew a {last_card}). You busted with a {player_sum}!")
    #         playAgainPrompt()
    #     if player_sum == 21:
    #         print("You drew to 21! you win!")
    #         playAgainPrompt()
    #     print(f"You drew {last_card}: \tNew value is {player_sum} (Cards on hand: {player_cards}")
    #     h_or_s = input("(h)it or (s)tay?\n") == 's'
            
    
    # if h_or_s == 's':
    #     print(f"Your final value of your hand is {player_sum}. Computer is now drawing...")
    #     while(computer_sum < 16):
            
    #         computer_cards.append(deal_card())
    #         computer_sum = sum(computer_cards)
    #         if computer_sum > 21 and 11 in computer_cards:
    #             computer_sum -= 10
    #         last_computer_card = computer_cards[len(computer_cards) - 1]
    #         print(f"Computer draws {last_computer_card}\n")
    #         time.sleep(1)
    #         print(f"Computer drew {last_computer_card}. Computer total: {computer_sum}\t Computer cards: {computer_cards} ")
    #     def compare_scores():
    #         if computer_sum > 21: # Computer bust player wins
    #             print(f"Computer drew {last_computer_card} and busted with a {computer_sum}. Player wins!\n\n Player final deck: {player_cards}\n Player final score: {player_sum}")
    #             playAgainPrompt()
    #         elif computer_sum <= 21 and computer_sum > player_sum: # Computer wins no player bust
    #             print(f"Computer score: {computer_sum}\t Computer cards: {computer_cards}\n\n Player score: {player_sum}\tPlayer cards:: {player_cards}. Computer wins! ")
    #             playAgainPrompt()
                
        compare_scores()

           
            
        




game()
##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.