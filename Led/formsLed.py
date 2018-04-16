#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

# Display different forms on the pi-topPULSE led matrix
#
# Based on the script to display digits on pi-topPULSE

"""
MIT License
Copyright (c) 2018 Florian Vaissiere [https://github.com/FlorianVaissiere]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

###############################################################################
# Import                                                                      #
###############################################################################
import ptpulse
from ptpulse import ledmatrix

import random
from random import random

import re
from re import search

import time
from time import time


###############################################################################
# Constant                                                                    #
###############################################################################
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


###############################################################################
# Show Class                                                                  #
###############################################################################
class Show(object):

    def __init__(self):
        self.r = random.randrange(255)
        self.g = random.randrange(255)
        self.b = random.randrange(255)

    def show_digit(self, val: int, xd: int, yd: int) -> None:
        """show_digit

            Calculate position of leds on and off

            Attributes:
               : int <val> : number display
               : int <xd>  : width display
               : int <yd>  : height display
        """

        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p-offset) // 3
            ledmatrix.set_pixel( 
                xt+xd, 
                6-yt-yd, 
                self.r*NUMS[p], 
                self.g*NUMS[p], 
                self.b*NUMS[p]
            )
        ledmatrix.show()

    def show_letters_digits(self, val) -> None:
        """show_letters_digits

            Make the diffrence between int and str and call different function

            Attributes:
               : str or int <val> : number or letter
        """

        valStr = str(val)

        if re.search(valStr, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            switch = Switcher()
            switch.call_letters(val)
        else :
            value   = int(val)
            abs_val = abs(value)
            tens    = abs_val // 10
            units   = abs_val % 10
            if (abs_val > 9):
                self.show_digit(
                    tens, 
                    OFFSET_LEFT, 
                    OFFSET_TOP
                )

            self.show_digit(
                units, 
                OFFSET_LEFT+4, 
                OFFSET_TOP
            )

    def clean_display(self) -> None:
        """clean_display

            Function of ledmatrix to remove the old display

        """
        ledmatrix.clear()
        ledmatrix.show()


###############################################################################
# Switcher Class                                                              #
###############################################################################
class Switcher(object):

    def __init__(self):
        self.r              = random.randrange(255)
        self.g              = random.randrange(255)
        self.b              = random.randrange(255)

    def call_letters(self, argument: str):
        """call_letters

            Return and call the function corresponding to the letter 

            Attributes:
                : str <argument> : Letter call

        """

        method_name = 'show_' + argument
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid letter")
        # Call the method as we return it
        return method()

 
    def show_A(self) -> None:
        """show_A

            Position and parameters for letter A
            
        """
        #Vertical Droit
        ledmatrix.set_pixel(
            3 ,
            6 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] ,
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            2 ,
            5 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] ,
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            2 ,
            4 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] ,
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 ,
            3 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 ,
            2 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 ,
            1 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )

        #Vertical Gauche
        ledmatrix.set_pixel(
            4 ,
            5 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            4 ,
            4 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] ,
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            5 ,
            3 ,
            self.r*NUMS[1] ,
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel( 
            5 , 
            2 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel( 
            5 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] ,    
            self.b*NUMS[1]
        )

        #Horizontal
        ledmatrix.set_pixel( 
            2 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel( 
            3 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel( 
            4 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        #Show
        ledmatrix.show()
 
    def show_B(self) -> None:
        """show_B

            Position and parameters for letter B
            
        """

        #Vertical Droit
        ledmatrix.set_pixel(
            1 , 
            6 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            5 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            4 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            2 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 ,
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            0 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )

        #Vertical Gauche
        ledmatrix.set_pixel(
            2 , 
            6 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            3 , 
            5 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            2 , 
            4 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            2 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            3 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            4 , 
            2 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            4 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            3 , 
            0 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            2 , 
            0 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        #Show
        ledmatrix.show()
 
    def show_C(self) -> None:
        """show_C

            Position and parameters for letter C
            
        """

        #Vertical Droit
        ledmatrix.set_pixel(
            1 , 
            4 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            2 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )

        #Arc de Cercle
        ledmatrix.set_pixel(
            3 , 
            6 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            2 , 
            5 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        
        ledmatrix.set_pixel(
            2 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            3 , 
            0 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )

        #Horizontal
        ledmatrix.set_pixel(
            4 , 
            6 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            4 , 
            0 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        #Show
        ledmatrix.show()

    def show_L(self) -> None:
        """show_L

            Position and parameters for letter L

        """

        #Vertical
        ledmatrix.set_pixel(
            1 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            2 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            3 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            4 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 ,
            5 , 
            self.r*NUMS[1] ,
            self.g*NUMS[1] ,
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            1 , 
            6 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )

        #Horizontal
        ledmatrix.set_pixel(
            2 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            3 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        ledmatrix.set_pixel(
            4 , 
            1 , 
            self.r*NUMS[1] , 
            self.g*NUMS[1] , 
            self.b*NUMS[1]
        )
        #Show
        ledmatrix.show()
    

###############################################################################
# MAIN                                                                        #
###############################################################################
if __name__ == '__main__':
    ledmatrix.rotation(0)
    led.clean_display()

    led = Show()
    val = 0

    while True:
        if val <= 99:
            led.show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1

        if val > 99 and val < 104:
            led.clean_display()
            if val == 100:
                led.show_letters_digits('A')
                time.sleep(1)

            if val == 101:
                led.show_letters_digits('B')
                time.sleep(1)

            if val == 102:
                led.show_letters_digits('C')
                time.sleep(1)

            if val == 103:
                led.show_letters_digits('L')
                time.sleep(1)

            val = val + 1       
        if val >= 104:
            led.clean_display()
            val = 0 
            led.show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1

    led.clean_display()