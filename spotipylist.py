from requests import auth
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# TODO #8 import playlist_generator
# and use defined helper functions

# take input of playlist URL or playlist_id from user
playlist_url = input("""
    Please input the desired playlist ID.\n
    The id will be the string of characters at the end of the URL as below\n
    https://open.spotify.com/playlist/5t9TUKubTd0bOriqsxq79h -> 5t9TUKubTd0bOriqsxq79h\n
    Playlist ID: """)

# TODO #12 Get Spotify client credentials from user to authenticate
# SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET need to be set via environment variables

auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)

# TODO #13 Get playlist_items and necessary fields (name, artists)