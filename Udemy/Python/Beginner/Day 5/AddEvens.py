#program to only add the even numbers between 2 and 100, Expected sum should be 2550

sum =0
for i in range(2, 101, 2):
    sum += i
print(sum)