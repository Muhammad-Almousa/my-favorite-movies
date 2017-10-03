import webbrowser


class Movie():
    """ This class provides a way to store movies related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """This docstring explains the constructer method"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            """This is a function to show the trailer of the movie"""
            webbrowser.open(self.trailer_youtube_url)
