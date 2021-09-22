import pathlib
import os

from rapidfuzz import process
import rapidfuzz.fuzz as fuzz

# FUTURE ENHANCEMENT? Allow user to select music folder via GUI

def get_music_library():
    """Get the user's music library and return the library path object
    and a list of artist path objects.
    """

    # Either get the music library from an environment variable OR
    # allow user to set at runtime
    music_library = os.environ.get("SPOTIPYLIST_MUSIC_LIBRARY")
    
    # if the environment variable is not set, prompt the user
    if not music_library:
        print("Music library not set. Please set the SPOTIPYLIST_MUSIC_LIBRARY environment variable before running or input the absolute path of your music library now")
        music_library = input("Music library absolute path: ")
    
    music_library = pathlib.Path(music_library)
    
    # pathlib.iterder() will list all top-level directories in the music library
    # My library is set up with Artist/Album/Track.mp3, so this will
    # allow us to search based on artist and filter, before selecting
    # the actual tracks
    library_artists = [*music_library.iterdir()]

    return music_library, library_artists

def search_tracks(track, library_artists, music_library):
    """Read in track info and list of library artists;
    search for matching tracks and return a best match    
    """
    mp3_list=[]
    track_artist = track['track']['artists'][0]['name'] # take first/primary artist
    if len(track['track']['artists']) > 1: # if there are featured artists
        # setting cutoff of 70, seems to match pretty well for now
        artist_matches = [dir for dir in library_artists if fuzz.partial_ratio(track_artist, dir.name) > 70]

    else:
        # index library_artists with index provided by tuple returned from process.extract
        artist_matches = [library_artists[result[2]] for result in process.extract(track_artist, [dir.name for dir in library_artists])]

    for artist_dir in artist_matches:
        for mp3_file in artist_dir.rglob("*.mp3"):
            mp3_list.append(mp3_file)

    best_match = process.extractOne(track['track']['name'], [mp3.stem for mp3 in mp3_list])
    
    # Return best_match's relative path to the music_library, taking the index of the best match
    # in the mp3_list to get the full PosixPath object, allowing use of the .relative_path() method

    return mp3_list[best_match[2]].relative_to(music_library)

def write_playlist(track_dict, playlist_name, music_library):
    """Open a new playlist, write M3U header, write all best matches from search_tracks()
    """
    with open(f"{music_library}/{playlist_name}.m3u", 'w') as f:
        f.write("#EXTM3U\n")

        for track in track_dict:
            best_match = search_tracks(track, library_artists, music_library)

            f.write(f"{str(best_match)}\n")
    return

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

if __name__ == "__main__":

    music_library, library_artists = get_music_library()
    playlist_name = input("Name for New Playlist: ")

    write_playlist(track_info['items'], playlist_name, music_library)
