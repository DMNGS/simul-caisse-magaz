# Script      : register.py
# Description : Register class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from queue import Queue

class Register:
    def __init__(self, line_size):
        self.open = False
        self.line = []
        self.line_size = line_size
        self.pay_time = 0

    def full(self):
        return True if len(self.line) >= self.line_size else False