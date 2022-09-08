# FestivalPlaylistMaker
## Reads in a list of artists and generates a playlist of their top 5 songs on Spotify using Python and Spotipy

1. Create a `lineup.txt` file, and place it in the `FestivalPlaylistMaker` folder

    - example `lineup.txt` file is provided
    - format as one artist per line
    - any size list should work

2. Set your spotify developer credentials 
    
    Instructions: https://developer.spotify.com/documentation/general/guides/authorization/app-settings/

3. From the spotify app panel

    - click "edit settings"

    ![](https://i.imgur.com/EWaNUdH.png)

    - add a redirect URI

    ![](https://i.imgur.com/0zP92u7.png)

    - and save

    ![](https://i.imgur.com/LdZQFz4.png)

4. Create a Spotify Playlist and copy the link url

    ![](https://i.imgur.com/CanLOQy.png)

5. Run the program like so: 

    `python main.py *username* *playlistURI*`

    Example:

    `python main.py srt252 spotify:user:srt252:playlist:3inHoNcLaV9HjNdxJwZzEi`

6. (First run only) A browser will open. After authorizing, copy the url of the page that the browser redirects to. Paste that url into the prompt

------------------------

Note - this program is not perfect but it works well enough.
