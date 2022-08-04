############DEBUGGING#####################
#DEBUGGING PRACTICE
# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
#The above bug occurs because the range function assumes 1 as index 0, so the loop will stop when i == 19.

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
#The above bug occurs because the randint chooses a random index from 1 to 6, but the index should be from 0-5.

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#This bug occurs because there is no condition for when year == 1994, and will not be evaluated.

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")
# #This error occurs because the input is evaluating numbers as str rather than int, as well as not an fstring.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words) 
# The above bug occurs because word_per_page was evaluated using an equality operator, rather than assigning it a value, use '=' instead of '=='

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])