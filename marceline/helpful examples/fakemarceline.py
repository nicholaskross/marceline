import os
import tinydb
from tinydb import TinyDB, Query
from datetime import date, timedelta
import calendar
import random
import fakemarcy

fakemarcy.makeTask(taskKind = "work", taskName = "kill urself", taskDesc = "use bleach", timeEst = 45, pEffective = 0.99, goal = "selfcare", moneyNet = -(700 + fakemarcy.dependency["usableMoney"]))

fakemarcy.makeTask(taskKind = "fun", taskName = "help urself", taskDesc = "dont die plz", timeEst = 120, pEffective = 0.5, taskTypes = ["do", "play"], goal = "selfcare", canInterrupt = True) 

fakemarcy.bigRecalc()

#fakemarcy.changeSomething()
