# Script      : model.py
# Description : Model class
# Author      : DOMINGUES PEDROSA Samuel
from tkinter import *

MIN_REGISTERS = 1
MAX_REGISTERS = 13
CLIENTS_HOUR = (0, 0, 0, 0, 0, 0, 0, 30, 30, 40, 50, 60, 100, 80, 50, 30, 80, 100, 50, 50, 80, 0, 0, 0)

class MarketSim:
    def __init__(self, window):
        self.registers = []
        self.clients = []

        # to take care movement in x direction
        self.x = 1
        # to take care movement in y direction
        self.y = 0

        # Update window to allow the canvas to be the right size
        window.update()
        # canvas object to create shape
        self.canvas = Canvas(window, width=window.winfo_width(), height=window.winfo_height())
        # creating rectangle
        self.rectangle = self.canvas.create_rectangle(5, 5, 25, 25, fill = "black")
        self.canvas.pack()

        # calling class's movement method to
        # move the rectangle
        self.movement(self.rectangle)
    
    def movement(self, client):

        DELAY = 16 # 16ms for ~60 FPS

        # Move object
        self.canvas.move(client, self.x, self.y)

        self.canvas.after(DELAY, self.movement, client)
    
    # for motion in negative x direction
    def left(self, event):
        print(event.keysym)
        self.x = -5
        self.y = 0
    
    # for motion in positive x direction
    def right(self, event):
        print(event.keysym)
        self.x = 5
        self.y = 0
    
    # for motion in positive y direction
    def up(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -5
    
    # for motion in negative y direction
    def down(self, event):
        print(event.keysym)
        self.x = 0
        self.y = 5