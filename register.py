# Script      : register.py
# Description : Register class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from queue import Queue
MIN_CLIENTS = 1
MAX_CLIENTS = 5

class Register:
    def __init__(self, line_size, wait_time):
        self.open = False
        self.line = Queue(line_size)
        self.wait_time = wait_time