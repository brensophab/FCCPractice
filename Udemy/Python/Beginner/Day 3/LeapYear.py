year = int(input("What year do you want to check?(0 to exit)"))
while(year != 0):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print("Is a leap year")
            else:
                print("Not a leap year")
        print("Is a leap year")        
    else:
        print("Not a leap year")
    year = int(input("What year do you want to check?(0 to exit)"))
