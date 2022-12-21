# Script      : register.py
# Description : Register class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0
from queue import Queue

class Register:
    def __init__(self, line_size, wait_time):
        self.line = Queue(line_size)
        self.wait_time = wait_time