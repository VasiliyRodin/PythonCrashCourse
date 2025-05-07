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

#creates a list of dictionaries. 