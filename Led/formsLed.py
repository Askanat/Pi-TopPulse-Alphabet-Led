#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

# Display different forms on the pi-topPULSE led matrix
#
# Based on the script to display digits on pi-topPULSE

import ptpulse
from ptpulse import ledmatrix

import random

import re

import time

OFFSET_LEFT = 0
OFFSET_TOP = 0

NUMS = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,  # 0
        0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,  # 1
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,  # 2
        1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 3
        1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 4
        1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 5
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 6
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,  # 6
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 8
        1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]  # 9

class Show(object):

    def __init__(self):
        self.regex  = r"(^[a-zA-Z]*)"
        self.r      = random.randrange(255)
        self.g      = random.randrange(255)
        self.b      = random.randrange(255)

    def show_digit(val, xd, yd):
        """show_digit

            Calculate position of leds on and off

            Attributes:
                val : number display
                xd  : width display
                yd  : height display
        """

        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p-offset) // 3
            ledmatrix.set_pixel( xt+xd, 6-yt-yd, self.r*NUMS[p], self.g*NUMS[p], self.b*NUMS[p])
        ledmatrix.show()

    def show_letters_digits(self, val):
        """show_letters_digits

            Calculate number of 

            Attributes:
                val : number or letter
        """
        if val == 'L' is not None:
            switch = Switcher()
            switch.call_letters(val)
            
        else :
            value   = int(val)
            abs_val = abs(value)
            tens    = abs_val // 10
            units   = abs_val % 10
            if (abs_val > 9):
                show_digit(tens, OFFSET_LEFT, OFFSET_TOP)
            show_digit(units, OFFSET_LEFT+4, OFFSET_TOP)

class Switcher(object):

    def __init__(self):
        self.method_name    = 'show'
        self.r              = random.randrange(255)
        self.g              = random.randrange(255)
        self.b              = random.randrange(255)

    def call_letters(self, argument):
        """call_letters

            Call the  function corresponding to the letter

            Attributes:
                argument    : 

        """

        method_name = self.method_name + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, self.method_name, lambda: "Invalid letter")
        # Call the method as we return it
        print('pouet')
        return method()

 
    def show_A(self):
        return "January"
 
    def show_B(self):
        return "February"
 
    def show_C(self):
        return "March"

    def show_L(self):
        print('coucou')
        #Vertical
        ledmatrix.set_pixel( 1 , 1 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 1 , 2 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 1 , 3 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 1 , 4 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 1 , 5 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 1 , 6 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        #Horizontal
        ledmatrix.set_pixel( 2 , 1 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 3 , 1 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.set_pixel( 4 , 1 , self.r*NUMS[1] , self.g*NUMS[1] , 
            self.b*NUMS[1])
        ledmatrix.show()
    


###############################################################################
# MAIN                                                                        #
###############################################################################
if __name__ == '__main__':
    ledmatrix.rotation(0)
    ledmatrix.clear()

    led = Show()
    val = 0

    led.show_letters_digits('L')

    """while True:

        led.show_letters_digits('L')

        if val <= 99:
            show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1
        if val > 99:
            ledmatrix.clear()
            ledmatrix.show()
            val = 0 
            self.r = random.randrange(255)
            self.g = random.randrange(255)
            self.b = random.randrange(255)
            show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1"""

    ledmatrix.clear()
    ledmatrix.show()