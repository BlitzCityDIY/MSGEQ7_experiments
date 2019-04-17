'''
Based on MicroPython code by linker3000 on GitHub
https://github.com/linker3000/micro-bit_spectrum
For use with a micro:bit board and an MSGEQ7

This iteration uses a Metro M4, MSGEQ7, MAX7219 & an 8x8 matrix
'''

from adafruit_max7219 import matrices
import board
from board import RX, TX
import busio
from digitalio import DigitalInOut, Direction
import time
from analogio import AnalogIn

msg7RESET = DigitalInOut(board.D3)
msg7RESET.direction = Direction.OUTPUT

msg7Strobe = DigitalInOut(board.D4)
msg7Strobe.direction = Direction.OUTPUT

msg7DCout = AnalogIn(board.A3) #  reset, strobe and DC out pins for MSGEQ7

clk = RX
din = TX
cs = DigitalInOut(board.A2) #  pins for the MAX7219

spi = busio.SPI(clk, MOSI=din)
display = matrices.Matrix8x8(spi, cs) #  SPI setup for MAX7219


baseVal = 21000 #  base value for use with some math in the loop. 21000 because it's divisible by 7

def getVoltage(pin):  
    return (pin.value) #  function to get the analog value from DC out

while True:
    msg7RESET.value = True
    time.sleep(.00001)
    msg7RESET.value = False #  resets the Reset pin on MSGEQ7
    
    display.brightness(3) #  brightness for the matrix
    

    for i in range(7): #  7 to send data to 7 rows/columns on matrix

        msg7Strobe.value = False #  begins strobe pin reset
        time.sleep(.00001)
        
        audioSample = getVoltage(msg7DCout) #  logs analog signal from DC out
        
        audioSample = audioSample - baseVal # subtracts 21000 from the analog input value
        
        audioSample = int(audioSample / ((baseVal) / 7)) #  since analog value has a max of 65353 this gets the value down to a range of 0 to 14
        
        if audioSample < 0:
            audioSample = 0 #  gets rid of any negative numbers
        if audioSample > 0:
            audioSample = audioSample / 2 #  gets the max range from 14 to 7
        
        if audioSample > 0: #  if/else statements for all 7 rows of the matrix
            display.pixel(0, i, 7)
            display.show()
        else:
            display.pixel(0, i, 0)
            display.show()

        if audioSample > 1:
            display.pixel(1, i, 7)
            display.show()
        else:
            display.pixel(1, i, 0)
            display.show()

        if audioSample > 2:
            display.pixel(2, i, 7)
            display.show()
        else:
            display.pixel(2, i, 0)
            display.show()
        if audioSample > 3:
            display.pixel(3, i, 7)
            display.show()
        else:
            display.pixel(3, i, 0)
            display.show()
            
        if audioSample > 4:
            display.pixel(4, i, 7)
            display.show()
        else:
            display.pixel(4, i, 0)
            display.show()
            
        if audioSample > 5:
            display.pixel(5, i, 7)
            display.show()
        else:
            display.pixel(5, i, 0)
            display.show()
            
        if audioSample > 6:
            display.pixel(6, i, 7)
            display.show()
        else:
            display.pixel(6, i, 0)
            display.show()
        print(audioSample)
        
        msg7Strobe.value = True #  sets Strobe high to complete the cycle. if/else statements have to be nested between the strobe reset
