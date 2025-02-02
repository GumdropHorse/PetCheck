from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
  while True:
    print("\nHold a tag near the reader to clear contents.")
    id, text = reader.read()
    
    write_str = ""
    reader.write(write_str)
    print("clearing...\nSuccessfully cleared.")
    
    sleep(2)

except KeyboardInterrupt:
  print("stopping")
  GPIO.cleanup()
  raise
