# Script      : model.py
# Description : Model class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from random import randint
from client import Client
from register import Register

NB_CLIENTS = 5
NB_REGISTERS = 13
CLIENTS_HOUR = (0, 0, 0, 0, 0, 0, 0, 30, 30, 40, 50, 60, 100, 80, 50, 30, 80, 100, 50, 50, 80, 0, 0, 0)

class MarketSim:
    def __init__(self, window):
        self.registers = []
        self.clients = []
        self.time = 60*7
        print(len(CLIENTS_HOUR))

        # to take care movement in x direction
        self.x = 5
        # to take care movement in y direction
        self.y = 3

        # Update window to allow the canvas to be the right size
        window.update()
        # canvas object to create shape
        self.width = 1000
        self.height = window.winfo_height()
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')

        self.clock = self.canvas.create_text(50, 50, text=str(self.time))

        # Create registers
        for i in range(NB_REGISTERS + 1):
            self.registers.append(Register(NB_CLIENTS, None))

        # Create clients
        for i in range(10):
            wait_time = randint(5, 120)
            self.rectangle = self.canvas.create_oval(5, 5, 45, 45, fill = "green")
            self.text = self.canvas.create_text(25, 25, text=str(wait_time))
            self.canvas.grid(row=0, column=0)

            self.clients.append(Client(self.rectangle, self.text, 100, 100, randint(1, 10), randint(1, 10)))
            self.movement(self.clients[i])

        self.canvas.after(1000, self.pass_time)

    def pass_time(self):
        self.time += 1
        self.canvas.itemconfigure(self.clock, text=str(self.time))

        for c in self.clients:
            if c.time <= 0:
                c.shopping = False
                c.time = c.wait_time
            elif c.shopping:
                c.time -= 1


        self.canvas.after(1000, self.pass_time)
    
    def movement(self, obj):

        DELAY = 16 # 16ms for ~60 FPS
        X1 = 0
        X2 = 2
        Y1 = 1
        Y2 = 3

        # Move object
        self.canvas.move(obj.shape_id, obj.vel_x, obj.vel_y)
        self.canvas.move(obj.text_id, obj.vel_x, obj.vel_y)

        pos = self.canvas.coords(obj.shape_id)
        
        if pos[X1] < 0 or pos[X2] > self.width:
            obj.vel_x *= -1
        if pos[Y1] < 0 or pos[Y2] > self.height:
            obj.vel_y *= -1

        self.canvas.after(DELAY, self.movement, obj)