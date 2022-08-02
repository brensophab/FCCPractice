from audioop import mul
from operator import indexOf
from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2
def exponent(n1, n2):
    return n1 ** n2
operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": mod,
    "^": exponent
}
def calc():
    num1 = float(input("Whats the first number?:\n"))
    num2 = float(input("Whats the second number?\n"))

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
    print(f"{num1}{operation_symbol}{num2} = {answer}\n")
    calc_loop(answer)
def calc_loop(answer):
    continue_calc = input("type 'y' to continue calculation. Press any other key to exit.\n")
    if continue_calc is 'y':
        prev_answer = answer
        # print(f"previous answer is {prev_answer}")
        num2 = float(input("Insert the next number\n"))
        operation_symbol = input("Pick your next operation\n")
        calc_func = operations[operation_symbol]
        answer = calc_func(prev_answer,num2)
        print(f"{prev_answer} {operation_symbol} {num2} = {answer}")
        calc_loop(answer)
    elif continue_calc is not 'y':
        restart_calc = input("Do you wish to start a new calculation?('y' or 'n')")
        if restart_calc is 'y':
            calc()
        else:
            return
        
calc()
