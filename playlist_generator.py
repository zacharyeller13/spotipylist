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

library_artists = [*music_library.iterdir()]

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

# Open new playlist file and begin searching and writing matches to file
playlist_name = input("Name for New Playlist: ")

with open(f"{music_library}/{playlist_name}.m3u", 'a') as f:
    f.write("#EXTM3U\n")

    # for each track, grab the top 3 artist matches
    # we will probably change to some sort of ratio threshold instead, but top 3 works for now
    # for tracks with featured artists, we use partial_ratio for a better match
    for track in track_info['items']:
        mp3_list = []
        track_artist = track['track']['artists'][0]['name'] # take the first/primary artist
        if len(track['track']['artists']) > 1: # checking if there are featured artists
            # setting cuttoff of 70, seems to work for the most part right now
            artist_matches = [dir for dir in library_artists if fuzz.partial_ratio(track_artist, dir.name) > 70]

        else:
            # index library_artists with index provided by the tuple returned from process.extract
            artist_matches = [library_artists[result[2]] for result in process.extract(track_artist, [dir.name for dir in library_artists])]

        # search each matched artist folder for mp3 files, recursively
        # append all found mp3 files to a list mp3_list
        for artist_dir in artist_matches:
            for mp3_file in artist_dir.rglob("*.mp3"):
                mp3_list.append(mp3_file)
        
        # Check each file in mp3_list against song from playlist
        best_match = process.extractOne(track['track']['name'], [mp3.stem for mp3 in mp3_list])
        
        # write best_match relative path to the playlist file, taking the index of the best match
        # in the mp3_list to get the full PosixPath object, allowing use of the .relative_path() method
        mp3 = mp3_list[best_match[2]].relative_to(music_library)
        f.write(f"{str(mp3)}\n")
