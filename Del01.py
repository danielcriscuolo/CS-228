# imports
from pygameWindow import PYGAME_WINDOW
import random

x = 250 #where the black circle is located
y = 250 #where the black circle is located

#create an instance of the class called PYGAME_WINDOW
instance = PYGAME_WINDOW()

#this method will alter the position on the circle as if it were on a graph
def Perturb_Circle_Position():
    global x, y
    fourSidedDieRoll = random.randint(1,5)
    if fourSidedDieRoll == 1:
        x -= 1
    elif fourSidedDieRoll == 2:
                x += 1
    elif fourSidedDieRoll == 3:
        y -= 1
    else:
        y += 1

#continuous function to ultimately draw a circle and move is as hand moves
#currently function is only used for creating a dot that moves randomly throughout the screen
while True:
    instance.Prepare()
    instance.Draw_Black_Circle(x,y)
    Perturb_Circle_Position()
    instance.Reveal()
        
