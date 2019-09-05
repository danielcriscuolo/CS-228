# imports
import sys
sys.path.insert(0, "..")
import Leap

from constants import CONSTANTS
#create an instance variable for the class constances
constants_instance2 = CONSTANTS()

from pygameWindow import PYGAME_WINDOW
import random

x = 250 #where the black circle is located
y = 250 #where the black circle is located

#
xMin = 100.0
xMax = 0.0
yMin = 100.0
yMax = 0.0

#create an instance of the class called PYGAME_WINDOW
instance = PYGAME_WINDOW()

#this method will alter the position on the circle as if it were on a graph
def Perturb_Circle_Position():
    global x
    global y
    fourSidedDieRoll = random.randint(1,5)
    if fourSidedDieRoll == 1:
        x -= 1
    elif fourSidedDieRoll == 2:
                x += 1
    elif fourSidedDieRoll == 3:
        y -= 1
    else:
        y += 1

def Handle_Frame(frame):
    #print "hand detected."
    hand = frame.hands[0]

    #detect fingers
    fingers = hand.fingers

    #search specifically for index finger
    indexFingerList = fingers.finger_type(1)

    #only one index finger per hand so grab the first in the list
    indexFinger = indexFingerList[0]
    #print(indexFinger)

    #specific bone analysis through leap
    distalPhalanx = indexFinger.bone(3)
    #print(distalPhalanx)

    #get the positions of the base and the tip of the bone
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    global x
    x = tip[0]
    x = int(x)
    global y
    y = tip[1]
    y = int(y)
    print(tip)

    #make the screen be in the middle of where the leap device is looking??
    global xMin, xMax, yMin, yMax
    if ( x < xMin ):
        xMin = x
    if ( x > xMax ):
        xMax = x
    if ( y < yMin ):
        yMin = y
    if ( y > yMax ):
        yMax = y

#scale the black point within our pygame window
def Scale(x, xMin, xMax, xMin2, xMax2):
    if xMin == xMax:
        xMin += .01
    #value = ((x-xMin)/(xMax-xMin)) * (xMax2 - xMin2)
    #value = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    value = (((x - xMin) * (xMax2 - xMin2)) / (xMax - xMin)) + xMin2
    value = int(value)
    #value = int(value)
   
    return value


    
            
controller = Leap.Controller()
#continuous function to ultimately draw a circle and move is as hand moves
#currently function is only used for creating a dot that moves randomly throughout the screen
while True:
    instance.Prepare()
    frame = controller.frame()
    #Process hands...
    if not frame.hands.is_empty:
        x = 1
    else:
        x = 0
    if (int(x) > 0):
        Handle_Frame(frame)
    pygameX = Scale(x, xMin, xMax, constants_instance2.pygameXMin, constants_instance2.pygameWindowWidth)
    #print pygameX
    #pygameY = Scale(y, yMin, yMax, constants_instance2.pygameYMin, constants_instance2.pygameWindowDepth)
    pygameY = Scale(y, yMin, yMax, constants_instance2.pygameWindowDepth, constants_instance2.pygameYMin)
    #print pygameY
        
    
    #create the circle that follows your hand
    instance.Draw_Black_Circle(pygameX,pygameY)
    #Perturb_Circle_Position()
    instance.Reveal()
