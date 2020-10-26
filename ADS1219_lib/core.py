#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	The ``core`` module
	======================

	How to use ?
	------------------------

	Import the library with 

		from ADS1219_lib import ADS1219
	
	Create a new object with : 

		ads = new ADS1219(1, 0x40, 4)
	
	Have fun !

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


	def __write_command( self, cmd ):
		"""Wrapper to send data easly

		Parameters
		----------
		cmd : hex
 		 	command to send

		"""
		self.bus.write_byte( self.i2c_adr, cmd )



	def __read_registers( self, reg, size ):
		"""Wrapper to read data easly
		Parameters
		----------
		reg : hex
 		 	register to write

		size : int
			size of data

		Returns
		-------
		list
			Data read

		"""
		write = i2c_msg.write( self.i2c_adr, [reg] )
		read  = i2c_msg.read( self.i2c_adr, size )
		self.bus.i2c_rdwr( write, read )
		return list( read )


	def start( self ):
		"""Start the conversion"""
		self.__write_command( self.COMMAND_START_SYNC )

	def resetConfig( self ):
		"""Reset Chip"""
		self.config = 0x00
		self.gain = 1
		self.datarate = 20
		self.Vref = 2.048
		self.__write_command( self.COMMAND_RESET )

	def poweroff( self ):
		"""Power off the Chip"""
		self.__write_command( self.COMMAND_POWERDOWN )


	def __sendConfig ( self ):
		"""Send  config to the chip """
		self.bus.write_byte_data( self.i2c_adr, self.COMMAND_WREG, self.config )

	def setGain( self, gain ):
		"""
		Define the gain

		Parameters
		----------
		gain : int
 		 	value of the gain:  1 or 4 (default: 1)

		:Example:

			ads.setGain(4)

		"""
		self.config &= self.GAIN_MASK
		if ( gain == 4) : 
			self.config |= self.GAIN_4
			self.gain =  4
		elif( gain == 1) : 
			self.config |= self.GAIN_1
			self.gain =  1
		else : raise ValueError("'gain' can only be either 1 or 4")
		self.__sendConfig()

	def setDataRate( self, datarate ):
		"""
		Define the datarate

		Parameters
		----------
		datarate : int
 		 	value of the datarate:  20, 90, 330 or 1000 (default: 20)

		size : int
			size of data

		:Example:

			ads.setDataRate(1000)

		"""

		self.config &= self.DATA_RATE_MASK
		if( datarate == 20 ) : 
			self.config |= self.DATA_RATE_20
			self.datarate = 20
		elif( datarate == 90 ) : 
			self.config |= self.DATA_RATE_90
			self.datarate = 90
		elif( datarate == 330 ) : 
			self.config |= self.DATA_RATE_330
			self.datarate = 330
		elif( datarate == 1000 ) : 
			self.config |= self.DATA_RATE_1000
			self.datarate = 1000
		else : raise ValueError("'datarate' can only be either 20, 90, 330 or 1000")
		self.__sendConfig()


	def setSingleShot( self ):
		"""Configure the chip in Single Shot mode """
		self.config &= self.MODE_MASK
		self.config |= self.MODE_SINGLESHOT
		self.__sendConfig()

	def setContinuous( self ):
		"""Configure the chip in Continuous mode """
		self.config &= self.MODE_MASK
		self.config |= self.MODE_CONTINUOUS
		self.__sendConfig()

	def setExternalReference( self , value):
		"""Configure the chip with an external reference 

		Parameters
		----------
		value : float
 		 	value of the external reference

 		"""

		self.Vref = value
		self.config &= self.VREF_MASK
		self.config |= self.VREF_EXTERNAL
		self.__sendConfig()

	def setInternalReference( self ):
		"""Configure the chip with the internal reference """
		self.Vref = 2.048
		self.config &= self.VREF_MASK
		self.config |= self.VREF_INTERNAL
		self.__sendConfig()

	def readSingleEnded( self, channel ):
		"""
		Read a value from a specific channel

		Parameters
		----------
		channel : int
			channel number:  0 to 3

		:Example:

			ads.readSingleEnded(0)

		"""

		self.config &= self.MUX_MASK
		if( channel == 0 ) : self.config |= self.MUX_SINGLE_0
		elif( channel == 1 ) : self.config |= self.MUX_SINGLE_1
		elif( channel == 2 ) : self.config |= self.MUX_SINGLE_2
		elif( channel == 3 ) : self.config |= self.MUX_SINGLE_3
		else : raise ValueError("'channel' can only be either 0, 1, 2 or 3")
		self.__sendConfig()
		self.start()
		self.waitResult()
		return self.readConversionResult()


	def readConversionResult( self ):
		""" Get the result data from the chip """
		buffer = self.__read_registers( self.COMMAND_RDATA, 3 )
		value = (buffer[0]<<16) | (buffer[1]<<8) | (buffer[2])
		if value >= 0x800000:
			value = value-0x1000000
		return value

	def isReady( self ):
		""" Software function to get the moment who the data is available """
		value = self.__read_registers( self.COMMAND_RREG|4, 1 )
		return value[0] & 0x80


	def waitResult( self ):
		"""Blocking fonction to wait data"""
		if self.readyPin>0:
			GPIO.wait_for_edge( self.readyPin, GPIO.FALLING )
		else:
			while not self.isReady():
				sleep(0.0001)



	def readDifferential_0_1( self ):
		"""Read a value between 0 and 1 channel"""
		self.config &= self.MUX_MASK
		self.config |= self.MUX_DIF_0_1
		self.__sendConfig()
		self.start()
		self.waitResult()
		return self.readConversionResult()

	def readDifferential_1_2( self ):
		"""Read a value between 1 and 2 channel"""
		self.config &= self.MUX_MASK
		self.config |= self.MUX_DIF_1_2
		self.__sendConfig()
		self.start()
		self.waitResult()
		return self.readConversionResult()

	def readDifferential_2_3( self ):
		"""Read a value between 2 and 3 channel"""
		self.config &= self.MUX_MASK
		self.config |= self.MUX_DIF_2_3
		self.__sendConfig()
		self.start()
		self.waitResult()
		return self.readConversionResult()


	def readShorted( self ):
		"""
		Set the chip to get an offset to calibrate

		.. note:: Please refer to 8.3.7 in the datasheet ( https://www.ti.com/lit/ds/sbas924a/sbas924a.pdf )

		"""

		self.config &= self.MUX_MASK
		self.config |= self.MUX_SHORTED
		self.__sendConfig()
		self.start()
		self.waitResult()
		return self.readConversionResult()

	def convertToV(self, value):
		"""Function to convert the value in Volt using Gain and Vref. 
		Parameters
		----------
		value : float
			Value to convert

		Returns
		---------
		float 
			Value in V.
		"""
		return  ( self.Vref / self.gain ) * ( value / pow(2,23) ) 

	def __init__( self, port=1, address=0x40, readyPin=0 ):
		"""
		Constructor
		Parameters
		----------
		port : int
			I2C port, for raspberry with port 2 and 3 please set to port=1
		address : hex
			I2C adress of the chip. Default is 0x40
		readyPin: int
			Input pin of the raspberry to know if data is available. 0 to desactivate and use software information
		:Example:

			ads = ADS1219(1, 0x40, 4)

		"""

		self.i2c_adr = address
		self.bus = SMBus( port, True )
		self.readyPin = readyPin
		self.config = 0x00
		self.gain = 1
		self.datarate = 20
		self.Vref = 2.048
		if( readyPin>0 ):
			GPIO.setmode( GPIO.BCM )
			GPIO.setup(readyPin, GPIO.IN )

	def __enter__( self ):
		"""Enter function"""
		return self

	def __del__( self ):
		"""Delete function"""
		self.bus.close()

	def __exit__( self, exc_type, exc_value, traceback ):
		"""Exit function"""
		self.bus.close()

