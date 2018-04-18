#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

"""
MIT License
Copyright (c) 2018 Florian VAISSIERE [https://github.com/FlorianVaissiere]

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

"""
    Display different forms on the pi-topPULSE led matrix
    Based on the script to display digits on pi-topPULSE
"""

###############################################################################
# Import                                                                      #
###############################################################################
import ptpulse
from ptpulse import ledmatrix

import random
from random import randrange  # FIXME unused

import re
from re import search  # FIXME unused

import time
from time import sleep  # FIXME unused

###############################################################################
# Constant                                                                    #
###############################################################################
# Grid border
OFFSET_LEFT = 0
OFFSET_TOP = 1

# Sleep
S1 = 1  # 1 second

# Start const
START_LETTER_VALUE = 65
START_DIGIT_VALUE = 0

"""
    Digits Code Table
"""
NUMS = [1, 1, 1,   1, 0, 1,   1, 0, 1,   1, 0, 1,   1, 1, 1,  # 0
        0, 1, 0,   0, 1, 0,   0, 1, 0,   0, 1, 0,   0, 1, 0,  # 1
        1, 1, 1,   0, 0, 1,   0, 1, 0,   1, 0, 0,   1, 1, 1,  # 2
        1, 1, 1,   0, 0, 1,   1, 1, 1,   0, 0, 1,   1, 1, 1,  # 3
        1, 0, 0,   1, 0, 1,   1, 1, 1,   0, 0, 1,   0, 0, 1,  # 4
        1, 1, 1,   1, 0, 0,   1, 1, 1,   0, 0, 1,   1, 1, 1,  # 5
        1, 1, 1,   1, 0, 0,   1, 1, 1,   1, 0, 1,   1, 1, 1,  # 6
        1, 1, 1,   0, 0, 1,   0, 1, 0,   1, 0, 0,   1, 0, 0,  # 6
        1, 1, 1,   1, 0, 1,   1, 1, 1,   1, 0, 1,   1, 1, 1,  # 8
        1, 1, 1,   1, 0, 1,   1, 1, 1,   0, 0, 1,   0, 0, 1   # 9
        ]

"""
    Letters Code Table
"""
LETTERS = [1, 1, 1,   1, 0, 1,   1, 1, 1,   1, 0, 1,   1, 0, 1, # A
    	   1, 0, 0,   1, 0, 0,   1, 1, 1,   1, 0, 1,   1, 1, 1, # B
           0, 0, 0,   1, 1, 1,   1, 0, 0,   1, 0, 0,   1, 1, 1, # C
           0, 0, 1,   0, 0, 1,   1, 1, 1,   1, 0, 1,   1, 1, 1, # D
           1, 1, 1,   1, 0, 0,   1, 1, 0,   1, 0, 0,   1, 1, 1, # E
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
ALPHABET = {
            letter: nb
            for letter, nb
            in zip(
                [chr(65+x) for x in range(26)],
                [x for x in range(26)]
            )
        }


###############################################################################
# Show Class                                                                  #
###############################################################################
class Show(object):

    def __init__(self):
        self.r = random.randrange(50, 255)
        self.g = random.randrange(50, 255)
        self.b = random.randrange(50, 255)

    def show_digit(self, val: int, xd: int, yd: int) -> None:
        """show_digit

            Calculate position of leds on and off

            Attributes:
               :param <val> : (int) number display
               :param <xd>  : (int) width display
               :param <yd>  : (int) height display

        """

        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p - offset) // 3
            ledmatrix.set_pixel(
                xt + xd,
                6 - yt - yd,
                self.r * NUMS[p],
                self.g * NUMS[p],
                self.b * NUMS[p]
            )
        ledmatrix.show()

    def show_letters(self, val: int, xd: int, yd: int) -> None:
        """show_digit

            Calculate position of leds on and off

            Attributes:
               :param <val> : (int) number display
               :param <xd>  : (int) width display
               :param <yd>  : (int) height display
        """

        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p - offset) // 3
            ledmatrix.set_pixel(
                xt + xd,
                6 - yt - yd,
                self.r * LETTERS[p],
                self.g * LETTERS[p],
                self.b * LETTERS[p]
            )
        ledmatrix.show()

    def show_letters_digits(self, val: int, int_str: bool) -> None:
        """show_letters_digits

            Make the diffrence between int and str and call different function

            Attributes:
               :param <val>     : (int) number or letter
               :param <int_str> : (bool) define if it's int or str
        """

        if int_str:
            self.show_letters(ALPHABET[chr(val)], OFFSET_LEFT + 2, OFFSET_TOP)

        else:
            abs_val = abs(val)
            tens = abs_val // 10
            units = abs_val % 10
            if abs_val > 9:
                self.show_digit(
                    tens,
                    OFFSET_LEFT,
                    OFFSET_TOP
                )

            self.show_digit(
                units,
                OFFSET_LEFT + 4,
                OFFSET_TOP
            )

    @staticmethod
    def clean_display() -> None:
        """clean_display

            Function of ledmatrix to remove the old display

        """

        ledmatrix.clear()
        ledmatrix.show()


###############################################################################
# MAIN                                                                        #
###############################################################################
if __name__ == '__main__':

    led = Show()
    val = START_DIGIT_VALUE
    val_letter = START_LETTER_VALUE

    ledmatrix.rotation(0)
    led.clean_display()

    while True:
        led.clean_display()
        if val <= 99:
            led.show_letters_digits(val, False)
            val += 1

        elif 99 < val < 126:
            led.show_letters_digits(val_letter, True)
            val_letter += 1
            val += 1

        else:
            val_letter = START_LETTER_VALUE
            val = START_DIGIT_VALUE

        time.sleep(S1)