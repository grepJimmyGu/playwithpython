import webbrowser

class Movie():

    """The movie class represents the list of Jinze's favorite movies"""


    VALID_RATINGS = ["PG","PG-13","R","C"]

    
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def poster(self):
        webbrowser.open(self.poster_image_url)
        
