import pickle
import numpy
class READER:
    pickle_in = open("userData/gesture.p","rb")
    gestureData = pickle.load(pickle_in)
    print gestureData
