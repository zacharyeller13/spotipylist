# Spotipylist

A playlist generator for creating local playlists using Spotify's curated playlists

## Table of Contents

- [General Info](#General-Info)
- [Dependencies](#Dependencies)
- [Setup](#Setup)
- [Usage](#Usage)
- [License](#License)

## General Info

This project is my final project for CS50x (Harvard University's Intro to Computer Science hosted on edX.org)

The main purpose is to make creating playlists from my personal music library faster, easier, and better by using the track lists of many of the fantastic playlists that are already hosted on Spotify.

Video Demo: <https://youtu.be/hiCw-1UxLPs>

## Dependencies

Spotipylist uses the following:

- Python 3.6 or later
- spotipy 2.19.0
- rapidfuzz 1.7.1

## Setup

Spotipylist is installable using `pip`:

```bash
pip install spotipylist
```

OR

```bash
python3 -m pip install spotipylist
```

Currently, your music library must be arranged the in the following format:

- Folder structure:

    ```bash
    <music_library>/<artist>/[<album>/]
    ```

- Filenames

    ```bash
    <track_number> - <track_name>.mp3
    ```

    where track_number is 2 digits (e.g. 01 for track number 1)

This is mostly a personal choice as that's how my music library is structured.  I have considered other options, such as adding support for ID3 tags, and probably will add one or more in future releases.

## Usage

1. Set the following environment variables:

    - SPOTIPY_CLIENT_ID
    - SPOTIPY_CLIENT_SECRET
    - SPOTIPYLIST_MUSIC_LIBRARY

    To set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET, first create a new app on <https://developers.spotify.com>, then use the client_id and client_secret given there.

    Set SPOTIPYLIST_MUSIC_LIBRARY with the absolute path to your local music library.

2. Because you installed from PyPi, you can run spotipylist in your terminal with

    ```bash
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
