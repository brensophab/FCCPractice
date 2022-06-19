
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# example input 23
#Write your code below this row 👇
horizontal = int(position[0]) #2
vertical   = int(position[1]) #3

selected_row = map[vertical - 1]
selected_row[horizontal -1] = "X"




#Write your code above this row 👆


print(f"{row1}\n{row2}\n{row3}")
