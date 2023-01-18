# Script      : client.py
# Description : Client class
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0

class Client:
    def __init__(self, shape_id, text_id, shop_time, wait_time, vel_x, vel_y):
        self.shape_id = shape_id
        self.text_id = text_id

        self.shop_time = shop_time
        self.wait_time = wait_time
        self.time = shop_time

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.shopping = true