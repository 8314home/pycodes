class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist: (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]):  A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year

        if artist is None:
            self.artist = Artist("Various artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=0):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def checkpoint_file(artist_list):
    with open("check_point_file.txt", "w") as check_point_file:
        for artist_field in artist_list:
            for album_field in artist_field.albums:
                for song_field in album_field.tracks:
                    print("{} {} {} {}".format(artist_field.name, album_field.name, album_field.year,
                                               song_field.title), file=check_point_file)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
#            print("{} {} {} {}".format(artist_field, album_field, year_field, song_field))

# handling artist section:

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # just read a new artist name, now we need to find if it already in list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None  # reset of new_album value for newly encountered artist


# handling Album  section: Artist member already selected

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)    # 1st album for an artist being added
            elif new_album.name != album_field:    # different album detected for an artist
                # look to find if album is already present in album list for artist
                new_album = find_object(album_field, new_artist.albums)

                if new_album is None: # a new album detected for the artist
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


if __name__ == '__main__':
    print("Starting with Program")

    artists = load_data()
    print("Artist no of artists: {}".format(artists.__len__()))
    checkpoint_file(artists)
    print("Program completed")
