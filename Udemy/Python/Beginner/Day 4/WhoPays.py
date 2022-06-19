#Method given to split a string
import random


names_string = input("Give me everybody's names, separated by a comma.(EX: Angela, Ben, Jenny, Michael, Chloe) ")
names = names_string.split(", ")

chosen = names[random.randint(0, len(names) - 1)]
print(f"{chosen} is going to buy the meal today")
