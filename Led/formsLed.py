#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Display different forms on the pi-topPULSE led matrix
#
# Based on the script to display digits on pi-topPULSE

import ptpulse
from ptpulse import ledmatrix

import re

import time

OFFSET_LEFT = 0
OFFSET_TOP = 2

NUMS = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,  # 0
        0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,  # 1
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,  # 2
        1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 3
        1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 4
        1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 5
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 6
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,  # 7
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 8
        1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]  # 9

REGEXP = r"(^[a-zA-Z]*)"



def show_digit(val, xd, yd, r, g ,b):
	"""show_digit

		Calculate position of leds on and off

		Attributes:
			val : number display
			xd  : width display
			yd  : height display
			r 	: red value
			g	: green value
			b   : blue value
	"""

	offset = val * 15
	for p in range(offset, offset + 15):
		xt = p % 3
		yt = (p-offset) // 3
		ledmatrix.set_pixel( xt+xd , 7-yt-yd , r*NUMS[p] , g*NUMS[p] , 
			b*NUMS[p])
	ledmatrix.show()

def show_letters_digits(val, r, g, b):
	"""show_letters_digits

		Calculate number of 

		Attributes:
			val : number or letter
			r 	: red value
			g	: green value
			b   : blue value
	"""

	"""if re.match(REGEXP, val) is not None:
		abs_val = ord(val)
		print (abs_val)
	else :"""
	value 	= int(val)
	abs_val = abs(value)
	tens 	= abs_val // 10
	units 	= abs_val % 10
	if (abs_val > 9):
		show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
	show_digit(units, OFFSET_LEFT+2, OFFSET_TOP, r, g, b)
	


###############################################################################
# MAIN																		  #
###############################################################################
if __name__ == '__main__':
	ledmatrix.rotation(0)
	ledmatrix.clear()

	val = 0

	while True:
		show_letters_digits(val, 255, 0, 150)
		time.sleep(0,5)
		val = val + 1

	ledmatrix.clear()
	ledmatrix.show()