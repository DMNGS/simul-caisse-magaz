# Script      : frm_settings.py
# Description : Simulation settings window
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from tkinter import ttk

def sim_param():
    win_settings = Tk()
    win_settings.title('Paramètres du simulateur')
    win_settings.resizable(False, False)

    nb_registers = 1
    nb_clients = 1
    min_shop_time = 5
    max_shop_time = 20
    time_register = 1

    frm_settings = ttk.Frame(win_settings, padding=10)
    ttk.Label(frm_settings, text='Nombre de caisse').grid(row=0, column=0)
    ttk.Scale(frm_settings, from_=1, to=13).grid(row=0, column=1)

    ttk.Label(frm_settings, text='Nombre de clients par caisses').grid(row=1, column=0)
    ttk.Scale(frm_settings, from_=1, to=5).grid(row=1, column=1)
    
    ttk.Label(frm_settings, text='Temps de course minimum').grid(row=2, column=0)
    ttk.Scale(frm_settings, from_=5, to=10).grid(row=2, column=1)
    frm_settings.grid()
    
    ttk.Label(frm_settings, text='Temps de course maximum').grid(row=3, column=0)
    ttk.Scale(frm_settings, from_=20, to=120).grid(row=3, column=1)
    frm_settings.grid()
    
    ttk.Label(frm_settings, text='Temps d\'attente pour caisses').grid(row=4, column=0)
    ttk.Scale(frm_settings, from_=1, to=10).grid(row=4, column=1)
    frm_settings.grid()
    frm_settings.grid()

    win_settings.mainloop()