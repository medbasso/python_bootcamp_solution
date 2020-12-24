def right():  
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
        if right_is_clear():
            right()
       
    
        
    
       
        
        
 
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
