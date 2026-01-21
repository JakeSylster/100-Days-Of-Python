#This code is readable but was used to design for Reeborg.ca
from library import turn_right
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

def draw_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

def jump():
    #move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#Jump over hurdles
for i in range(6):
    jump()

#Jump when the end point is randomly generated
while(not at_goal()):
   jump()

#Reach end point with random generated hurdles and end point
while(not at_goal()):
    if(front_is_clear()):
        move()
    if(wall_in_front()):
        jump()

#Reach end point with randomly generated end point, hurdles and their heights
while(not at_goal()):
    if(right_is_clear()):
        turn_right()
    if(wall_in_front()):
        turn_left()
    if(front_is_clear()):
        move()

#Randomly spawned robot in random direction needs to reach end point
while(front_is_clear()):
    move()
turn_left()
while(not at_goal()):
    if(right_is_clear()):
        turn_right()
        move()
    elif(front_is_clear()):
        move()
    else:
        turn_left()
        
   
        

