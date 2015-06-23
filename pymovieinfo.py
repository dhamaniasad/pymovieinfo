__version__ = 0.1
import urllib
import json
import argparse



def command_line_runner():
    parser = argparse.ArgumentParser(description='Get information about any movie from the command line')
    parser.add_argument('movie', type=str, help="Name of the movie you want information about")
    args = parser.parse_args()
    movie = args.movie
    movie_data = get_info(movie)
    if movie_data is False:
        print "Sorry, could not find a movie with that name :'("
    else:
        print "Movie: {}".format(movie_data['title'])
        print "Plot: {}".format(movie_data['plot'])
        print "Genre: {}".format(movie_data['genre'])
        print "Released: {}".format(movie_data['released'])
        print "Runtime: {}".format(movie_data['runtime'])
        print "IMDb rating: {}".format(movie_data['rating'])


def get_info(movie):
    url = "http://www.omdbapi.com/?t={}&type=movie".format(movie)
    r = urllib.urlopen(url)
    data = json.loads(r.read())
    if data['Response'] == "True":
        movie_runtime = int(data['Runtime'].split()[0])
        rating = "{} stars from {} votes".format(data['imdbRating'], data['imdbVotes'])
        movie_runtime = "{} hours {} minutes".format(movie_runtime / 60, movie_runtime % 60)
        movie_info = {'title': data['Title'], 'genre': data['Genre'],
                      'released': data['Year'], 'runtime': movie_runtime,
                      'plot': data['Plot'], 'rating': rating}
        return movie_info
    else:
        return False
