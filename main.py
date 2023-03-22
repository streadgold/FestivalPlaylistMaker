import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

keys = json.load(open('./credentials.json'))

os.environ['SPOTIPY_CLIENT_ID'] = keys['SPOTIPY_CLIENT_ID']
os.environ['SPOTIPY_CLIENT_SECRET'] = keys['SPOTIPY_CLIENT_SECRET']
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback/'

# Set up Spotify API credentials
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def generate_playlist():
    # Get list of files in directory
    files = os.listdir()

    # Find the first .txt file in the directory
    for file in files:
        if file.endswith(".txt"):
            file_path = file
            break
    else:
        print("No .txt files found in directory!")
        return

    # Open file and read in list of artists
    with open(file_path, "r") as f:
        artists = f.readlines()

    # Remove any whitespace and empty lines from list of artists
    artists = [artist.strip() for artist in artists if artist.strip()]

    # Create empty list to store track IDs
    track_ids = []

    # Choose the number of songs to add to the playlist from the artist's top tracks (max 10)
    num_songs = 5

    # Loop through each artist and get their top 5 tracks
    for artist in artists:
        results = sp.search(q=artist, type="artist")
        if results["artists"]["items"]:
            artist_id = results["artists"]["items"][0]["id"]
            top_tracks = sp.artist_top_tracks(artist_id)
            if top_tracks["tracks"]:
                for i in range(min(num_songs, len(top_tracks["tracks"]))):
                    try:
                        track_ids.append(top_tracks["tracks"][i]["id"])
                        print('adding ', top_tracks["tracks"][i]["id"], ' for artist ', artist)
                    except Exception as e:
                        print('Adding song failed: ')
                        print(e)

    # Create a new playlist and add the top 5 tracks from each artist
    playlist_name = os.path.splitext(os.path.basename(file_path))[0]
    playlist = sp.user_playlist_create(user=sp.me()["id"], name=playlist_name)

    # Add tracks to playlist in batches of 100 (to help with large number of artists)
    for i in range(0, len(track_ids), 100):
        sp.playlist_add_items(playlist["id"], track_ids[i:i + 100])

    print(f"Playlist '{playlist_name}' created successfully with {len(track_ids)} tracks!")


generate_playlist()
