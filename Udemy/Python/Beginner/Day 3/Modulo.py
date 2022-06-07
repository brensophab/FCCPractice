

OddOrEven = int(input("Enter an odd or even whole number(0 to exit) \n"))
while OddOrEven != 0:
    if (OddOrEven % 2) == 0:
        print(f"Your number is Even:\t" )
        OddOrEven = int(input("Enter an odd or even whole number(0 to exit) \n"))
    else:
        print(f"Your number is Odd:\t") 
        OddOrEven = int(input("Enter an odd or even whole number(0 to exit) \n"))
