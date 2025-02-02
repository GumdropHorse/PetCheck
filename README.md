# PetCheck
Application to track when an animal has gone to eat at it's food bowl, or drink at it's water bowl. For use with a RFID-RC522 raspberry pi setup.
This project can be used for pets and livestock alike.


# Requirements
- Must have a RFID-RC522 sensor connected to a raspberry pi.
  - Wiring setup:
    - 3.3 RFID -> pin 17 Raspberry Pi
    - RST RFID -> pin 22 Raspberry Pi red
    - GND RFID -> pin 25 Raspberry Pi
    - RG RFID -> skip, do not attach to anything
    - MISO RFID -> pin 21 Raspberry Pi
    - MOSI RFID -> pin 19 Raspberry Pi
    - SCK RFID -> pin 23 Raspberry Pi
    - SDA RFID -> pin 24 Raspberry Pi
  - Note:
    We used a breadboard to handle the connections on the RFID sensor side of things, and sottering the pins to the sensor before putting it in the breadboard was required. The connection was not stable enough otherwise.
- Must have a rasberry pi connected to a monitor, keyboard and mouse

# Instructions
- Upload main.py and clear.py to your raspberry pi
- Open a terminal and run main.py with: Python3 main.py
- Hold an empty RFID tag up to the sensor, and follow the prompts to register your animal.
  NOTE: Do not inculde the character '|' in any of your responses
- Attach the RFID sensor to your pet's collar. When you pet eats, you will receive an email
- If you need to exit the program, press ctrl-c in the terminal to quit.
- If you would like to clear a tag of a registered pet, run clear.py instead with: Python3 clear.py
- Next, hold the tag you would like to clear up to the sensor.
- If you need to exit the program, press ctrl-c in the terminal to quit.

# Notes
Tags are written to in the following format: |Name|Species|Email||
Most tags have limited storage space. If you face issues receiving emails, clear your tag and try using less character for the name and species.
