# Script      : model.py
# Description : Model class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from random import randint
from client import *
from register import Register

DEFAULT_NB_CLIENTS = 5
DEFAULT_NB_REGISTERS = 13
DEFAULT_MIN_SHOP_TIME = 5
DEFAULT_MAX_SHOP_TIME = 120
DEFAULT_REGISTER_WAIT_TIME = 10

CLIENTS_HOUR = (0, 0, 0, 0, 0, 0, 0, 30, 30, 40, 50, 60, 100, 80, 50, 30, 80, 100, 50, 50, 80, 0, 0, 0)

class MarketSim:
    def __init__(self, window):
        self.registers = []
        self.clients = []
        self.time = 60*7-1
        self.win = window
        self.clients_register = DEFAULT_NB_CLIENTS
        self.shop_time_min = DEFAULT_MIN_SHOP_TIME
        self.shop_time_max = DEFAULT_MAX_SHOP_TIME
        self.register_wait_time = DEFAULT_REGISTER_WAIT_TIME

        # Update window to allow the canvas to be the right size
        window.update()
        # canvas object to create shape
        self.width = 1000
        self.height = window.winfo_height()
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.grid(row=0, column=0)

        self.clock = self.canvas.create_text(50, 50, text=str(self.time))

        # Create registers
        for i in range(self.clients_register):
            self.registers.append(Register(self.clients_register))
        self.registers[0].open = True

        self.canvas.after(1000, self.update)

    # Create clients
    def create_clients(self, nb_clients):
        for i in range(nb_clients):
            shop_time = randint(self.shop_time_min, self.shop_time_max)
            vel_x = randint(1, 10)
            vel_y = randint(1, 10)
            self.rectangle = self.canvas.create_oval(5, 5, 45, 45, fill = "black")
            self.text = self.canvas.create_text(25, 25, fill='white', text=str(shop_time))

            self.clients.append(Client(self.rectangle, self.text, shop_time, vel_x, vel_y))
            self.movement(self.clients[len(self.clients) - 1])

    # Move client to register
    def move_client(self, client):
        # TODO
        pass

    # Update the simulation
    def update(self):
        HOUR = 60
        total_wait = 0
        waiting_clients = 0
        avg_wait = 0

        self.time += 1
        self.canvas.itemconfigure(self.clock, text=str(self.time))

        for c in self.clients:
            # Decrement shop time
            if c.state == CLIENT_SHOPPING:
                if c.time <= 0:
                    c.state = CLIENT_WAIT_OPEN
                    self.canvas.itemconfigure(c.shape_id, fill='red')
                else:
                    grey = int(c.time/c.shop_time * 255)
                    c.time -= 1
                    #self.canvas.itemconfigure(c.shape_id, fill=f'#{grey}{grey}{grey}')
            # Look for an open register
            elif c.state == CLIENT_WAIT_OPEN:
                for r in self.registers:
                    if r.open and not r.line.full():
                        r.line.put(c)
                        self.move_client(c)
                        c.state = CLIENT_PAYING
                    else:
                        c.time += 1
                        total_wait += c.time
                        waiting_clients += 1

            self.canvas.itemconfigure(c.text_id, text=str(c.time))
        
        # If there is wait, there is waiting client(s)
        if total_wait > 0:
            avg_wait = total_wait / waiting_clients

        # Registers
        
        for r in self.registers:

            r.pay_time -= 1

            # Check in new client
            if not r.line.empty() and r.pay_time <= 0:
                r.line.get()
                r.wait_time = r.line[0].wait_time

            # Open it if average wait time is too big
            if not r.open and avg_wait > self.register_wait_time:
                r.open = True
            # And close it when there is little to no wait
            elif r.open and avg_wait > self.register_wait_time:
                r.open = False

        # Add new clients every hour
        cur_hour = int(self.time / HOUR)
        if self.time % HOUR == 0:
            if cur_hour == 24:
                time = 0
                cur_hour = 0
            
            self.create_clients(CLIENTS_HOUR[cur_hour])


        self.canvas.after(1000, self.update)
    
    # Move a client
    def movement(self, obj):
        DELAY = 16 # 16ms for ~60 FPS
        X1 = 0
        X2 = 2
        Y1 = 1
        Y2 = 3

        # Move object
        if obj.state != CLIENT_PAYING:
            self.canvas.move(obj.shape_id, obj.vel_x, obj.vel_y)
            self.canvas.move(obj.text_id, obj.vel_x, obj.vel_y)

            pos = self.canvas.coords(obj.shape_id)
        
            if pos[X1] < 0 or pos[X2] > self.width:
                obj.vel_x *= -1
            if pos[Y1] < 0 or pos[Y2] > self.height:
                obj.vel_y *= -1

            obj.move_event = self.canvas.after(DELAY, self.movement, obj)