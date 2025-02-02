from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import smtplib
from email.message import EmailMessage

def send_email(rec, subject, body):
  me = "petcheckdev@gmail.com"
  you = rec
  msg = EmailMessage()
  
  msg.set_content(body)
  msg['Subject'] = subject
  msg['From'] = me
  msg['To'] = you
  
  s = smtplib.SMTP("smtp.gmail.com",587) #587 uses gmail severs
  s.starttls() # uses TLS connection
  s.login(me, "xkql oqtm guoh kbyt")
  
  s.send_message(msg)
  s.quit()

reader = SimpleMFRC522()
try:
  while True:
    print("\nHold a tag near the reader")
    id, text = reader.read()
    
    if text[0] != "|": # if pet is not registered
      print("Please register your animal.")
      name = input("Enter animal's name: ")
      species = input("Enter animal's species: ")
      email = input("Enter your email: ")
      
      write_str = "|" + name + "|" + species + "|" + email + "||"
      print(\nPlease hold tag near reader.\nRegistering...")
      reader.write(write_str)
      print("Animal successfully registered")
    else: # if pet is registered
      print("Animal registered, sending notification")
      a_name = ""
      a_species = ""
      a_email = ""
      first = True
      in_name = False
      in_species = False
      in_email = False
      
      for char in text:
        if char == '|':
          if first:
            first = False
            in_name = True
          elif in_name:
            in_name = False
            in_species = True
          elif in_species:
            in_species = False
            in_email = True
          elif in_email:
            in_email = False
          else:
            pass
        else:
          if in_name:
            a_name = a_name + char
          elif in_species:
            a_species = a_species + char
          elif in_email:
            a_email = a_email + char
      
      subjet = a_name + " just ate!"
      body = "Hello!\n" + a_name + " just ate at your food dish.\nHere is the information on file about your animal:\n\tName - "+ a_name + "\n\tSpecies - " + a_species
      send_email(a_email, subject, body)

    sleep(5)

except KeyboardInterrupt:
  print("stopping")
  GPIO.cleanup()
  raise
