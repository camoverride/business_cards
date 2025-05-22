import RPi.GPIO as GPIO
import os
import time
import cv2



# Set the GPIO pin number (using BCM numbering)
BUTTON_PIN = 17  # GPIO17, physical pin 11

# Must wait this long before a new print is allowed. Min 5 for CUPS to reset.
DELAY = 5

# Import image and text to print.
from cards import card_1 as DATA
TEXT = DATA["text"]
PIC_PATH = "_.png"
pic = cv2.imread(DATA["pic"])
pic = cv2.resize(pic, (130, 130))
cv2.imwrite(PIC_PATH, pic)

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the pin as an input WITHOUT internal pull-up/down (we're using an external one)
GPIO.setup(BUTTON_PIN, GPIO.IN)


print("Press the button. Press Ctrl+C to exit.")

try:
    while True:
        # Detect button press.
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:

            # Print the text.
            os.system("sudo chmod 777 /dev/usb/lp0")
            os.system(f"sudo echo -e {TEXT} > /dev/usb/lp0")

            # Print the image
            os.system(f"lp -d face_printer {PIC_PATH}")

        # Delay between button presses.
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("Exiting")

finally:
    GPIO.cleanup()
