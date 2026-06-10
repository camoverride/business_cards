import RPi.GPIO as GPIO
import os
import random
import time



# Text to be displayed on the card
TEXT = """
CAM SMITH
email : camoverride@gmail.com
IG    : camoverride
web   : https://smith.cam
"""

# Picture to be displayed on the card.
PICS = [
    "pics/cam1.png",
    "pics/cam2.jpg",
    "pics/cam3.jpg",
    "pics/cam4.jpg",
    "pics/cam5.jpg",
    "pics/cam6.jpg",
    "pics/cam7.jpg",
]



# Print the text
os.system(f"sudo sh -c 'echo \"{TEXT}\" > /dev/usb/lp0'")

# Print the image
pic_path = random.choice(PICS)
os.system(f"lp -d face_printer {pic_path}")
