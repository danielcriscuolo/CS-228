#imports
from constants import CONSTANTS
import pygame

#create an instance variable for the class constances
constants_instance = CONSTANTS()

#this class creates the window that ultimately is what we should see when we run the program
class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants_instance.pygameWindowWidth,constants_instance.pygameWindowDepth))
    def Prepare(self):
        
        #fill with white
        self.screen.fill((255,255,255))
        
        #code to help the visual from step 44
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
    def Reveal(self):
        pygame.display.update()

    #this method should draw the circle in the window
    #...circle(surface, color, center, radius)
    def Draw_Black_Circle(self,x,y):
        pygame.draw.circle(self.screen,(0,0,0),(x,y),15)
