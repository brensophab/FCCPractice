# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():#Standard function
    print("Hi")
    print("How are you?")
    print("It is nice to meet you dear.")
greet()

#function with param
# def greet_with_name(name):
    
#     print(f"Hello {name}!")
# greet_with_name(input("What is your name?\n"))

#Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name} from {location}! its nice to meet you.")
    print(f"Whats the weather like down in {location}?")
greet_with(input("What is your name?\n"), input("Where are you from?\n"))
#Can also be written as
#greet_with(name = input("What is your name?\n"), location=input("What is your location?\n"))


#TEACHER EXAMPLES FOR REFERENCE
# Simple Function
# def greet():
#   print("Hello Angela")
#   print("How do you do Jack Bauer?")
#   print("Isn't the weather nice today?")
# greet()

# Function that allows for input
# 'name' is the parameter.
# 'Jack Bauer' is the argument.
# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
# greet_with_name("Jack Bauer")

# Functions with more than 1 input
# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}?")

# Calling greet_with() with Positional Arguments
# greet_with("Jack Bauer", "Nowhere")
# vs.
# greet_with("Nowhere", "Jack Bauer")


# Calling greet_with() with Keyword Arguments
# greet_with(location="London", name="Angela")