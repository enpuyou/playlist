import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests

import pprint

emac_uri = "spotify:user:us8fmc9gg9bpnt2o2bn5p74p8"
playlist_uri = "spotify:playlist:1Ne1izrcK7dCI1oKuq9nt1"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# sp = spotipy.Spotify()
# artist = sp.artist(emac_uri)

# get playlist
playlist = sp.playlist(playlist_uri)
# print(playlist)

# get tracks in the playlist
tracks = sp.playlist_tracks(playlist_uri)
pp = pprint.PrettyPrinter(indent=4)
for track in tracks["items"]:
    # pp.pprint(track)
    print(f"album: {track['track']['album']['name']}")
    for artist in track['track']['artists']:
        print(f"artist: {artist['name']}")
    track_name = track['track']['name']
    print(f"track name: {track_name}")
    cover_art_url = track['track']['album']['images'][0]['url']
    print(f"cover art: {cover_art_url}")
    f = open(f'{track_name}.jpg','wb')
    f.write(requests.get(cover_art_url).content)
    f.close()

# pp.pprint(tracks)
