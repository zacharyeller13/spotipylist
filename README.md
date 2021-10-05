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

TODO #5

## Usage

1. Set the following environment variables:

    - SPOTIPY_CLIENT_ID
    - SPOTIPY_CLIENT_SECRET
    - SPOTIPYLIST_MUSIC_LIBRARY

    To set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET, first create a new app on <https://developers.spotify.com>, then use the client_id and client_secret given there.

    Set SPOTIPYLIST_MUSIC_LIBRARY with the absolute path to your local music library.

2. Run spotipylist in your terminal with `python spotipylist.py`

## License

Spotipylist is licensed under the MIT license.

This is one reason for using the rapidfuzz library over fuzzywuzzy as fuzzywuzzy is licensed under GPL-2.0, which would require Spotipylist to adopt GPL-2.0 as well.
