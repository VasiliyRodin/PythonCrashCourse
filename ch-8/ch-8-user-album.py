'''
User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.”
'''

#creates a list of dictionaries. 
def make_album2(artist_name, album_name, tracks=''):
    if tracks: 
        artist_album_dictinary = {"artist_name": artist_name.title(), "album_name": album_name.title(), "tracks": tracks}
    else:
        artist_album_dictinary = {"artist_name": artist_name.title(), "album_name": album_name.title()}
    return artist_album_dictinary



print("Please input artist name, album, and number of tracks if you know it" \
    "\nIf you do no know the amount of tracks just leave it blank.")

albums_list = []
while True:
    print("Type q to quit any time")

    artist_name = input("Artist Name: ")
    if(artist_name.lower() == 'q'):
        break

    album_name = input("Almbum Name: ")
    if(album_name.lower() == 'q'):
        break

    album_tracks = input("Almbum Tracks: ")
    if(album_tracks.lower() == 'q'):
        break

    if album_tracks:
        albums_list.append(make_album2(artist_name, album_name, album_tracks))
    else:
        albums_list.append(make_album2(artist_name,album_name))

print(albums_list)


#For dictionaries in lists you need two for loops. One for the list on for dictionary.(IF ALL THE DICIONARIES are the same otherwise i need to add a checker to see if they have tracks.)
#WHEN DOING GET USE the "KEY" You kept doing get(artist_name) WHICH IS NOT THE FREAKING KEY.
for album in albums_list:
    print("\n --------")
    print("Artist Name " + album.get("artist_name"))
    print("Album Name " + album.get("album_name"))
    if album.get("tracks"):
        print("Album tracks" + album.get("tracks"))
    else:
        print("No track count provided")
    print("--------")



    