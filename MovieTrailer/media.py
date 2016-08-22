import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_Youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_Youtube_url = trailer_Youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_Youtube_url)
