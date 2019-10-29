import os
import subprocess
import tinydb
from tinydb import TinyDB, Query
import csv
import sys
import imp
#ADD TO EVERY HELPER FILE:
#os.path.dirname(os.path.abspath(__file__))
#marcy = importlib.machinery.SourceFileLoader("marcy", os.path.dirname(os.path.abspath(__file__))).load_module()
marcy = imp.load_source("marcy", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "marcy.py"))
storage = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "storage/")
#END STUFF TO ADD TO EVERY HELPER FILE.

#http://stackoverflow.com/questions/34568774/reading-a-csv-file-using-python-3
#http://stackoverflow.com/questions/30218802/get-parent-of-current-directory-from-python-script

with open(os.path.join(storage, "Watch Again.csv")) as watchagain:
    for row in csv.DictReader(watchagain):
        if marcy.taskdb.search(Query()["taskName"] == ("Watch " + row["Title"])) == []:
            marcy.makeTask(taskName = ("Watch " + row["Title"]), taskDesc = row["URL"], goals = "selfcare", taskTypes = ["watch"], timeEst = (int(row["Runtime (mins)"])), pEffective = 0.7, taskKind = "fun")
