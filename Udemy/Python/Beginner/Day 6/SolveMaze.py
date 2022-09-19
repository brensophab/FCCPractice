#Same deal as Hurdle solver. https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json



def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
    turn_left()
def solve_maze():
    while not_at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
solve_maze()
#Supposed Indentation error, but lgtm, so oh well.