import RPi.GPIO as GPIO
import os
import time
import cv2



# Set the GPIO pin number (using BCM numbering)
BUTTON_PIN = 17  # GPIO17, physical pin 11

# Must wait this long before a new print is allowed.
DELAY = 3

# Import image and text to print.
from cards import card_1 as DATA
PIC = cv2.resize(DATA["pic"], (130, 130))
TEXT = DATA["text"]

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the pin as an input WITHOUT internal pull-up/down (we're using an external one)
GPIO.setup(BUTTON_PIN, GPIO.IN)


print("Press the button. Press Ctrl+C to exit.")

try:
    while True:
        # Detect button press.
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:

            # Enable the printer.
            os.system("sudo chmod 777 /dev/usb/lp0")

            # Print the image
            os.system(f"lp -d face_printer {PIC}")
            time.sleep(0.5)

            # Print the text.
            os.system(f"sudo echo -e {TEXT} > /dev/usb/lp0")
            time.sleep(0.5)

        # Delay between button presses.
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("Exiting")

finally:
    GPIO.cleanup()
