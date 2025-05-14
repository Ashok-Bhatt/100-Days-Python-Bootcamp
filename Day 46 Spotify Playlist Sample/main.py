
from bs4 import BeautifulSoup
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

input_date = input("Enter the date in YYYY-MM-DD format:")
URL = f"https://www.billboard.com/charts/hot-100/{input_date}/"

sp = Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="Enter Your Own Client Id",
        client_secret="Enter Your Own Client Secret",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

request = requests.get(URL)
response = request.text

soup = BeautifulSoup(response, "html.parser")

song_tag_list = soup.select(name="h3", selector="#title-of-a-story.a-no-trucate")
song_name_list = [song.getText().strip() for song in song_tag_list]

song_uris = []
year = input_date.split("-")[0]

#FIXME: Remove the printing lines form the loop after that index for song won't be required
for no,song in enumerate(song_name_list):
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    if no==0:
        print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)