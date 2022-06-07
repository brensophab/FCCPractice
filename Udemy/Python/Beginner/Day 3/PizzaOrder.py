print("Welcome to PPD!")
size = input("What size pizza do you want?(\nS = Small\nM = Med\nL = Large\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0

if size == "S":
    if(add_pepperoni == "Y"):
        bill +=2
    bill += 15
elif size == "M":
    bill +=20
    if(add_pepperoni == "Y"):
        bill +=3
elif size == "L":
    if(add_pepperoni == "Y"):
        bill +=3
    bill +=25
if(extra_cheese == "Y"):
    bill+=1

print(f"Your final bill is:\t ${bill}")
