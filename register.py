# Script      : register.py
# Description : Register class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from queue import Queue

class Register:
    def __init__(self, line_size):
        self.open = False
        self.line = Queue(line_size)
        self.pay_time = 0