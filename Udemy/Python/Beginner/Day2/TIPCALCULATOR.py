#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What was the total bill?\n"))

tipPercent = float(input("What percentage(%) tip would you like to give?\n"))

peopleSplit = int(input("How many people would you like to split the bill with?\n"))

perPersonSplit = (bill / peopleSplit) * (tipPercent/100) + (bill/peopleSplit)

print(f"Each person should pay ${perPersonSplit:.2f}")
