# Script      : main.py
# Description : entry code
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from tkinter import ttk
from frm_about import show_about
from frm_settings import sim_param
import model

def main():
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900

    root = Tk()
    root.title('Simulateur de caisses')
    root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    root.resizable(False, False)

    sim = model.MarketSim(root)

    menubar = Menu(root)
    submenu = Menu(menubar, tearoff=0)
    submenu.add_command(label="Paramètres", command=sim_param)
    submenu.add_command(label="A propos", command=show_about)
    menubar.add_cascade(label="Programe", menu=submenu)

    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()