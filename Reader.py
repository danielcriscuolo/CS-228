import pickle
import numpy
import os
from pygameWindow_Del03 import PYGAME_WINDOW
class READER:
    def __init__(self):
        self.Store_Num_Gestures()
        self.pygame_Window = PYGAME_WINDOW()
        # pickle_in = open("userData/gesture.p","rb")
        # gestureData = pickle.load(pickle_in)
        # print gestureData

    def Store_Num_Gestures(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)
    def Print_Gestures(self):
        path, dirs, files = next(os.walk('userData'))
        for i in files:
            pickle_in = open("userData/"+i,"rb")
            gestureData = pickle.load(pickle_in)
            print gestureData
    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()

    def Draw_Each_Gesture_Once(self):
        path, dirs, files = next(os.walk('userData'))
        for i,filename in enumerate(files):
            pickle_in = open("userData/"+filename,"rb")
            gestureData = pickle.load(pickle_in)
            # print gestureData
            self.Draw_Gesture(i)
    def Draw_Gesture(self, gestureNumber):
        pass
