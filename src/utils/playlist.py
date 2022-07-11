# define classes for Playlist and Track/Song

class Song:

    def __init__(self, name: str, artists: list[str]) -> None:
        self.name = name
        self.artists = artists

class Playlist:

    def __init__(self, name: str, tracks: list[Song]) -> None:
        self.name = name
        self.tracks = tracks
