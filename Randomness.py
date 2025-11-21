from graphics import *
import random as random

x_val = random.randint(0, 1600)
y_val = random.randint(0, 800)

# Create Window and object inside it 
# Note not my created code
window = GraphWin("Randomness", 1600, 800, autoflush=True)
target = Circle(Point(x , y), 30)
target.setFill("red")
target.draw(window)

#move the object at random
def movement():
        #change position
        choice_x = random.randint(-1,1)
        x_val = x_val + choice_x

        choice_y = random.randint(-1,1)
        y_val = y_val + choice_y

# Add noise to the randomness


while true:
    #Impliment updating movement
