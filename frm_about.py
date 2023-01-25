# Script      : frm_about.py
# Description : About window
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2023.01.11, V1.0
from tkinter import *
from tkinter import ttk

def show_about():
    win_about = Tk()
    win_about.title('A propos')
    win_about.resizable(False, False)

    frm_about = ttk.Frame(win_about, padding=10)
    frm_about.grid()

    ttk.Label(frm_about, text="Simulation de caisses V1.0").grid(column=0, row=0)
    ttk.Label(frm_about, text="Auteur : DOMINGUES PEDROSA Samuel").grid(column=0, row=1)
    ttk.Label(frm_about, text="CFPT 2023").grid(column=0, row=2)

    win_about.mainloop()