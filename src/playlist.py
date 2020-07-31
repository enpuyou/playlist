import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests

import pprint

pp = pprint.PrettyPrinter(indent=4)

emac_uri = "spotify:user:us8fmc9gg9bpnt2o2bn5p74p8"
playlist_uri = "spotify:playlist:1Ne1izrcK7dCI1oKuq9nt1"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# sp = spotipy.Spotify()
# artist = sp.artist(emac_uri)


# get playlist
def get_playlist_by_id():
    playlist = sp.playlist(playlist_uri)
    return playlist
    # print(playlist)


# get tracks in the playlist
def get_tracks():
    tracks = sp.playlist_tracks(playlist_uri)

    for track in tracks["items"]:
        # pp.pprint(track)
        print(f"album: {track['track']['album']['name']}")
        for artist in track['track']['artists']:
            print(f"artist: {artist['name']}")
        track_name = track['track']['name']
        print(f"track name: {track_name}")
        cover_art_url = track['track']['album']['images'][0]['url']
        print(f"cover art: {cover_art_url}")
        f = open(f'{track_name}.jpg', 'wb')
        f.write(requests.get(cover_art_url).content)
        f.close()

    # pp.pprint(tracks)


def get_user_playlists():
    # user = sp.user("us8fmc9gg9bpnt2o2bn5p74p8")
    p_lst = {}
    playlists = sp.user_playlists("us8fmc9gg9bpnt2o2bn5p74p8")
    for pl in playlists["items"]:
        p_lst[pl["name"]] = pl["uri"]
    return p_lst


if __name__ == "__main__":
    playlists = get_user_playlists()
    print(playlists)
