
isPrime = True
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break
        else:
            isPrime = True
    
    if isPrime:
        print("{} is a prime number".format(number))
    else:
        print("{} is not a prime number".format(number))
   

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
