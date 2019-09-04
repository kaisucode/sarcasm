
import sys
import pyperclip
import random

if len(sys.argv) == 1: 
    print("No message inputed")
    quit()

message = sys.argv[1]
sarcasmed = ""
cnt = 0
for letter in message: 
    sarcasmed += letter.upper() if random.randint(1,3) == 1 else letter.lower()
    #  sarcasmed += letter.upper() if cnt%2 else letter.lower()
    cnt += 1
pyperclip.copy(sarcasmed)

# Apply bold, underline, and red color effects
print(message + " -> " + '\033[4m\033[91m\033[1m' + sarcasmed + '\033[0m')

