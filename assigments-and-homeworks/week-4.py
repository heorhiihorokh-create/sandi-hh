import smbus
from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

i2c = smbus.SMBus(1)
ADC_address = 0x48

commands_per_channel = {
    2: 0b1001,
    3: 0b1101,
}

channel = 2

try:
    while True:
        i2c.write_byte(ADC_address, (commands_per_channel[channel] << 4) | 0x04)

        analog_value = i2c.read_byte(ADC_address)
        voltage = analog_value * 3.3 / 255

        print(f"Channel {channel} has value: {analog_value} and in volt this is {voltage:.3f}")
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    i2c.close()
    GPIO.cleanup()