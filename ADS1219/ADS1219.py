#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
	The ``ADS1219`` module
	======================
 
	How to use ?
	------------------------
 
	Import the library with import ADS129
	Create a new object with : ADS1219 = new ADS1219(1, 0x40, 3)
	Have fun !

	.. note:: Want more exemple ? See examples folder
 
 	Licence 
	------------------------

	MIT License
	-----------

	Copyright (c) 2020 Mickaël Veleine ( https://mickaelv.fr ) with
	the support of INREA ( Unité REVERSAAL at Villeurbanne )

	Permission is hereby granted, free of charge, to any person
	obtaining a copy of this software and associated documentation
	files (the "Software"), to deal in the Software without
	restriction, including without limitation the rights to use,
	copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the
	Software is furnished to do so, subject to the following
	conditions:

	The above copyright notice and this permission notice shall be
	included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
	OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
	NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
	HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
	OTHER DEALINGS IN THE SOFTWARE.
			
"""

import RPi.GPIO as GPIO
from time import sleep
from smbus2 import SMBus, i2c_msg

class ADS1219:

	COMMAND_RESET 				= 0x06
	COMMAND_START_SYNC 			= 0x08
	COMMAND_POWERDOWN 			= 0x02
	COMMAND_RDATA 				= 0x10
	COMMAND_RREG 				= 0x20
	COMMAND_WREG 				= 0x40

	MUX_MASK 					= 0x1F
	MUX_DIF_0_1 				= 0x00
	MUX_DIF_2_3 				= 0x20
	MUX_DIF_1_2 				= 0x40
	MUX_SINGLE_0 				= 0x60
	MUX_SINGLE_1 				= 0x80
	MUX_SINGLE_2 				= 0xa0
	MUX_SINGLE_3 				= 0xc0
	MUX_SHORTED					= 0xe0

	GAIN_MASK					= 0xF3
	GAIN_ONE 					= 0x00
	GAIN_FOUR 					= 0x10

	DATA_RATE_MASK 				= 0xF3
	DATA_RATE_20 				= 0x00
	DATA_RATE_90 				= 0x04
	DATA_RATE_330 				= 0x08
	DATA_RATE_1000				= 0x0c

	MODE_MASK					= 0xFD
	MODE_SINGLESHOT				= 0x00
	MODE_CONTINUOUS 			= 0x02

	VREF_MASK					= 0xFE
	VREF_INTERNAL 				= 0x00
	VREF_EXTERNAL 				= 0x01


