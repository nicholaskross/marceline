#import shit
import marcy
import os
import tinydb
from tinydb import TinyDB, Query
import random

marcy.runAllHelpers()

#make first task. should be obviously better BUT more expensive.
marcy.makeTask(taskName = "buy a safe", taskDesc = "buy.", goals = ["ai", "selfcare", "biz", "comms"], timeEst = 30, taskKind = "work", taskTypes = ["edit", "bewith", "train", "read", "play", "make", "tell", "ask", "watch", "listen", "do"], canInterrupt = True, moneyNet = -100)

#make second task. this one is obviously worse, but also actually affordable.
marcy.makeTask(taskName = "buy a book", taskDesc = "also buy.", goals = ["ai", "selfcare", "biz", "comms"], timeEst = 30, taskKind = "work")

marcy.bigRecalc()
marcy.getNeededTask(30, "work")
