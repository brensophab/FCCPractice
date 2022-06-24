from art import logo
print(logo)
def clear():
    
    print('\n' * 100)
    print('\033[2J\033[1;1H', end='')

#Calculator
#add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2
operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Whats the first number?:\n"))
num2 = int(input("Whats the second number?\n"))
for operation in operations:
    print(operations) #INCOMPLETE: COMPLETE FOR LOOP TO PRINT OUT EVERY OPERATION IN THE OPERATIONS DICT