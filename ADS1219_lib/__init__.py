#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	The ``ADS1219_lib`` package
	======================

	Use it to use ADS1219 with à raspberry Pi.


	Wirering
	-------------------

	SDA 	: Pin 3 (GPIO 2)

	SCL 	: Pin 5 (GPIO 3)

	Ready 	: Pin 7 (GPIO 4)

	GND 	: Pin 39

	3.3V	: Pin 1



	.. warning:: Use the correct voltage to avoid problem with the chip.

	How to use ?
	------------------------

	Import the library with 

		from ADS1219_lib import ADS1219
	
	Create a new object with : 

		ads = new ADS1219(1, 0x40, 4)
	
	Have fun !

	.. note:: Want more examples ? See Examples folder


 	Licence
	------------------------

	MIT License
	-----------

	Copyright (c) 2020 Mickaël Veleine ( https://mickaelv.fr )
	Development funded by INRAE (REVERSAAL research unit, Villeurbanne, France)

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
__version__ = "0.0.2"
from .core import ADS1219
