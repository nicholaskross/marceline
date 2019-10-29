#import essential things
import os
import tinydb
from tinydb import TinyDB, Query
import random
from ast import literal_eval
import marcy

#should be APV.
marcy.makeTask(taskName = "kill urself", taskKind = "work", timeEst = 60, moneyNet = -(marcy.usableMoney), goals = ["selfcare"],  pEffective = 0.8, taskTypes = ["do"])
#should be APV.
marcy.makeTask(taskName = "fuck a duck", taskKind = "fun", timeEst = 23, dependencies = ["amAdult"], pEffective = 0.4)
#should be APV.
marcy.makeTask(taskName = "go to furrycon 2016", taskKind = "fun", timeEst = 360, moneyNet = -60, goals = ["selfcare", "comms"], pEffective = 0.8, taskTypes = ["bewith", "watch"],  buildsCC = True)
#should be APV.
marcy.makeTask(taskName = "watch driftwood", taskKind = "work", timeEst = 45, goals = ["selfcare"], pEffective = 0.9, taskTypes = ["watch"])
#should be APV.
marcy.makeTask(taskName = "ultimate showdown with Chris", taskKind = "fun", timeEst = 180, dependencies = ["notOnCampus"], goals = ["biz", "selfcare"], pEffective = 0.5, taskTypes = ["bewith", "tell", "train"])
#should be APV.
marcy.makeTask(taskName = "become bo burnham", taskKind = "work", timeEst = 15, repeats = 0, goals = ["comms"], pEffective = 0.2, taskTypes = ["make", "edit", "listen", "watch", "do"], buildsCC = True)

marcy.bigRecalc()

marcy.markCompleted(3)

marcy.bigRecalc()

marcy.makeTask(taskName = "wew", taskKind = "work", timeEst = 9, goals = ["selfcare"], pEffective = 0.99)

a = marcy.getNeededTask(12*60, "either")

print(a)

print("That tasks's kind: " + a["taskKind"] + "!")
