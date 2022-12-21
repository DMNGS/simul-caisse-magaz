# Script      : model.py
# Description : Model class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
MIN_CLIENTS = 1
MAX_CLIENTS = 5
MIN_REGISTERS = 1
MAX_REGISTERS = 13
CLIENTS_HOUR = (0, 0, 0, 0, 0, 0, 0, 30, 30, 40, 50, 60, 100, 80, 50, 30, 80, 100, 50, 50, 80, 0, 0, 0)

class MarketSim:
    def __init__(self):
        self.registers = []
        self.clients = []