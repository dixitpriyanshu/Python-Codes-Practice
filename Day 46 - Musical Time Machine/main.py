from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

songs_list = soup.select(selector=".o-chart-results-list__item h3")
songs = [song.getText() for song in songs_list]
all_songs = []
for song in songs:
    song = song.split()
    song = " ".join(song)
    all_songs.append(song)

pprint(all_songs)

CLIENT_ID = ""
CLIENT_SECRET = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)
song_uris = []
year = date.split("-")[0]
for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)