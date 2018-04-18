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
from random import randrange

import re
from re import search

import time
from time import sleep


###############################################################################
# Constant                                                                    #
###############################################################################
# Grid border
OFFSET_LEFT = 0
OFFSET_TOP = 1

# Sleep
S1  = 1     # 1 second
M1S = 0.1   # Less than 1 second

"""
    Digits Code Table
"""
NUMS = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,  # 0
        0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,  # 1
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,  # 2
        1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 3
        1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 4
        1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 5
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 6
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,  # 6
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 8
        1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1   # 9
    ]

"""
    Letters Code Table
"""
LETTERS = [ 1, 1, 1,   1, 0, 1,   1, 1, 1,   1, 0, 1,   1, 0, 1, # A
    	    1, 0, 0,   1, 0, 0,   1, 1, 1,   1, 0, 1,   1, 1, 1, # B
            0, 0, 0,   1, 1, 1,   1, 0, 0,   1, 0, 0,   1, 1, 1, # C
            0, 0, 1,   0, 0, 1,   1, 1, 1,   1, 0, 1,   1, 1, 1, # D
            1, 1, 1,   1, 0, 0,   1, 1, 1,   1, 0, 0,   1, 1, 1, # E
    	    1, 1, 1,   1, 0, 0,   1, 1, 0,   1, 0, 0,   1, 0, 0, # F
            0, 1, 0,   1, 0, 1,   0, 1, 1,   1, 0, 1,   0, 1, 0, # G
            1, 0, 1,   1, 0, 1,   1, 1, 1,   1, 0, 1,   1, 0, 1, # H
            1, 1, 1,   0, 1, 0,   0, 1, 0,   0, 1, 0,   1, 1, 1, # I
            0, 0, 1,   0, 0, 0,   0, 0, 1,   0, 0, 1,   0, 1, 1, # J
            1, 0, 0,   1, 0, 0,   1, 0, 1,   1, 1, 0,   1, 0, 1, # K
            1, 0, 0,   1, 0, 0,   1, 0, 0,   1, 0, 0,   1, 1, 1, # L
            1, 0, 1,   1, 1, 1,   1, 0, 1,   1, 0, 1,   1, 0, 1, # M
            0, 0, 0,   0, 0, 0,   1, 1, 1,   1, 0, 1,   1, 0, 1, # N
    	    1, 1, 1,   1, 0, 1,   1, 0, 1,   1, 0, 1,   1, 1, 1, # O
    	    1, 1, 1,   1, 0, 1,   1, 1, 1,   1, 0, 0,   1, 0, 0, # P
    	    1, 1, 1,   1, 0, 1,   1, 1, 1,   0, 0, 1,   0, 0, 1, # Q
    	    1, 1, 0,   1, 0, 1,   1, 1, 0,   1, 0, 1,   1, 0, 1, # R
    	    0, 1, 1,   1, 0, 0,   0, 1, 0,   0, 0, 1,   1, 1, 0, # S
    	    0, 0, 0,   1, 1, 1,   0, 1, 0,   0, 1, 0,   0, 1, 0, # T
    	    0, 0, 0,   1, 0, 1,   1, 0, 1,   1, 0, 1,   1, 1, 1, # U
    	    0, 0, 0,   1, 0, 1,   1, 0, 1,   1, 0, 1,   0, 1, 0, # V
    	    1, 0, 1,   1, 0, 1,   1, 0, 1,   1, 1, 1,   1, 0, 1, # W
    	    1, 0, 1,   1, 0, 1,   0, 1, 0,   1, 0, 1,   1, 0, 1, # X
    	    1, 0, 1,   1, 0, 1,   0, 1, 0,   0, 1, 0,   0, 1, 0, # Y
    	    1, 1, 1,   0, 0, 1,   0, 1, 0,   1, 0, 0,   1, 1, 1  # Z
	    ]

"""
    Dictionary allowing the choice of the line to read
"""
ALPHABET = {'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 
            'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 
            'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 
            'Z':25 
        }


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

    def show_letters(self, val: int, xd: int, yd: int) -> None:
        """show_digit

            Calculate position of leds on and off

            Attributes:
               : int <val> : number display
               : int <xd>  : width display
               : int <yd>  : height display
        """
        print(val)
        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p-offset) // 3
            ledmatrix.set_pixel( 
                xt+xd, 
                6-yt-yd, 
                self.r*LETTERS[p], 
                self.g*LETTERS[p], 
                self.b*LETTERS[p]
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
            self.show_letters(ALPHABET[val], OFFSET_LEFT+2, OFFSET_TOP)

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
# MAIN                                                                        #
###############################################################################
if __name__ == '__main__':
    ledmatrix.rotation(0)
    ledmatrix.clear()

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
                led.show_letters_digits('D')
                time.sleep(1)

            if val == 104:
                led.show_letters_digits('E')
                time.sleep(1)

            if val == 105:
                led.show_letters_digits('F')
                time.sleep(1)

            if val == 106:
                led.show_letters_digits('G')
                time.sleep(1)

            if val == 107:
                led.show_letters_digits('H')
                time.sleep(1)

            if val == 108:
                led.show_letters_digits('I')
                time.sleep(1)

            if val == 109:
                led.show_letters_digits('J')
                time.sleep(1)

            if val == 110:
                led.show_letters_digits('K')
                time.sleep(1)

            if val == 111:
                led.show_letters_digits('L')
                time.sleep(1)

            if val == 112:
                led.show_letters_digits('M')
                time.sleep(1)

            if val == 113:
                led.show_letters_digits('N')
                time.sleep(1)

            if val == 114:
                led.show_letters_digits('O')
                time.sleep(1)

            if val == 115:
                led.show_letters_digits('P')
                time.sleep(1)

            if val == 116:
                led.show_letters_digits('Q')
                time.sleep(1)

            if val == 117:
                led.show_letters_digits('R')
                time.sleep(1)

            if val == 118:
                led.show_letters_digits('S')
                time.sleep(1)

            if val == 119:
                led.show_letters_digits('T')
                time.sleep(1)

            if val == 120:
                led.show_letters_digits('U')
                time.sleep(1)

            if val == 121:
                led.show_letters_digits('V')
                time.sleep(1)

            if val == 122:
                led.show_letters_digits('W')
                time.sleep(1)

            if val == 123:
                led.show_letters_digits('X')
                time.sleep(1)

            if val == 124:
                led.show_letters_digits('Y')
                time.sleep(1)

            if val == 125:
                led.show_letters_digits('Z')
                time.sleep(1)

            val = val + 1       
        if val >= 126:
            led.clean_display()
            val = 0 
            led.show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1

    led.clean_display()
