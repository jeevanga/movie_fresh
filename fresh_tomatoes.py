import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes! - Hostile Takeover!! </title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
    <!-- Assigning trailer video and written content display box dimensions: 1200px X 400px -->
    <!-- Trailer video display dimensions: 800px X 400px -->
    <!-- Written content display dimensions: 400px X 400px -->
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 100px;
            width: 1200px;
            height: 400px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            float: left;
            width: 66.66%;
            height: 100%;
        }
        .trailer-container{
            float: left;
            width: 66.66%;
            height: 100%
        }
        .writeup{
            float: right;
            width: 400px;
            height: 400px;
            background-color: black;
            color: white;
        }
        .movie-tile {
            margin-top: 40px;
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            width: 1200px;
            height: 400px;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 66.66%;
            left: 0;
            top: 0;
            background-color : black;
        }
        .primary-background{
          background-image: url("bg.jpg");
          background-repeat: no-repeat;
          background-size: cover;
        }
        #title-bar{
          padding-top: 10px;
          padding-bottom: 10px;
          height: 48px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $("#title-bar h5").empty();
            $("#storyline-bar p").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

            // Assigning required movie title name to javascript variable (movieTitle) followed by appending it to
            // DIV ID title-bar
            var movieTitle = $(this).attr('data-movie-title-id');
            $("#title-bar h3").empty().append(movieTitle);

            // Assigning required movie storyline to javascript variable (movieStoryline) followed by appending it to
            // DIV ID storyline-bar
            var movieStoryline = $(this).attr('data-movie-storyline');
            $("#storyline-bar p").empty().append(movieStoryline);

            // Assigning required movie director name to javascript variable (movieDirector) followed by appending it to
            // DIV ID director-bar
            var movieDirector = $(this).attr('data-director-info');
            $("#director-bar span").empty().append(movieDirector);

            // Assigning required movie actor names to javascript variable (movieActors) followed by appending it to
            // DIV ID actor-bar
            var movieActors = $(this).attr('data-actor-info');
            $("#actor-bar span").empty().append(movieActors);

            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<body class="primary-background">
<!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true"><img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/></a>
                    <div class="scale-media">
                        <div class="trailer-container" id="trailer-video-container"> </div>
                        <!-- Movie writeup content box containing movie title, storyline, director and actor names -->
                        <div class="writeup" >
                            <!-- Title target for jquery -->
                            <div id="title-bar">
                                <b><h3> </h3></b>
                            </div>
                            <!-- Storyline target for jquery -->
                            <div id="storyline-bar">
                                <br><p> </p>
                            </div>
                            <!-- Director name target for jquery -->
                            <div id="director-bar">
                                <br><b> Director: </b> <span> </span>
                            </div>
                            <!-- Actor names target for jquery -->
                            <div id="actor-bar">
                                <br><b> Starring: </b> <span> </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
<!-- Main Page Content -->
<div class="container">
  <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="container">
      <div class="navbar-header">
        <a class="navbar-brand" href="#">The 9 G.O.A.T. Hood Movies Ever Made. Period. </a>
      </div>
    </div>
  </div>
</div>
<div class="container">
  {movie_tiles}
</div>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<!-- Movie tile template contains data-* attribute for all movie related content -->
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" data-movie-title-id="{movie_title}" data-movie-storyline="{movie_storyline}" data-director-info="{director_name}" data-actor-info="{actor_names}">
    <a title = "{movie_synopsis}"><img src="{poster_image_url}" width="220" height="360"></a>
    <h4></h4>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_synopsis=movie.synopsis,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            director_name=movie.director_name,
            actor_names=movie.actor_names
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes_ii.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
