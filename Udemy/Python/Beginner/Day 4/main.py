#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
#function to randomly roll heads or tails while input is not 'q'
def roll_dice():
    while True:
        user_input = input("Enter 1 to flip the coin, or 'q' to quit.\n")
        if user_input == 'q':
            break
        elif user_input == '1':
            HoT = random.randint(0,1)
            if(HoT == 0):
                print("Heads")
            elif(HoT == 1):
                print("Tails")
roll_dice()






