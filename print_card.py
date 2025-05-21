import os
import time
import cv2



# Import image and text to print.
from cards import card_1 as DATA
PIC = cv2.imread(DATA["pic"])
PIC = cv2.resize(PIC, (130, 130))
TEXT = DATA["text"]


# Enable the printer.
os.system("sudo chmod 777 /dev/usb/lp0")

# Print the image
os.system(f"lp -d face_printer {PIC}")
time.sleep(0.5)

# Print the text.
os.system(f"sudo echo -e {TEXT} > /dev/usb/lp0")
time.sleep(0.5)
