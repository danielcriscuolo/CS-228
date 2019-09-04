# imports
import sys
sys.path.insert(0, "..")
import Leap

##from pygameWindow import PYGAME_WINDOW
##import random
##
##x = 250 #where the black circle is located
##y = 250 #where the black circle is located
##
#create an instance of the class called PYGAME_WINDOW
##instance = PYGAME_WINDOW()
##
#this method will alter the position on the circle as if it were on a graph
##def Perturb_Circle_Position():
##    global x, y
##    fourSidedDieRoll = random.randint(1,5)
##    if fourSidedDieRoll == 1:
##        x -= 1
##    elif fourSidedDieRoll == 2:
##                x += 1
##    elif fourSidedDieRoll == 3:
##        y -= 1
##    else:
##        y += 1
##

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
    print(distalPhalanx)

    #get the positions of the base and the tip of the bone
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    print(tip)

    
            
controller = Leap.Controller()
#continuous function to ultimately draw a circle and move is as hand moves
#currently function is only used for creating a dot that moves randomly throughout the screen
while True:
##    instance.Prepare()
    frame = controller.frame()
    #Process hands...
    if not frame.hands.is_empty:
        x = 1
    else:
        x = 0
    if (int(x) > 0):
        Handle_Frame(frame)
        
##    instance.Draw_Black_Circle(x,y)
##    Perturb_Circle_Position()
##    instance.Reveal()
