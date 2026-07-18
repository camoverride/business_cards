"""
Run the code as follows:

    python aimustdie.py --num_copies 10 --pause 2
"""
import argparse
import os
import time



# Get the number of copies.
parser = argparse.ArgumentParser()
parser.add_argument("--num_copies", type=int)
parser.add_argument("--pause", type=int)


args = parser.parse_args()


# Text to be displayed on the card
TEXT = """
I'm Cam Smith, a Seattle-based artist whose work explores how AI is used for surveillance and control.

I teamed up with Myke Walton, a Biden-era AI policy expert, to write AI MUST DIE. It's a well-researched zine that presents critical perspectives on the way AI is talked about, governed, and owned in 2026.

Please take a look. If you'd like more copies, let 's get in touch. They usually sell for between $6 and $10.

There's also an online version you can share for free:

https://aimustdie.info

Thanks!


CAM SMITH
email : camoverride@gmail.com
IG    : @camoverride
site  : https://smith.cam
"""


for _ in range(args.num_copies):

    with open("/dev/usb/lp0", "wb") as printer:

        # Enable the printer.
        os.system(f"sudo chmod 777 /dev/usb/lp0")

        # Print the text.
        printer.write(TEXT.encode("utf-8"))
        printer.write(b"\n\n\n")

        # Wait a little bit.
        time.sleep(args.pause)
