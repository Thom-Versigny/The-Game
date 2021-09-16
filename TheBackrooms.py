from time import sleep
import sys
import time
import os

print("""
████████╗██╗░░██╗███████╗
╚══██╔══╝██║░░██║██╔════╝
░░░██║░░░███████║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░
░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░░█████╗░███╗░░░███╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝
██████╦╝███████║██║░░╚═╝█████═╝░██████╔╝██║░░██║██║░░██║██╔████╔██║╚█████╗░
██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║░╚═══██╗
██████╦╝██║░░██║╚█████╔╝██║░╚██╗██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░""")
time.sleep(5)
os.system("cls")

string = """It was approximately 12:15 when I entered the Johnson County Community Health Clinic. 
I was there for an appointment I had set up weeks ago, just a routine checkup. It wasn’t a new place for me; I had been there a couple times before. 
However, the place had an odd nostalgic feel to it, as if it were a location from my childhood or something, 
and I could never pinpoint exactly what this feeling was, or where it came from.

As I walked in, an overwhelming feeling of deja vu swept over me. The hum of the flickering fluorescent lights, the white tile flooring,
the muted beige paint that colored the walls. I noticed that there was a TV mounted in the corner, a smaller flatscreen, 
that was playing a short PowerPoint slideshow on loop of ads and events that were being held by the clinic.
I passed the empty waiting area— a small area of the main room with magazines, children’s playthings and blue cushioned chairs— and approached the woman at the front desk.
She was sitting in her blueish gray office chair, looking at a spreadsheet on the same Windows XP desktop they’ve had since 2008.
There was a sign-in sheet on the counter in front of me."""

for letter in string:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()