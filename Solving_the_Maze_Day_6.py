def turn_right():
    turn_left()       # 4 spaces for each line in this function
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():       # 4 spaces to align with the while loop
        turn_right()           # 8 spaces for lines within the if block
        move()
    
    elif front_is_clear():     # 4 spaces to align with the while loop
        move()                 # 8 spaces within the elif block

    else:
        turn_left()            # 8 spaces within the else block



#reeborgs world Maze 4 code