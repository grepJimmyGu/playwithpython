import webbrowser

class Video():
    """All the favorite video information"""
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline

class Movie(Video):

    """The movie class represents the list of Jinze's favorite movies"""
    VALID_RATINGS = ["PG","PG-13","R","C"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        Video.__init__(self, movie_title, movie_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def poster(self):
        webbrowser.open(self.poster_image_url)
        

class TvShow(Movie):
    """All Jinze's favorite TV shows"""
    def __init__(self, TV_title, TV_storyline, TV_poster_image, TV_trailer_youtube,
                 TV_season, TV_episode, TV_listing):
        Movie.__init__(self, TV_title, TV_storyline, TV_poster_image,
                       TV_trailer_youtube)
        self.season = TV_season
        self.episode = TV_episode
        self.listing = TV_listing

    def get_local_listings(self):
        webbrowser.open(self.listing)
    def get_seasons(self):
        webbrowser.open(self.season)
    def get_episodes(self):
        webbrowser.open(self.episode)

    
        
