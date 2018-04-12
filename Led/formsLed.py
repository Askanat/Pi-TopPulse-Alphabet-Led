#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Display different forms on the pi-topPULSE led matrix
#
# Based on the script to display digits on pi-topPULSE

import ptpulse
from ptpulse import ledmatrix

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


def show_letter(val, xd, yd, r, g ,b):
	"""show_A

		Use pi-topPulse led board to show one selected letter

		Attributes:
			val : if number or letter value
			xd  : width display
			yd  : height display
			r 	: red value
			g	: green value
			b   : blue value

	"""

	offset = val
	for p in range(offset, offset + 15):
		xt = p % 3
		yt = (p-offset) // 3
		ledmatrix.set_pixel( xt+xd , 5-yt-yd , r*NUMS[p] , g*NUMS[p] , 
			b*NUMS[p])
	ledmatrix.show()

def show_letters(val, r, g, b):
	abs_val = ord(val)
	tens 	= abs_val // 10
	units 	= abs_val % 10
	if (abs_val > 9):
		show_letter(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
	show_letter(units, OFFSET_LEFT+2, OFFSET_TOP, r, g, b)


###############################################################################
# MAIN																		  #
###############################################################################

ledmatrix.rotation(0)
ledmatrix.clear()

while True:
	show_letters('A', 255, 255, 255)

ledmatrix.clear()
ledmatrix.show()