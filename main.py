print("""
 ____    ___   __ __      ___ ___  __ __  _____ ____   __ 
|    \  /   \ |  |  |    |   |   ||  |  |/ ___/|    | /  ]
|  o  )|     ||  |  |    | _   _ ||  |  (   \_  |  | /  / 
|     ||  O  ||_   _|    |  \_/  ||  |  |\__  | |  |/  /  
|  O  ||     ||     |    |   |   ||  :  |/  \ | |  /   \_ 
|     ||     ||  |  |    |   |   ||     |\    | |  \     |
|_____| \___/ |__|__|    |___|___| \__,_| \___||____\____|
                                                          
\n\n""")

# Importing modules
import spotipy
from mfrc522 import SimpleMFRC522
import signal
import time

# Basic setups
print("Hello, Welcome to Box music")
print("Use the test.py to find your card id or if you have it just enter it below!\nmax of cards is 2")
print("If you don't have two cards just press ENTER\n")
i1 = input("ID 1: ")
i2 = input("ID 2: ")
print("Press Ctrl-C to stop.\n\n")
continue_reading = True

# spotify Information
# You have to import all of this it's different for everyone
username = 'username of yours in the spotify settings'
clientID = 'YOU NEED DEVELOPER ACCESS'
clientSecret = 'YOU NEED DEVELOPER ACCESS'
# This is the redirect url, you can change this or just use this, however you need to enter this to your account.
redirectURI = 'https://www.google.com/'

# The spotify Initialization
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI,scope='user-modify-playback-state user-read-playback-state')
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
j = spotifyObject.devices()
user = spotifyObject.current_user()


# You can change this songs by copying the link of song from spotify
lists = ['https://open.spotify.com/track/58ge6dfP91o9oXMzq3XkIS', 'https://open.spotify.com/track/3gkiUzAUBH035zRHy7KyJg']

# The end
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.\n")
    continue_reading = False
    exit()
    
# initializing the Reader
signal.signal(signal.SIGINT, end_read)
MIFAREReader = SimpleMFRC522()

# Starting the loop
print("\n\nMAKE SURE YOU HAVE ACTIVE DEVICE OTHER WISE YOU WILL GET KICKED OUT OF THE APP\n\n")
while continue_reading:
    id, text = MIFAREReader.read()
    if str(id) == str(i1):
        print("Found the song\n")
        play = spotifyObject.start_playback(device_id=None,uris=[lists[0]])
        time.sleep(1)
    if str(id) == str(i2):
        print("Found the song\n")
        play = spotifyObject.start_playback(device_id=None,uris=[lists[1]])
        time.sleep(1)
    else:
        print("This is not your card, Please use a valid card!\n\n")