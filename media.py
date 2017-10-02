import webbrowser


class Movie():
    """ The Movie() class sets up the data input (ie title, image, etc)
    for each instance(aka movie) listed"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The show_trailer() function provides a pop-up trailer once the
        movie is clicked on from the website."""
        webbrowser.open(self.trailer_youtube_url)
