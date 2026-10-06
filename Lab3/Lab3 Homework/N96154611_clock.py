#!/usr/bin/env python3
from time import sleep, localtime

import sys

sys.path.append(r"../7segment_display/raspberrypi-tm1637")  # add the path to the tm1637.py file

# import tm1637
from tm1637 import TM1637

CLK = 17     # 請更改至你實際接線的 GPIO 腳位 (BCM GPIO??)
DIO = 27    # 請更改至你實際接線的 GPIO 腳位 (BCM GPIO??)

class Clock:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.show_colon = False

    def run(self):
        while True:
            t = localtime()
            self.show_colon = not self.show_colon
            self.tm.numbers(t.tm_hour, t.tm_min, self.show_colon)
            sleep(1)

if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(1)  # set brightness: 0 (min) ~ 7 (max)

    clock = Clock(tm)
    clock.run()
