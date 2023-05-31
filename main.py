import spotipy
import spotipy.util as util
import random

# Set the client ID, client secret, and redirect URI
client_id = ""
client_secret = ""
redirect_uri = ""

# Set the username and scope
username = ""
scope = ""

# Get the access token
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Create the Spotify API client
sp = spotipy.Spotify(auth=token)

# Create a new playlist
playlist_name = "My Random Playlist by using python"
playlist = sp.user_playlist_create(username, playlist_name)
playlist_id = playlist["id"]

# Search for tracks on Spotify
results = sp.search(q="genre:rock", type="track", limit=50)

# Select a random set of tracks from the search results
random_tracks = random.sample(results["tracks"]["items"], 10)
track_uris = [track["uri"] for track in random_tracks]

# Add the tracks to the playlist
sp.user_playlist_add_tracks(username, playlist_id, track_uris)
