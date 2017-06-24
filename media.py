# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_synopsis, movie_storyline, movie_poster_image, movie_trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.synopsis = movie_synopsis
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    def show_poster(self):
        # Opening image in web browser
        webbrowser.open_new_tab(self.poster_image_url)
        # Opening image from system
        # os.system("menaceIIsociety.jpg")

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer_youtube_url)
