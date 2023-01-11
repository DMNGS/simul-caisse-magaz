# Script      : main.py
# Description : entry code
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from tkinter import *
from tkinter import ttk
import model

circle_x = 10
circle_y = 10
 

def move_circle(circle):
    canvas.move(circle, 1, 1)
    canvas.after(100, move_circle(circle))   

def main():

    global circle_x, circle_y
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500

    root = Tk()
    root.title('canvasulateur de caisses')
    root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    root.resizable(False, False)

    sim = model.MarketSim(root)

    root.mainloop()

if __name__ == "__main__":
    main()