def right():
    turn_left()
    turn_left()
    turn_left()
    
    
    
def jump():
    right()
    move()
    right()
    


while not  at_goal():
    while wall_in_front():
        turn_left()
    if front_is_clear():
        move()
        if right_is_clear():
            jump()
    
  
         
        
    
      
        
        
    
      
      
    
     
        
        
        
     
    
        
        
 
 
    
    
    
    
        
        
    
        
 
    
    
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
