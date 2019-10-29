#https://tinydb.readthedocs.io/en/latest/getting-started.html#basic-usage
#http://tinydb.readthedocs.io/en/latest/usage.html

#UNDERSTAND ELEMENTS OF DB ENTRIES

#import essential things
import os
import tinydb
from tinydb import TinyDB, Query
from datetime import date, timedelta
import calendar
import random


#important misc variables
taskstorage = "testdb.json"
helpers = "helperscripts/"
testdb = TinyDB(taskstorage)
interruptBonus = 1.5


#goal probabilities
goalAllocated = {
    "controlproblem" : 9,
    "selfcare" : 10,
    "business" : 7,
    "threewordtitle" : 7
}


#important effectiveness/personal enjoyment stuff (can stack!)
taskAllocated = {
    "ask" : 8,
    "tell" : 7,
    "make" : 9,
    "edit": 10,
    "train": 10,
    "intake" : 8,
    "do" : 6, #default
    "bewith" : 10,

    "play" : 8,
    "watch" : 8,
    "listen" : 7
}


#dependencies! access from marceline as marcy.dependency.amAdult, etc.
dependency = {
    "usableMoney" : 13.66, #get from moneymanagerEX or thereabouts.
    "bookmansCredit" : 0, #see above
    "amAdult" : 0, #am I a legal, free adult?
    "haveHome" : 1, #do I have someplace to live?
    "ownHome" : 0, #do I OWN where I live?
    "atHome" : 1, #am I AT home, right now?
    "haveNet" : 1, #do I have internet access?
    "notOnCampus" : 1, #am I NOT using school resources?
    "notAtWork" : 1, #am I NOT using work resources?
    "bookmansBagIsClean" : 0, #has the Bookman's bag stuff had stuff erased?
}


#functions!

def makeTask(**kwargs):
    kwargs.setdefault("APV", 0)
    kwargs.setdefault("moneyNet", 0.00)
    kwargs.setdefault("canInterrupt", False)
    kwargs.setdefault("taskTypes", ["do"])
    kwargs.setdefault("dependencies", [])
    kwargs.setdefault("completed", False)
    testdb.insert(dict(**kwargs))
    ##taskKind = "fun"
    ##taskName = "wew"
    ##taskDesc = "go 2 tvtroeps"
    ##goal = "selfcare"
    ###timeEst = 20
    ###taskTypes = ["watch", "intake"]
    ###pEffective = 0.87
    #dependencies = [amAdult, notAtWork, haveNet]
    ###canInterrupt = True
    #completed = False
    #APV = ???
    #moneyNet = -$5.00


def runAllHelpers(): #runs all scripts in helper script folder
    for filename in os.listdir(helpers):
        exec(filename.read())


def goalSelect():
    r = random.uniform(0, sum(goalAllocated.values()))
    s = 0.0
    for key, value in goalAllocated.items():
        s += value
        if r < s: return key
    return key


def calcAPV(taskID):
    t = testdb.get(eid=taskID)
    currentAPV = t["timeEst"] * t["pEffective"]
    if t["moneyNet"] > 0:
        currentAPV = currentAPV * t["moneyNet"]
    elif t["moneyNet"] < 0:
        currentAPV = currentAPV / abs(t["moneyNet"])
    if t["canInterrupt"] == True:
        currentAPV = currentAPV * interruptBonus
    elif t["canInterrupt"] == False:
        currentAPV = currentAPV * 1
    #INSERT PART TO CALCULATE THE DEPENDENCIES IN!
    typeMult = 0
    for item in t["taskTypes"]:
        typeMult += taskAllocated[item]
    currentAPV = currentAPV * typeMult
    return currentAPV
    

def printAllAPVs():
    for item in testdb.all():
        print(item["APV"])


def bigRecalc():
    #calculate all the APVs
    for item in testdb.all():
        a = calcAPV(item.eid)
        testdb.update({"APV" : calcAPV(item.eid)}, eids = [item.eid])
    printAllAPVs()


##def changeSomething():
##    lelist = []
##    for item in testdb.all():
##        lelist.append(item.eid)
##    leBestEid = random.choice(lelist)
##    eToChange = random.choice()


##stuff to do when opening the program and after a dependency is updated:
##    bigRecalc()
##    runAllHelpers()

def getNeededTask(timeNeeded, taskKindNeeded):
    t = Query() #task being searched for.
    #randomly select stuff!
    g = goalSelect()
    #create temporary dictionary to store the tasks that fit the time, so they can be sorted
    gettingSorted = {}
    for item in testdb.search((t["goal"] == g) & (t["timeEst"] <= timeNeeded) & (t["taskKind"] == taskKindNeeded)):
        gettingSorted[item.eid] = item["APV"]
    #sort the items and figure out highest APV
    highestAPV = sorted(gettingSorted.values())[-1]
    #return the EID of random task with highest APV
    possibleEIDs = []
    for key, value in gettingSorted.items(): #make list of apvs to randomly pick from
        if value == highestAPV:
            possibleEIDs.append(key)
    chosenEID = random.choice(possibleEIDs)
    return testdb.get(eid=chosenEID)
