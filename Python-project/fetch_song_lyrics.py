#pip install lyricsgenius

api_key = "xxxxxxxxxxxxxxxxxx"

genius = lyricsgenius.Genius(api_key)
artist = genius.search_artist("Pop smoke",max_songs = 5,sort="title")
song = artist.song("100k on couple")


print(song.lyrics)