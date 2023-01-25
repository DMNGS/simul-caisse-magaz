# Script      : model.py
# Description : Model class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from tkinter import ttk
from random import randint
from client import *
from register import Register

DEFAULT_NB_CLIENTS = 5
DEFAULT_NB_REGISTERS = 13
DEFAULT_MIN_SHOP_TIME = 5
DEFAULT_MAX_SHOP_TIME = 120
DEFAULT_REGISTER_WAIT_TIME = 10

HOUR = 60
CIRCLE_DIAMETER = 40

CLIENTS_HOUR = (0, 0, 0, 0, 0, 0, 0, 30, 30, 40, 50, 60, 100, 80, 50, 30, 80, 100, 50, 50, 80, 0, 0, 0)

class MarketSim:
    def __init__(self, window):
        self.registers = []
        self.clients = []

        self.time = HOUR*7-1 # Begin just before 07:00
        self.avg_wait = 0.0

        self.clients_register = DEFAULT_NB_CLIENTS
        self.nb_registers = DEFAULT_NB_REGISTERS
        self.shop_time_min = DEFAULT_MIN_SHOP_TIME
        self.shop_time_max = DEFAULT_MAX_SHOP_TIME
        self.register_wait_time = DEFAULT_REGISTER_WAIT_TIME

        # Create registers
        for i in range(self.nb_registers):
            self.registers.append(Register(self.clients_register))
        self.registers[0].open = True

        # Update window to allow the canvas to be the right size
        window.update()
        # canvas object to create shape
        self.width = 1000
        self.height = window.winfo_height()
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.grid(row=0, column=0, rowspan=100)

        # UI
        STICKY_DIR = N+W
        grid_row = 0

        self.lbl_registers = ttk.Label(window, text=f'Caisses {1}/{len(self.registers)}')
        self.lbl_registers.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.lbl_register_time = ttk.Label(window, text=f'Temps avant ouverture : {self.register_wait_time} s')
        self.lbl_register_time.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.lbl_registerless_clients = ttk.Label(window, text=f'Clients sans caisse : {self.count_registerless()}')
        self.lbl_registerless_clients.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.lbl_open_slots = ttk.Label(window, text=f'Places disponibles : {self.count_open_slots()}')
        self.lbl_open_slots.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.lbl_nb_clients = ttk.Label(window, text=f'Nombre de clients : {len(self.clients)}')
        self.lbl_nb_clients.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.lbl_avg_wait = ttk.Label(window, text=f'Temps d\'attente moyen : {self.avg_wait:.2f}')
        self.lbl_avg_wait.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.lbl_clock = ttk.Label(window, text=f'Heure : {int(self.time / HOUR)}:{(self.time % HOUR):02d}')
        self.lbl_clock.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.btn_add_clients = ttk.Button(window, text='Ajouter 5 clients', command = lambda: self.create_clients(5))
        self.btn_add_clients.grid(row=grid_row, column=1, sticky=STICKY_DIR)
        grid_row += 1

        self.btn_add_time = ttk.Button(window, text='Ajouter 1 heure', command = lambda: self.new_hour(1))
        self.btn_add_time.grid(row=8, column=1, sticky=STICKY_DIR)
        grid_row += 1

        #Active simulation
        self.canvas.after(1000, self.update)

    # Create clients
    def create_clients(self, nb_clients):
        for i in range(nb_clients):
            shop_time = randint(self.shop_time_min, self.shop_time_min)
            vel_x = randint(1, 10)
            vel_y = randint(1, 10)
            self.rectangle = self.canvas.create_oval(5, 5, 5 + CIRCLE_DIAMETER, 5 + CIRCLE_DIAMETER, fill = "black")
            self.text = self.canvas.create_text(25, 25, fill='white', text=str(shop_time))

            self.clients.append(Client(self.rectangle, self.text, shop_time, vel_x, vel_y))
            self.move_client(self.clients[len(self.clients) - 1])

    # Add clients at begining of hour
    # advance : how many hours to add
    def new_hour(self, advance = 0):
        self.time += HOUR * advance
        new_hour = False if advance == 0 else True

        cur_hour = int(self.time / HOUR)
        if self.time % HOUR == 0 and not new_hour:
            if cur_hour == 24:
                time = 0
                cur_hour = 0
            
            new_hour = True

        if new_hour:
            self.create_clients(CLIENTS_HOUR[cur_hour])
            
        self.update_view()
    
    # Move a client
    def move_client(self, obj):
        DELAY = 16 # 16ms for ~60 FPS
        X1 = 0
        X2 = 2
        Y1 = 1
        Y2 = 3

        # Move client
        if obj.state != CLIENT_PAYING:
            self.canvas.move(obj.shape_id, obj.vel_x, obj.vel_y)
            self.canvas.move(obj.text_id, obj.vel_x, obj.vel_y)

            pos = self.canvas.coords(obj.shape_id)
        
            if pos[X1] < 0 or pos[X2] > self.width:
                obj.vel_x *= -1
            if pos[Y1] < 0 or pos[Y2] > self.height / 2:
                obj.vel_y *= -1

            obj.move_event = self.canvas.after(DELAY, self.move_client, obj)

    # Count clients who are done shopping but aren't at a register
    def count_registerless(self):
        registerless = 0
        for c in self.clients:
            registerless += 1 if c.state == CLIENT_WAIT_OPEN else 0

        return registerless

    def count_open_registers(self):
        opens = 0
        for r in self.registers:
            opens += 1 if r.open else 0

        return opens

    # Count open slots on all registers
    def count_open_slots(self):
        return 0

    # Move client to register
    def move_to_register(self, client, register_id):
        self.canvas.moveto(client, 10 * register_id, self.height - 30)
        pass

    # Update the simulation
    def update(self):
        total_wait = 0
        waiting_clients = 0
        self.avg_wait = 0

        self.time += 1

        for c in self.clients:
            # Decrement shop time
            if c.state == CLIENT_SHOPPING:
                if c.time <= 0:
                    c.state = CLIENT_WAIT_OPEN
                    self.canvas.itemconfigure(c.shape_id, fill='red')
                else:
                    grey = int(c.time/c.shop_time * 255)
                    c.time -= 1
                    self.canvas.itemconfigure(c.shape_id, fill=f'#{grey}{grey}{grey}')
            # Look for an open register
            elif c.state == CLIENT_WAIT_OPEN:
                for r in self.registers:
                    if r.open and not r.full():
                        r.line.append(c)
                        self.move_to_register(c, self.registers.index(r))
                        c.state = CLIENT_PAYING
                    else:
                        c.time += 1
                        total_wait += c.time
                        waiting_clients += 1

            self.canvas.itemconfigure(c.text_id, text=str(c.time))
        
        # If there is wait, there is waiting client(s)
        if total_wait > 0:
            self.avg_wait = total_wait / waiting_clients

        # Registers
        
        for r in self.registers:

            r.pay_time -= 1

            # Check in new client
            if len(r.line) > 0 and r.pay_time <= 0:
                r.line.pop(0)
                r.wait_time = r.line[0].wait_time

            # Open it if average wait time is too big
            if not r.open and self.avg_wait > self.register_wait_time:
                r.open = True
            # And close it when there is little to no wait
            elif r.open and self.avg_wait > self.register_wait_time and len(r.line) == 0:
                r.open = False

        # Add new clients every hour
        self.new_hour()

        self.update_view()
        self.canvas.after(1000, self.update)

    # Update all the labels
    def update_view(self):
        self.lbl_registers.config(text=f'Caisses {self.count_open_registers()}/{len(self.registers)}')
        self.lbl_register_time.config(text=f'Temps avant ouverture : {self.register_wait_time} s')
        self.lbl_registerless_clients.config(text=f'Clients sans caisse : {self.count_registerless()}')
        self.lbl_open_slots.config(text=f'Places disponibles : {self.count_open_slots()}')
        self.lbl_nb_clients.config(text=f'Nombre de clients : {len(self.clients)}')
        self.lbl_avg_wait.config(text=f'Temps d\'attente moyen : {self.avg_wait:.2f}')
        self.lbl_clock.config(text=f'Heure : {int(self.time / HOUR):02d}:{(self.time % HOUR):02d}')