#! /usr/bin/python3
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

REGEXP = r"(^[a-zA-Z]*)"

R = random.randrange(255)
G = random.randrange(255)
B = random.randrange(255)

A = [ ]
B = [ ]
C = [ ]
D = [ ]
E = [ ]
F = [ ]
G = [ ]
H = [ ]
I = [ ]
J = [ ]
K = [ ]
L = [#Vertical
	ledmatrix.set_pixel( 6 , 1 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 6 , 2 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 6 , 3 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 6 , 4 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 6 , 5 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 6 , 6 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	#Horizontal
	ledmatrix.set_pixel( 6 , 1 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 5 , 1 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 4 , 1 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1]),
	ledmatrix.set_pixel( 3 , 1 , R*NUMS[1] , G*NUMS[1] , B*NUMS[1])]
M = [ ]
N = [ ]
O = [ ]
P = [ ]
Q = [ ]
R = [ ]
S = [ ]
T = [ ]
U = [ ]
V = [ ]
W = [ ]
X = [ ]
Y = [ ]
Z = [ ]

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
		ledmatrix.set_pixel( xt+xd , 6-yt-yd , R*NUMS[p] , G*NUMS[p] , 
			B*NUMS[p])
	ledmatrix.show()

def show_letters_digits(val):
	"""show_letters_digits

		Calculate number of 

		Attributes:
			val : number or letter
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
		show_digit(tens, OFFSET_LEFT, OFFSET_TOP, R, G, B)
	show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, R, G, B)

def show_L():
	
	for i in range (L):
		L[i]
	ledmatrix.show()
	


###############################################################################
# MAIN																		  #
###############################################################################
if __name__ == '__main__':
	ledmatrix.rotation(0)
	ledmatrix.clear()

	val = 0

	while True:
		show_L(colorR, colorG, colorB)
		"""if val <= 99:
			show_letters_digits(val)
			time.sleep(0.1)
			val = val + 1
		if val > 99:
			ledmatrix.clear()
			ledmatrix.show()
			val = 0 
			R = random.randrange(255)
			G = random.randrange(255)
			B = random.randrange(255)
			show_letters_digits(val)
			time.sleep(0.1)
			val = val + 1"""

	ledmatrix.clear()
	ledmatrix.show()