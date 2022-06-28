from audioop import mul
from operator import indexOf
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
    print(operation) #INCOMPLETE: COMPLETE FOR LOOP TO PRINT OUT EVERY OPERATION IN THE OPERATIONS DICT
operation_symbol = input("Pick an operation from the lines above")
# def calculate():
#     if operation_symbol == "+":
#         answer = add(num1, num2)
#     elif operation_symbol == "-":
#         answer = subtract(num1,num2)
#     elif operation_symbol == "*":
#         answer = multiply(num1,num2)
#     elif operation_symbol == "/": 
#         answer = divide(num1,num2)
#     return answer
# answer = calculate()

#MY SOLUTION ^^ WORKED FINE, HOWEVER, THIS IS THE INTENDED SOLUTION WITH DICTS
calc_func = operations[operation_symbol]
answer = calc_func(num1, num2)
print(f"{num1}{operation_symbol}{num2} = {answer}")