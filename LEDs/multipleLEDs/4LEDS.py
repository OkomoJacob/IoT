"""
Alternate the flashing of the LEDs
"""
from gpiozero import LED
import time

tme = 1
#tme = float(input("Sleep for how many Seconds: "))
led1 = LED(4)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)

def alternateFlash():
    while True:
        led1.on()
        time.sleep(tme)
        led1.off()
        
        led2.off()
        time.sleep(tme)
        led2.on()
        
        led3.off()
        time.sleep(tme)
        led3.on()
        
        led4.off()
        time.sleep(tme)
        led4.on()
        
        led1.on(); led2.on(); led3.on(); led4.on();

alternateFlash()