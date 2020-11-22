#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import ADS1219_lib


setup(

	name='ADS1219_lib',

	# la version du code
	version=ADS1219_lib.__version__,
	packages=find_packages(),
	author="Mickaël Veleine",
	author_email="contact@mickaelv.fr",
	description="Lib to use ADS1219 with Python on Raspberry",
	long_description_content_type='text/markdown',
	long_description=open('README.md').read(),
	install_requires= ["RPi.GPIO", "smbus2"],
	include_package_data=True,
	url='https://github.com/mickaelv/ADS1219-Python',
	classifiers=[
		"Programming Language :: Python",
		"Development Status :: 2 - Pre-Alpha",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Topic :: System :: Hardware :: Hardware Drivers",
	],


)
