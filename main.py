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
from subprocess import call
import os
import signal
import time

# define our clear function
def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

# Basic setups
print("Hello, Welcome to Box music")
i1 = ['1037840555095', '970464173093', '208999095765', '1035581529224', '424295998089', '1035097742415', '1037664001260', '1037502192785', '1035352284204']
continue_reading = True

# spotify Information
# You have to import all of this it's different for everyone
username = 'username of yours in the spotify settings'
clientID = 'YOU NEED DEVELOPER ACCESS'
clientSecret = 'YOU NEED DEVELOPER ACCESS'
redirectURI = 'https://www.google.com/'

# The spotify Initialization
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI,scope='user-modify-playback-state user-read-playback-state')
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
j = spotifyObject.devices()
user = spotifyObject.current_user()


# You can change this songs by copying the link of song from spotify
lists = ['https://open.spotify.com/track/04CRi4s1n7IAlE916TXcTC', 'https://open.spotify.com/track/1nFtiJxYdhtFfFtfXBv06s', 'https://open.spotify.com/track/7wEkkOzBlNHAJOfeQlkQUd', 'https://open.spotify.com/track/1GJ8GTkPlM5ifnyzu8cbVh', 'https://open.spotify.com/track/58ge6dfP91o9oXMzq3XkIS', 'https://open.spotify.com/track/1A45JvhIT39Ay2qriGXSUb', 'https://open.spotify.com/track/5GXeNbxOEbd7sKrbsVLVVx', 'https://open.spotify.com/track/2XGt7VK5ObGjCXIshdtnql', 'https://open.spotify.com/track/5UMMPHPp6vRP6ghPpSUOzp']

# The end
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.\n")
    continue_reading = False
    exit()
    
# initializing the Reader
signal.signal(signal.SIGINT, end_read)
MIFAREReader = SimpleMFRC522()


clear()
print("""
 ____    ___   __ __      ___ ___  __ __  _____ ____   __ 
|    \  /   \ |  |  |    |   |   ||  |  |/ ___/|    | /  ]
|  o  )|     ||  |  |    | _   _ ||  |  (   \_  |  | /  / 
|     ||  O  ||_   _|    |  \_/  ||  |  |\__  | |  |/  /  
|  O  ||     ||     |    |   |   ||  :  |/  \ | |  /   \_ 
|     ||     ||  |  |    |   |   ||     |\    | |  \     |
|_____| \___/ |__|__|    |___|___| \__,_| \___||____\____|
                                                          
\n\n""")

# Starting the loop
print("\n\nMAKE SURE YOU HAVE ACTIVE DEVICE OTHER WISE YOU WILL GET KICKED OUT OF THE APP\n\n")
while continue_reading:
    id, text = MIFAREReader.read()
    for k in range(len(i1)):
        if str(id) == str(i1[k]):
            print("Found the song\n")
            play = spotifyObject.start_playback(device_id=None,uris=[lists[k]])
            time.sleep(1)
        else:
            print("This is not a valid card, Please change it!!\n\n")
    clear()
    print("""
    ____    ___   __ __      ___ ___  __ __  _____ ____   __ 
    |    \  /   \ |  |  |    |   |   ||  |  |/ ___/|    | /  ]
    |  o  )|     ||  |  |    | _   _ ||  |  (   \_  |  | /  / 
    |     ||  O  ||_   _|    |  \_/  ||  |  |\__  | |  |/  /  
    |  O  ||     ||     |    |   |   ||  :  |/  \ | |  /   \_ 
    |     ||     ||  |  |    |   |   ||     |\    | |  \     |
    |_____| \___/ |__|__|    |___|___| \__,_| \___||____\____|
                                                            
    \n\n""")
    print("\n\nMAKE SURE YOU HAVE ACTIVE DEVICE OTHER WISE YOU WILL GET KICKED OUT OF THE APP\n\n")
