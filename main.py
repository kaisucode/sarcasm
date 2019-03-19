
import sys

if len(sys.argv) == 1: 
    print("No message inputed")
    quit()

message = sys.argv[1][:-1]

sarcasmed = ""
cnt = 0
for letter in message: 
    if cnt%2: 
        sarcasmed += letter.upper();
    else: 
        sarcasmed += letter.lower();
    cnt += 1

print(message + " -> " + sarcasmed)

