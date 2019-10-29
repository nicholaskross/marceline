#import essential things
import os
import tinydb
from tinydb import TinyDB, Query
import random
import marcy
#import moviedbfiller

moviestorage = "storage/moviedb.json"

moviedb = TinyDB(moviestorage)

for theEID in range(1, len(moviedb)+1):
    if moviedb.contains(eids = [theEID]):
        m = dict(moviedb.get(eid=theEID))
        if marcy.taskdb.search(Query()["taskName"] == ("Watch " + m["filmName"])) == []:
            marcy.makeTask(taskName = ("Watch " + m["filmName"]), taskDesc = "http://www.imdb.com/title/" + m["imdbID"] + "/", goals = "selfcare", taskTypes = ["watch"], timeEst = m["filmLength"], pEffective = 0.7, taskKind = "fun")

marcy.bigRecalc()

print(str(marcy.taskdb.all()))

marcy.getNeededTask(180, "fun")
