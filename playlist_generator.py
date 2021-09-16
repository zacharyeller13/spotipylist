import os
import pathlib

from rapidfuzz import process
import rapidfuzz.fuzz as fuzz


# Set the location of the music library for searching
# This can be an absolute reference, we will write the M3U playlist
# and save it to the music library so that it can have the relative reference


# FUTURE ENHANCEMENT? Allow user to select music folder via GUI

music_library = pathlib.Path("/media/storage/Music/All Music/")

# os.listdir will list all top-level directories in the music library
# My library is set up with Artist/Album/Track.mp3, so this will
# allow us to search based on artist and filter, before selecting
# the actual tracks

artist_dirs = [*music_library.iterdir()]

# TODO: #2 Read in list of tracks from spotipy output
# For now, we will hardcode a dict based on music I know I have
# for testing

track_info = {
    'items': [
        {
            'track': {
                'artists': [{'name': 'Phantom Planet'}],
                'name': 'California - Tchad Blake Mix'
            }
        },
        {
            'track': {
                'artists': [{'name': 'blink-182'}],
                'name': 'First Date'
            }
        },
        {
            'track': {
                'artists': [{'name': 'G-Eazy'}, {'name': 'Bebe Rexha'}],
                'name': 'Me, Myself & I'
            }
        }
    ]
}

# for each track, grab the top 3 artist matches
# we will probably change to some sort of ratio threshold instead, but top 3 works for now
# for tracks with featured artists, we use partial_ratio for a better match
for track in track_info['items']:
    mp3_list = []
    artist = track['track']['artists'][0]['name'] # take the first/primary artist
    if len(track['track']['artists']) > 1: # checking if there are featured artists
        # setting cuttoff of 70, seems to work for the most part right now
        artist_folders = [dir for dir in artist_dirs if fuzz.partial_ratio(artist, dir.name) > 70]

    else:
        # index artist_dirs with index provided by the tuple returned from process.extract
        artist_folders = [artist_dirs[result[2]] for result in process.extract(artist, [dir.name for dir in artist_dirs])]
    print(artist_folders)

    # search each matched artist folder for mp3 files, recursively
    # append all found mp3 files to a list mp3_list
    for artist_dir in artist_folders:
        for mp3_file in artist_dir.rglob("*.mp3"):
            mp3_list.append(mp3_file)
    print(mp3_list)
    
    # Check each file in mp3_list against song from playlist
    best_match = process.extractOne(track['track']['name'], [mp3.stem for mp3 in mp3_list])
    print(f"Best match:\n {track['track']['name']} | {best_match}")

    # TODO #3 Write the best_match to the playlist file
