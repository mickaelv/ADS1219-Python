#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ADS1219_lib import ADS1219

#Create a new object with interupt pin on GPIO 4:
ads =  ADS1219( 1, 0x40, 4 )

#Set an external voltage reference of 2V
ads.setExternalReference( 2 )

#Define the gain to 4
ads.setGain( 4 )

#read inputs :
print( ads.convertToV( ads.readSingleEnded( 0 ) ) )
print( ads.convertToV( ads.readSingleEnded( 1 ) ) )
print( ads.convertToV( ads.readSingleEnded( 2 ) ) )
print( ads.convertToV( ads.readSingleEnded( 3 ) ) )


#Print the value of voltage between input 0 and 1
print( ads.convertToV( ads.readDifferential_0_1() ) )

#Print the value of voltage between input 2 and 3
print( ads.convertToV( ads.readDifferential_2_3() ) )

#Print the value of voltage between input 1 and 2
print( ads.convertToV( ads.readDifferential_1_2() ) )


