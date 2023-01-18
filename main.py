# Script      : main.py
# Description : entry code
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from tkinter import ttk
import model 

def main():
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900

    root = Tk()
    root.title('canvasulateur de caisses')
    root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    root.resizable(False, False)

    sim = model.MarketSim(root)

    root.mainloop()

if __name__ == "__main__":
    main()