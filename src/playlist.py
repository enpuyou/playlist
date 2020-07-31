import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests

import pprint

pp = pprint.PrettyPrinter(indent=4)

emac_uri = "spotify:user:us8fmc9gg9bpnt2o2bn5p74p8"
emac_id = "us8fmc9gg9bpnt2o2bn5p74p8"
# playlist_uri = "spotify:playlist:1Ne1izrcK7dCI1oKuq9nt1"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# sp = spotipy.Spotify()
# artist = sp.artist(emac_uri)


# get playlist
def get_playlist_by_id(playlist_uri):
    playlist = sp.playlist(playlist_uri)
    return playlist
    # print(playlist)


# get tracks in the playlist
def get_tracks(playlist_uri):
    track_lst = []
    tracks = sp.playlist_tracks(playlist_uri)

    for index, track in enumerate(tracks["items"]):
        artist_lst = []
        # pp.pprint(track)
        album = track['track']['album']['name']
        print(f"album: {album}")
        for artist in track['track']['artists']:
            artist_name = artist['name']
            artist_lst.append(artist_name)
            print(f"artist: {artist_name}")
        track_name = track['track']['name']
        print(f"track name: {track_name}")
        cover_art_url = track['track']['album']['images'][0]['url']
        print(f"cover art: {cover_art_url}")
        save_image_from_url(track_name, cover_art_url)
        sep = ", "
        track_lst.append(f"{index + 1}. {track_name} - {sep.join(artist_lst)}")

    # pp.pprint(tracks)
    return track_lst


def get_user_playlists():
    p_lst = []
    playlists = sp.user_playlists(emac_id)
    for pl in playlists["items"]:
        p_lst.append({pl["name"]: pl["uri"]})
        # p_lst[pl["name"]] = pl["uri"]
    return p_lst


def save_image_from_url(filename, image_url):
    f = open(f'image/{filename}.jpg', 'wb')
    f.write(requests.get(image_url).content)
    f.close()


if __name__ == "__main__":
    playlists = get_user_playlists()
    playlist_uri = "".join(playlists[0].values())
    tracks = get_tracks(playlist_uri)
    print(tracks)
