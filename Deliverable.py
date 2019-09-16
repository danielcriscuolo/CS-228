import sys
sys.path.insert(0, "..")
import Leap
controller = Leap.Controller()
import random
from constants import CONSTANTS
#create an instance variable for the class constances
constants_instance2 = CONSTANTS()
from pygameWindow import PYGAME_WINDOW
instance = PYGAME_WINDOW()
class DELIVERABLE:
    def __init__(self):
        self.controller = Leap.Controller
        self.instance = PYGAME_WINDOW()
        self. x = 250
        self.y = 250
        self.xMin = -150
        self.xMax = 150
        self.yMin = -150
        self.yMax = 150

    def Handle_Frame(self, frame):
        hand = frame.hands[0]
        #detect fingers
        fingers = hand.fingers
        for finger in fingers:
            self.Handle_Finger(finger)
        #make the screen be in the middle of where the leap device is looking??
        global xMin, xMax, yMin, yMax
        if ( self.x < self.xMin ):
            self.xMin = self.x
        if ( self.x > self.xMax ):
            self.xMax = self.x
        if ( self.y < self.yMin ):
            self.yMin = self.y
        if ( self.y > self.yMax ):
            self.yMax = self.y

    #takes in one finger and sets it up to recognize the bone cooridinates
    def Handle_Finger(self, finger):
        for b in range(0,4):
            bone = finger.bone(b)
            self.Handle_Bone(bone,b)

    #takes in one bone at a time an gets the cooridinates
    def Handle_Bone(self, bone,bone_num):
        #get and save x,y coordinates for each base and tip of each bone
        base = bone.prev_joint
        base_coordinate_list = self.Handle_Vector_From_Leap(base)
        tip = bone.next_joint
        tip_coordinate_list = self.Handle_Vector_From_Leap(tip)

        #call the draw black line function
        instance.Draw_Black_Line(base_coordinate_list,tip_coordinate_list,((bone_num-3)*(-1)) +2)

    # take in a list of an x,y, and z value, use x and z to form the hand, scale them to the screen.
    def Handle_Vector_From_Leap(self, v):
        x = (v[0])
        scaled_x = self.Scale(x, self.xMin, self.xMax, constants_instance2.pygameXMin, constants_instance2.pygameWindowWidth)
            
        y = v[2]
        scaled_y = self.Scale(y, self.yMin, self.yMax, constants_instance2.pygameYMin, constants_instance2.pygameWindowDepth)
            
        return scaled_x,scaled_y

    #scale the black point within our pygame window
    def Scale(self, x, xMin, xMax, xMin2, xMax2):
        if xMin == xMax:
            xMin += .01
        value = (((x - xMin) * (xMax2 - xMin2)) / (xMax - xMin)) + xMin2
        value = int(value)
       
        return value

    #creating a new method for the while statement
    def Run_Forever(self):
        while True:
            instance.Prepare()
            frame = controller.frame()
            #Process hands...
            if not frame.hands.is_empty:
                x = 1
            else:
                x = 0
            if (int(x) > 0):
                self.Handle_Frame(frame)
            self.Run_Once()
            instance.Reveal()
    def Run_Once(self):
        instance.Prepare()
        frame = controller.frame()
        #Process hands...
        if not frame.hands.is_empty:
            x = 1
        else:
            x = 0
        if (int(x) > 0):
            self.Handle_Frame(frame)
        instance.Reveal()
