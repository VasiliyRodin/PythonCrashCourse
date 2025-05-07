'''
Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.
'''


def make_album(artist_name, album_name):
    artist_album_dictinary = {"artist_name":artist_name.title(), "album_name":album_name.title()} # Remember that 
    return artist_album_dictinary
albums =[]
albums.append(make_album("bob dylan", "desire"))
albums.append(make_album('test2 name',"test2 album"))
albums.append(make_album('test3 name', 'abum name3'))
print(albums)

'''“Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
 If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. 
 Make at least one new function call that includes the number of tracks on an album.”
'''

#creates a list of dictionaries. 
def make_album2(artist_name, album_name, tracks=''):
    if tracks: #no need for true. 
        artist_album_dictinary = {"artist_name":artist_name.title(), "album_name":album_name.title(), "tracks": tracks} # Remember that dictionary uses : not = 
    else:
        artist_album_dictinary = {"artist_name":artist_name.title(), "album_name":album_name.title()}
    return artist_album_dictinary
albums =[]
albums.append(make_album2("bob dylan", "desire"))
albums.append(make_album2('test2 name',"test2 album"))
albums.append(make_album2('test3 name', 'abum name3', 4))
print(albums)

