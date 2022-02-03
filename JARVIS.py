from playsound import playsound
from art import *
import time
import sys

tprint("JARVIS")
playsound('JARVIS.mp3')
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)

if __name__ == "__main__":
  slowprint("If you have any tasks to do for me please put that in the code.")

playsound('ACDC.mp3')
