#import essential things
import os
import subprocess
import tinydb
from tinydb import TinyDB, Query
import random

#important bonuses, etc.
#test:20 best bonus values
interruptBonus = 1.5 #bonus multiplier for being something interruptable.
ongoingBonus = 5 #bonus multiplier for being infinitely repeating.
timeWorth = 17 #money I should be making ($/hr) to make it worth my time in terms of money.
usableMoney = 50 #get from moneymanagerEX or thereabouts.
ccOdds = 0.7 #probability that the task picked is good for building career capital (skills, connections, savings, broadly-applicable stuff, etc.)

#dependencies! access from marceline as marcy.dependency.amAdult, etc.
dependency = {
    "amAdult" : False, #am I a legal, free adult?
    "haveHome" : True, #do I have someplace to live?
    "ownHome" : False, #do I OWN where I live?
    "atHome" : True, #am I AT home, right now?
    "haveNet" : True, #do I have internet access?
    "notOnCampus" : True, #am I NOT using school resources?
    "notAtWork" : True, #am I NOT using work resources?
}

#goal probabilities (can stack to give task a higher chance!)
goalAllocated = {
    "ai" : 9,
    "selfcare" : 10,
    "biz" : 7,
    "comms" : 7
    #first youtube/writing, then three word title, then VR (???)
}


#important effectiveness/personal enjoyment stuff (can stack!)
#test:10 CALIBRATE USING LOGIC (equal times btw. certain things, etc.)
taskAllocated = {
    "ask" : 9,
    "tell" : 7,
    "make" : 9,
    "edit": 10,
    "train": 10,
    "do" : 5, #default

    "read" : 12,

    "bewith" : 9,
    "play" : 9,
    "watch" : 7,
    "listen" : 6,

    "meta" : 50
}


#important misc variables
#mainPath = os.path.dirname(os.path.abspath(__file__))
taskstorage = "storage/taskdb.json" #os.path.join(mainPath, "THE THING")
completedstorage = "storage/completeddb.json"
helpers = "helperscripts/"
taskdb = TinyDB(taskstorage)
completeddb = TinyDB(completedstorage)





#functions!
def makeTask(**kwargs):
    #default values
    kwargs.setdefault("APV", 0)#
    kwargs.setdefault("moneyNet", 0.00)#
    kwargs.setdefault("pEffective", .5)#
    kwargs.setdefault("canInterrupt", False)#
    kwargs.setdefault("taskTypes", ["do"]) #
    kwargs.setdefault("dependencies", []) #
    kwargs.setdefault("buildsCC", False) #
    kwargs.setdefault("goals", []) #
    kwargs.setdefault("taskDesc", "This description is pretty sparse. In fact, it doesn't exist!") #
    return taskdb.insert(dict(**kwargs)) #actually insert task
    ##taskKind = "fun" OR "work"
    ###buildsCC = False
    ##taskName = "wew"
    ##taskDesc = "go 2 tvtroeps"
    ###goals = ["selfcare", "comms"]
    ##timeEst = 20
    ###taskTypes = ["watch", "intake"]
    ###pEffective = 0.87
    ###dependencies = [amAdult, notAtWork, haveNet]
    ###canInterrupt = True
    #APV = ???
    ###moneyNet = -$5.00


def runAllHelpers(): #runs all scripts in helper script folder
    for filename in os.listdir(helpers): #os.listdir(
        subprocess.run("python " + os.path.join(helpers, filename))
        #exec(filename.read())


def goalSelect(): #selects random goal, based on above weights.
    r = random.uniform(0, sum(goalAllocated.values()))
    s = 0.0
    for key, value in goalAllocated.items():
        s += value
        if r < s: return key
    return key


def ccSelect(): #selects whether or not to go for career capital.
    return random.random() < ccOdds


def calcAPV(taskID):
    t = taskdb.get(eid=taskID)
    print(taskID)
    currentAPV = 10000
    print("From start: " + str(currentAPV))
    #looks at money
    if t["moneyNet"] > 0:
        currentAPV = currentAPV * ((t["moneyNet"]/t["timeEst"]) / (timeWorth/60))
        print("From moneyNet > 0: " + str(currentAPV)) #1
    elif t["moneyNet"] < 0:
        if (abs(t["moneyNet"]) > (usableMoney)) and (t["moneyNet"] != 0):
            print("From moneyNet < 0: " + str(currentAPV)) #1
            return 0
        else:
            currentAPV = currentAPV / ((abs(t["moneyNet"])/t["timeEst"]) / (timeWorth/60)) #if you don't have enough money, no use doing the task.
            print("From moneyNet not enough: " + str(currentAPV)) #1
    #calculate with dependencies
    depMult = 1
    if t["dependencies"] != []:
        for dep in t["dependencies"]:
            depMult = depMult * dependency[dep]
    #if one or more dependency isn't met, no use doing the task.
    if depMult == 0:
        return 0
    print("From depMult: " + str(currentAPV)) #2
    #calculate with interruptions!
    if t["canInterrupt"] == True:
        currentAPV = currentAPV * interruptBonus
    elif t["canInterrupt"] == False:
        currentAPV = currentAPV * 1
    print("From canInterrupt: " + str(currentAPV)) #4
    #calculate with taskTypes
    typeMult = 0
    for item in t["taskTypes"]:
        typeMult += taskAllocated[item]
    currentAPV = currentAPV * typeMult * (t["pEffective"]/100)
    print("Final APV for " + str(t.eid) + ": " + str(currentAPV))
    return currentAPV


def printAllAPVs():
    for item in taskdb.all():
        print("Ey, m80! The APV for " + str(item.eid) + " is " + str(item["APV"]))


def bigRecalc():
    #calculate all the APVs
    for theEID in range(1, len(taskdb)+1):
        if taskdb.contains(eids = [theEID]):
            taskdb.update({"APV" : calcAPV(theEID)}, eids = [theEID])
    printAllAPVs()


def markCompleted(taskID): #removes task from taskdb, writes to completeddb.
    completeddb.insert(taskdb.get(eid=taskID))
    taskdb.remove(eids = [taskID])
    print("Removed whatever THAT task was!")


def getNeededTask(timeNeeded, taskKindNeeded): #returns the full dict element thing.
    t = Query() #task being searched for.
    #randomly select stuff!
    g = goalSelect()
    c = ccSelect()
    #create temporary dictionary to store the tasks that fit the time, so they can be sorted
    gettingSorted = {}
    if taskKindNeeded == "either":
        print("It needs either!")
        for element in taskdb.search((t["goals"].any(g)) & (t["buildsCC"]==c) & (t["timeEst"] <= timeNeeded)):
            print(str(element.eid))
            gettingSorted[str(element.eid)] = element["APV"]
            print("Added " + str(element.eid) + " to gettingSorted!")
    elif (taskKindNeeded == "fun") or (taskKindNeeded == "work"):
        print("It needs " + taskKindNeeded + "!")
        for element in taskdb.search((t["goals"].any(g)) & (t["buildsCC"]==c) & (t["timeEst"] <= timeNeeded) & (t["taskKind"] == taskKindNeeded) & (t["APV"] != 0)):
            gettingSorted[str(element.eid)] = element["APV"]
    if gettingSorted == {}:
        return "Nope"
        print("Nope")
    #sort the items and figure out highest APV
    highestAPV = sorted(gettingSorted.values())[-1]
    print("Highest APV: " + str(highestAPV))
    #return the EID of random task with highest APV
    possibleEIDs = []
    for key, value in gettingSorted.items(): #make list of apvs to randomly pick from
        if value == highestAPV:
            possibleEIDs.append(key)
            print("Appended " + key + " to possibleEIDs!")
    if possibleEIDs == []:
        return "Nope"
        print("Nope")
    print("All the possible EIDs to pick: " + str(possibleEIDs))
    chosenEID = float(random.choice(possibleEIDs))
    print("Name: " + taskdb.get(eid=chosenEID)["taskName"])
    print("Description: " + taskdb.get(eid=chosenEID)["taskDesc"])
    print("Time you gots ta do it: " + str(taskdb.get(eid=chosenEID)["timeEst"]) + " minutes.")
    #return dict(taskdb.get(eid=chosenEID))
    return taskdb.get(eid=chosenEID)
