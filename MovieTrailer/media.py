import webbrowser

class Movie():
    """ This class provides a way to store movie related information. """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """ This function initializes space in memory to remember arguments for the Movie class. """

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    """ This instance method opens the web browser with the correct URL."""
