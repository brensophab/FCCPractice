#Function to jump over hurdles of variable distance and height from eachother.
#Uses Predefined functions from https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
        turn_left()
        turn_left()
        turn_left()
def turn_around():
    turn_left()
    turn_left()
def move_forward():
    while front_is_clear() and not at_goal():
        move()
    
def face_north():
    while not is_facing_north():
        turn_left()
def jump_hurdle():
    face_north()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if front_is_clear() and not at_goal():
        move_forward()
    elif not front_is_clear():
        jump_hurdle()
        