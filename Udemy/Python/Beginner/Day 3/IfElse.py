from lib2to3.pgen2.token import LESS


print("Welcome to the roller coaster!\n")
height = int(input("What is your height?\n"))
if height < 120:
    print("You cannot ride the coaster!")
else:
    print("Congrats! you can ride the roller coaster.")

