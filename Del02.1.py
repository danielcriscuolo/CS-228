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
##xMin = 100.0
##xMax = 0.0
##yMin = 100.0
##yMax = 0.0
xMin = -150
xMax = 150
yMin = -150
yMax = 150
##xMin = -1000
##xMax = 1000
##yMin = -1000
##yMax = 1000

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
    #pass
    #print "hand detected."
    hand = frame.hands[0]

    #detect fingers
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)
    
##    
##    #search specifically for index finger
##    indexFingerList = fingers.finger_type(1)
####    i = int(0)
####    for i in indexFingerList:
####        indexFingerList = fingers.finger_type(i)
##    #only one index finger per hand so grab the first in the list
##    indexFinger = indexFingerList[0]
##    #print(indexFinger)
##
##    #specific bone analysis through leap
##    distalPhalanx = indexFinger.bone(3)
##    #print(distalPhalanx)
##
##    #get the positions of the base and the tip of the bone
##    distalPhalanx = indexFinger.bone(3)
##    tip = distalPhalanx.next_joint
##    global x
##    x = tip[0]
##    x = int(x)
##    global y
##    y = tip[1]
##    y = int(y)
##
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

#takes in one finger and sets it up to recognize the bone cooridinates
def Handle_Finger(finger):
    for b in range(0,4):
        bone = finger.bone(b)
        Handle_Bone(bone,b)

#takes in one bone at a time an gets the cooridinates
def Handle_Bone(bone,bone_num):
    #get and save x,y coordinates for each base and tip of each bone
    base = bone.prev_joint
    base_coordinate_list = Handle_Vector_From_Leap(base)
    tip = bone.next_joint
    tip_coordinate_list = Handle_Vector_From_Leap(tip)

    #call the draw black line function
    instance.Draw_Black_Line(base_coordinate_list,tip_coordinate_list,((bone_num-3)*(-1)) +2)
    

    

def Handle_Vector_From_Leap(v):
    x = (v[0])
    scaled_x = Scale(x, xMin, xMax, constants_instance2.pygameXMin, constants_instance2.pygameWindowWidth)
        
    y = v[2]
    scaled_y = Scale(y, yMin, yMax, constants_instance2.pygameYMin, constants_instance2.pygameWindowDepth)
        
    return scaled_x,scaled_y
    

#scale the black point within our pygame window
def Scale(x, xMin, xMax, xMin2, xMax2):
    if xMin == xMax:
        xMin += .01
    value = (((x - xMin) * (xMax2 - xMin2)) / (xMax - xMin)) + xMin2
    value = int(value)
   
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
##    pygameX = Scale(x, xMin, xMax, constants_instance2.pygameXMin, constants_instance2.pygameWindowWidth)
##    #print pygameX
##    #pygameY = Scale(y, yMin, yMax, constants_instance2.pygameYMin, constants_instance2.pygameWindowDepth)
##    pygameY = Scale(y, yMin, yMax, constants_instance2.pygameWindowDepth, constants_instance2.pygameYMin)
##    #print pygameY
##        
##    
##    #create the circle that follows your hand
##    instance.Draw_Black_Circle(pygameX,pygameY)
##    #Perturb_Circle_Position()
    instance.Reveal()
