import os
import tinydb
from tinydb import TinyDB, Query

moviestorage = "storage/moviedb.json"

moviedb = TinyDB(moviestorage)

#moviedb.insert({'filmName': 'Guardians of the Galaxy Vol. 2', 'imdbID': "tt3896198", 'filmLength' : 136})
#moviedb.insert({'filmName': 'Pi', 'imdbID': "tt0138704", 'filmLength' : 84})
#moviedb.insert({'filmName': 'Shrek the Third', 'imdbID': "tt0413267", 'filmLength' : 93})
moviedb.insert({'filmName': 'Bee Movie', 'imdbID': "tt0389790", 'filmLength' : 91})
