
# Adds tracks to a playlist

import pprint
import sys

import spotipy
import spotipy.util as util

tracks = []
lineupfile = open('lineup.txt','r')
lineup = [x.strip('\n') for x in lineupfile.readlines()]

numberofbands = len(lineup)
if(number)

if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
else:
    print("Usage: %s username playlist_id ..." % (sys.argv[0],))
    sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, redirect_uri = 'https://example.com/callback/')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    for x in range(0,len(lineup)):
        results = sp.search(q=str(lineup[x]), limit=5)
        for i, t in enumerate(results['tracks']['items']):
            tracks.append(str(t['id'].strip( 'u' )))
            print("adding ",t['id'],t['name'])
    results = sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)

else:
    print("Can't get token for", username)


print "Playlist Complete!"
