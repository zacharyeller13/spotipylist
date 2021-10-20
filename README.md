# Spotipylist

A playlist generator for creating local playlists using Spotify's curated playlists

**Currently under active development.**

## Table of Contents

- [General Info](#General-Info)
- [Technologies](#Technologies)
- [Setup](#Setup)
- [Usage](#Usage)
- [License](#License)

## General Info

This project is my final project for CS50x (Harvard University's Intro to Computer Science hosted on edX.org)

The main purpose is to make creating playlists from my personal music library faster, easier, and better by using the track lists of many of the fantastic playlists that are already hosted on Spotify.

Video Demo: TODO #7

## Technologies

Spotipylist uses the following:

- Python 3.6 or later
- spotipy 2.19.0
- rapidfuzz 1.7.1

## Setup

Spotipylist is easily installable using `pip`:

```
pip install spotipylist
```

OR

```
python3 -m pip install spotipylist
```

## Usage

1. Set the following environment variables:

    - SPOTIPY_CLIENT_ID
    - SPOTIPY_CLIENT_SECRET
    - SPOTIPYLIST_MUSIC_LIBRARY

    To set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET, first create a new app on <https://developers.spotify.com>, then use the client_id and client_secret given there.

    Set SPOTIPYLIST_MUSIC_LIBRARY with the absolute path to your local music library.

2. Because you installed from PyPi, you can run spotipylist in your terminal with

```
spotipylist
```

3. You will be prompted for the Spotify playlist ID you want to copy.
    - The playlist ID is the last portion of a Spotify Playlist URL:
        [https://open.spotify.com/playlist/**5t9TUKubTd0bOriqsxq79h**](https://open.spotify.com/playlist/5t9TUKubTd0bOriqsxq79h)

4. When prompted, input the name you would like to give to your new playlist.
    - New playlist will be saved in your music library as `<playlist_name>.m3u`, overwriting any playlist of the same name.

5. Finally, if your music library does not contain some of the songs in the Spotify playlist, the name and artist of each of those tracks will be saved to `missing_tracks.txt` in your music library.  You'll be prompted with the following message:
    - `Some songs from this playlist were not found in your library. See missing_tracks.txt for details.`

## License

Spotipylist is licensed under the MIT license.

This is one reason for using the rapidfuzz library over fuzzywuzzy as fuzzywuzzy is licensed under GPL-2.0, which would require Spotipylist to adopt GPL-2.0 as well.
