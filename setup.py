SPOTIPY_CLIENT_ID = input('Enter you Client Id: ')
SPOTIPY_CLIENT_SECRET = input('Enter you Client Secret: ')

with open('credentials.json', 'w') as f:
    f.write("{\n")
    f.write(f"\t\"SPOTIPY_CLIENT_ID\": \"{SPOTIPY_CLIENT_ID}\",\n")
    f.write(f"\t\"SPOTIPY_CLIENT_SECRET\": \"{SPOTIPY_CLIENT_SECRET}\"\n")
    f.write("}\n")
