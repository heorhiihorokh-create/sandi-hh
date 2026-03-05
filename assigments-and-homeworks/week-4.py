# assigment week 4

import smbus
from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

i2c = smbus.SMBus(1)

ADC_adress = 0x48

commands_per_channel = {
    #..
    2: 0b1001,
    3: 0b1101,
    #..
}

channel = 2

try:
    while True:
        i2c.write_bute(ADC_adress,(commands_per_channel[channel]<<4) | 0x4)

        analog_value = i2c.read_byte(ADC_adress)

        print("Channel 2 has  value of : {} and in volt this is {}".format(analog_value, analog_value / 255 *3.3))
        time.sleep(1)


except KeyboardInterrupt as e:
    pass
finally:
    i2c.close()
    del i2c
    GPIO.cleanup()