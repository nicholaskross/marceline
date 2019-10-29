#import essential things
import os
import subprocess
import tinydb
from tinydb import TinyDB, Query
import random
import marcy

marcy.makeTask(taskName = "eat shit", taskDesc = "you know who you are", timeEst = 20, taskKind = "fun", goals = ["selfcare", 'ai', "biz", "comms"], buildsCC = True)

print(str(marcy.taskdb))
