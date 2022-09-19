# For a given number of stairs n, find the number of ways you 
# can climb up the set of stairs by taking only either one or two steps.

def numberOfWays(n: int):
    
    for i in range(n - 1):
        one, two = 1,1
        temp = one
        one = one + two
        two = temp
    return one
print(numberOfWays(5))