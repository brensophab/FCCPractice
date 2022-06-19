import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
 
playerChoice = int(input("What do you choose? (1) for rock, (2) for paper, (3) for scissors\n"))
if playerChoice == 1:
    print(f"Player chose rock\n{rock}")
    
elif playerChoice == 2:
    print(f"Player chose paper\n{paper}")
elif playerChoice == 3:
        print(f"Player chose \n{scissors}")
else:
    print("Not a valid choice")
    
computerChoice = random.randint(1,3)
if computerChoice   == 1:
    print(f"Computer chose rock \n{rock}")
elif computerChoice == 2:
    print(f"Computer chose paper \n {paper}")
else:
    print(f"Computer chose scissors \n {scissors}")

if computerChoice == playerChoice:
    print("It's a Draw!")
elif playerChoice == 1:
    if computerChoice == 2:
        print("Rock loses to paper, Computer Wins!")
    else:
        print("Scissors loses to rock, Player Wins!")
elif playerChoice == 2:
    if computerChoice == 1:
        print("Paper beats rock, player wins!")
    else:
        print("Scissors beats paper, Computer Wins!")
else:
    if computerChoice ==1:
        print("Scissors beats paper, player wins!")
    else:
        print("Rock beats scissors, Computer Wins!")