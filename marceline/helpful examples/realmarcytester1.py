#import shit
import marcy
import os
import tinydb
from tinydb import TinyDB, Query
from datetime import date, timedelta
import calendar
import random

marcy.runAllHelpers()

#make first task. should have same apv.
marcy.makeTask(taskKind = "fun", taskName = "smoke weed", taskDesc = "you", timeEst = 15, taskTypes = ["do", "train"], goals = ["selfcare", "biz"], moneyNet = 1.50, pEffective = 0.8)
#make second task. should have same apv.
marcy.makeTask(taskKind = "work", taskName = "smoke dick", taskDesc = "the guy she tells you not to worry about", timeEst = 10, taskTypes = ["play", "listen"], goals = ["selfcare", "comms"], canInterrupt = True,  pEffective = 0.8)

marcy.bigRecalc()

print("The cabal has chosen task number " + str(marcy.getNeededTask(20, "either").eid))
