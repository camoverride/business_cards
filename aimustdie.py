import RPi.GPIO as GPIO
import os
import random
import time



# Text to be displayed on the card
TEXT = """
I\'m Cam Smith, a Seattle-
based artist whose work ex-
plores how AI is used for
surveillance and control.

I teamed up with Myke Walton,
a Biden-era AI policy expert,
to write AI MUST DIE. It\'s a
well-researched zine that pre
sents critical perspectives
on the way AI is talked about
governed, and owned in 2026.

Please take a look. If you'd
like more copies, let\'s get
in touch. They usually sell
for between $6 and $10.

There\'s alson an online ver-
sion you can share for free:

https://aimustdie.info

Thanks!


CAM SMITH
email : camoverride@gmail.com
IG    : camoverride
web   : https://smith.cam
"""



# Print the text
os.system(f"sudo sh -c 'echo \"{TEXT}\" > /dev/usb/lp0'")

# Print the image
pic_path = random.choice("PICS")
os.system(f"lp -d face_printer {pic_path}")
