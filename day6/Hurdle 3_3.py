def right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()

while at_goal() !=True:
    if wall_in_front() != True:
        move()
    else:
        jump()
        
    
    
        
        
        
        
 
        
 
    
    
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
