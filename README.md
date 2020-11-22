# ADS1219_lib

ADS1219_lib is a Python library to use a ADS1219 with a Raspberry Pi. 
Development funded by [INRAE](https://www.inrae.fr/) (REVERSAAL research unit, Villeurbanne, France)

Github of the project : https://github.com/mickaelv/ADS1219-Python

## Installation

You can use this command to install ADS1219_lib easily :

```bash
git clone https://github.com/mickaelv/ADS1219-Python && cd ADS1219-Python && python3 setup.py install
```

Soon on pip Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ADS1219_lib :
```bash
pip install ADS1219_lib 
```

## Usage
```python
from ADS1219_lib import ADS1219
#
#Create a new object with interupt pin on GPIO 4
ads =  ADS1219( 1, 0x40, 4 )
#
#Set an external voltage reference of 2V
ads.setExternalReference( 2 )
#
#Define the gain to 4
ads.setGain( 4 )
#
#read inputs :
print( ads.convertToV( ads.readSingleEnded( 0 ) ) )
print( ads.convertToV( ads.readSingleEnded( 1 ) ) )
print( ads.convertToV( ads.readSingleEnded( 2 ) ) )
print( ads.convertToV( ads.readSingleEnded( 3 ) ) )
#
#
#Print the value of voltage between input 0 and 1
print( ads.convertToV( ads.readDifferential_0_1() ) )
#
#Print the value of voltage between input 2 and 3
print( ads.convertToV( ads.readDifferential_2_3() ) )
#
#Print the value of voltage between input 1 and 2
print( ads.convertToV( ads.readDifferential_1_2() ) )
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
