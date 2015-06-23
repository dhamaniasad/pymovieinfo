import requests
import json

query = ""

url = "http://www.omdbapi.com/?t={}&type=movie".format(query)

r = requests.get(url)
data = json.loads(r.content)
movie_runtime = int(data['Runtime'].split()[0])
print "Movie: {}".format(data['Title'])
print "Genre: {}".format(data['Genre'])
print "Released: {}".format(data['Year'])
print "Runtime: {} hours {} minutes".format(movie_runtime / 60, movie_runtime % 60)
print "Plot: {}".format(data['Plot'])
print "IMDb rating: {} stars from {} votes".format(data['imdbRating'], data['imdbVotes'])
