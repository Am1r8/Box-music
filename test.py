from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print("With this script you can find your card and read the ID\n\n")
f = True

while f:
    try:
        print("Now place your tag to read\n")
        id, text = reader.read()
        print("\nHere is your ID: " + str(id) + "\n")
        print("Use the script.py to connect your card\n")
    except:
        print("No card detected\n\n")
        f = False
        break