import time
import array
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import pulseio

msg7RESET = DigitalInOut(board.D7)
msg7RESET.direction = Direction.OUTPUT

msg7Strobe = DigitalInOut(board.D9)
msg7Strobe.direction = Direction.OUTPUT

msg7DCout = AnalogIn(board.A0)

ledpins = [board.D3, board.D4, board.D5, board.D6, board.D13, board.D11, board.D12]

leds = []

for pin in ledpins:
    led = pulseio.PWMOut(pin, frequency=5000, duty_cycle=0)
    leds.append(led)
    
def getVoltage(pin):  
    return (pin.value)
    
while True:

        msg7RESET.value = True
        time.sleep(.0005)
        msg7RESET.value = False

        #  print("Analog Voltage: %f" % getVoltage(msg7DCout))
               
        for i in range(0, 7):

            msg7Strobe.value = False
            time.sleep(.00007)	#  .035 / 500
        
            leds[i].duty_cycle = int (getVoltage(msg7DCout))
            
            msg7Strobe.value = True
