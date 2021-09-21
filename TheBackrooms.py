from time import sleep
import sys
import time
import os
import winsound

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
I passed the empty waiting area a small area of the main room with magazines, children’s playthings and blue cushioned chairs— and approached the woman at the front desk.
She was sitting in her blueish gray office chair, looking at a spreadsheet on the same Windows XP desktop they’ve had since 2008.
There was a sign-in sheet on the counter in front of me.

“I have an appointment with Dr. Pebins?” I asked.
“What time?”
“12:30,” I replied.
She began typing something into her keyboard.
“Ah, yes,” she responded. “Gary Johnston?”
“Mhm.”
“Yes, I’ll tell the doctor. Please fill this out.”

She handed me a clipboard which held a simple fill-out form. I walked back to the waiting area, took a seat, and began to fill out the form.
I was about halfway done with filling in my information, when I slumped back. I noticed something very peculiar my head never hit the wall. In fact, it felt like it went IN.
I got up, quite frightened, and looked at the wall. Nothing. Not a single hole, or dent, had been made in the wall by my head. So, I reached to touch the wall.
And my fingers went through it. I recoiled in shock.
“What the hell was that?” I thought, as I reached to touch the wall again, only to find my fingers clipped through once more.
Then, suddenly, I lost my balance, tripped, and fell directly through the wall. I fell face-first onto some dirty tan carpeting.
Upon getting back up, I realized that I was in a completely different room. Well, not really a room, per se more so a set of rooms, all of which connected by openings.
The walls were covered in gross tan patterned wallpaper. There was also an overwhelming stench of moist carpet."""

for letter in string:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

time.sleep(5)
os.system("cls")

winsound.PlaySound("hey.wav", winsound.SND_ASYNC + winsound.SND_LOOP | winsound.SND_ALIAS )

start = input("""What are you going to do?
A(Search the room for clues
B(Try to go through the wall
C(Do nothing: """).lower()

if start == 'a':
  print("You found nothing.")
elif start == 'b':
  print("Your hand wont go through the wall. You realize your stuck in this room")
elif start == 'c':
  print("You did nothing.")