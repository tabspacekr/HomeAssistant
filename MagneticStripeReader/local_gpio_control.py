# prerequirement : sudo pip3 install OrangePi.GPIO
import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)         # set 3 as an output (RELAY)
GPIO.setup(5, GPIO.OUT)         # set 3 as an output (RELAY)

try:
    print ("Press CTRL+C to exit")
    while True:
        GPIO.output(3, 1)       # set port/pin value to 1/HIGH/True
        sleep(0.1)
        GPIO.output(3, 0)       # set port/pin value to 0/LOW/False
        sleep(0.1)

        GPIO.output(5, 1)       # set port/pin value to 1/HIGH/True
        sleep(0.1)
        GPIO.output(5, 0)       # set port/pin value to 0/LOW/False
        sleep(0.1)

        sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(3, 0)           # set port/pin value to 0/LOW/False
    GPIO.output(5, 0)           # set port/pin value to 0/LOW/False
    #GPIO.cleanup()              # Clean GPIO
    print ("Bye.")
