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
        # Initialize instance of class Movie
        self.title = movie_title
        self.synopsis = movie_synopsis
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

class Personnel(Movie):
    # The 'Personnel' class is defined as a child of the Parent 'Movie' class

    def __init__(self, movie_title, movie_synopsis, movie_storyline, movie_poster_image, movie_trailer_youtube, director_name, actor_names):
        # Initialize instance of child class 'Personnel'
        Movie.__init__(self, movie_title, movie_synopsis, movie_storyline, movie_poster_image, movie_trailer_youtube)
        self.director_name = director_name
        self.actor_names = actor_names
