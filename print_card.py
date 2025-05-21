import os
import time
import cv2



# Import image and text to print.
from cards import card_1 as DATA
TEXT = DATA["text"]
PIC_PATH = "_.png"
pic = cv2.imread(DATA["pic"])
pic = cv2.resize(pic, (130, 130))
cv2.imwrite(PIC_PATH, pic)





# Enable the printer.
os.system("sudo chmod 777 /dev/usb/lp0")



# # Print the text.
# os.system("sudo chmod 777 /dev/usb/lp0")
# os.system(f"sudo echo -e 'helo' > /dev/usb/lp0")
# time.sleep(0.5)
# text = "hello"
# cmd = f"echo -e '{text}' | sudo tee /dev/usb/lp0"
# os.system(cmd)

# Make sure we can write to the device
os.system("sudo chmod 777 /dev/usb/lp0")

# Send text using a subshell so redirection happens as root
os.system('sudo bash -c "echo -e \'hello\' > /dev/usb/lp0"')

# Print the image
os.system(f"lp -d face_printer {PIC_PATH}")
time.sleep(0.5)

# # Save the text to a temporary file
# with open("text.txt", "w") as f:
#     f.write(TEXT + "\n")

# # Print the text file
# os.system("lp -d face_printer text.txt")
