#http://easygui.sourceforge.net/
#http://www.ferg.org/easygui/tutorial.html#contents_item_1

#http://home.wlu.edu/~lambertk/breezypythongui/

#http://stackoverflow.com/a/38057351

#import essential stuff!
import os
import subprocess
import tinydb
from tinydb import TinyDB, Query
import random
import re
import marcy
from appJar import gui

#USE THIS ONE: http://appjar.info/
#CHECK THEIR HELP, TOO!

#interface usability variables (timing, colors, etc)
depGridWidth = 2
activeTabColor = "White"
inactiveTabColor = "LightSalmon"
satisfiedConditionColor = "Lime"
tabTextColor = "Red"
entryBgColor = "Coral"
entryTextColor = "White"
#taskEntryBgColor = "White"
taskEntryTextColor = "OrangeRed"
#icon = "newicon_rightsize.gif"
marcy.runAllHelpers()
#marcy.bigRecalc() #ALSO run when a dependency is changed at all.

app = gui("Marceline") #starts up the window
app.startTabbedFrame("Tabs") #start up tabs
def setInterfaceStuff():
    #app.setIcon(icon)
    app.setGeometry("945x935")
    #app.setResizable(canResize=False)
    app.setLocation(220, 70)
    app.setBg("White")
    app.setTabbedFrameActiveBg("Tabs", activeTabColor)
    app.setTabbedFrameInactiveBg("Tabs", inactiveTabColor)
    #app.setTabbedFrameBg("Tabs", "White")
    app.setTabbedFrameActiveFg("Tabs", tabTextColor)
    app.setLabelFont(20, font="Courier") #normie font.
    app.setButtonFont(15, font="Sans Serif") #button font.
setInterfaceStuff()



app.startTab("Do")
#actual/interface stuff
app.addLabel("iveGotText", "I've got", 0, 0)
app.addNumericEntry("timeNeededInput", 1, 0)

app.setFocus("timeNeededInput")
app.setEntryBg("timeNeededInput", entryBgColor)
app.setEntryFg("timeNeededInput", entryTextColor)

app.addLabel("minutesText", "minutes.", 2, 0)
app.addLabel("titleIndicator", "Title:", 0, 1)
app.addLabel("descIndicator", "Description:", 2, 1)
app.addLabel("moneyIndicator", "Net Money:", 2, 2)
app.addLabel("interruptIndicator", "Interruptable?:", 0, 2)
app.addEmptyLabel("task title", 1, 1, 1, 1)
app.addEmptyMessage("task description", 4, 1, 1, 2)
app.addLabel("money", "0.0", 3, 2, 1, 1)
app.addEmptyLabel("interrupt?", 1, 2, 1, 1)
app.addEmptyMessage("realGoals", 4, 2, 1, 1)
app.setLabelFg("titleIndicator", tabTextColor)
app.setLabelFg("descIndicator", tabTextColor)
app.setLabelFg("moneyIndicator", tabTextColor)
app.setLabelFg("interruptIndicator", tabTextColor)

#app.addLabelOptionBox("Task Kind", ["fun", "work", "either"], 4, 0)
#app.setOptionBox("Task Kind", 0)
leLink = ""
def submitNeeded(self):
    marcy.bigRecalc()
    global currentTask
    currentTask = marcy.getNeededTask(app.getEntry("timeNeededInput"), "fun")
    if currentTask == "Nope":
        app.setLabel("task title", "Try Again!")
        app.clearMessage("task description")
        app.setMessage("realGoals", "")
        app.setLabel("money", 0.00)
        app.setLabel("interrupt?", "")
        print("No task available! Try again!")
        return "Nope"
    else:
        app.setLabel("task title", currentTask["taskName"])
        app.setMessage("task description", currentTask["taskDesc"])
        leLink = re.search("(?P<url>https?://[^\s]+)", currentTask["taskDesc"]).group("url")
        if leLink is not None:
            app.addWebLink(str(leLink), leLink, 1, 0)
        app.setLabel("money", currentTask["moneyNet"])
        app.setLabel("interrupt?", str(currentTask["canInterrupt"]))
        app.setMessage("realGoals", ", ".join(sorted(currentTask["goals"])))
        #test:30 best colors to deliver this info with.
        return currentTask["taskName"]


app.addButton("Let's do it!", submitNeeded, 3, 0)
def killTask(self):
    if currentTask != "Nope":
        marcy.markCompleted(currentTask.eid)
        app.setLabel("task title", "Done!")
        app.setLabel("task description", "")
app.addButton("All done!", killTask, 5, 1)

#keybinding stuff
#app.enableEnter(submitNeeded)
#def changeTaskKind(self):
    #if app.getOptionBox("Task Kind") == "either":
        #app.setOptionBox("Task Kind", 0)
    #else (add colon)
        #app.setOptionBox("Task Kind", (["fun", "work", "either"].index(app.getOptionBox("Task Kind")) + 1))
#app.bindKey("TAB", changeTaskKind)
#def quit(self):
    #app.stop()
#app.bindKey("Q", quit) # press shift-q to quit!!!!!!!!!!
app.stopTab()






app.startTab("Add")
#unbinds keys so you can use them to type.
#app.unbindKey("c")
#app.unbindKey("Q")
#app.disableEnter()
#populatetom fos typeList and depList with the task types and dependencies from marcy
typeList = {}
depList = {}
def populateLists():
    for key in marcy.taskAllocated:
        if key == "do":
            typeList[str(key)] = True #so "do" is the default.
        else:
            typeList[str(key)] = False
    for otherKey in marcy.dependency:
        depList[str(otherKey)] = False
    print(typeList)
    print(depList)
populateLists()

app.addLabel("Task Name: ", "Task Name: ", 0, 0)
app.addEntry("name", 0, 1) #taskName #
app.setFocus("name")
app.addNumericEntry("time estimate", 0, 2) #timeEst #
app.addTextArea("description", 1, 0) #taskDesc #
app.addNumericEntry("netmoney", 1, 1) #moneyNet
app.addNumericEntry("effective", 1, 2) #pEffective #
app.addCheckBox("interrupt", 5, 0) #canInterrupt
app.addCheckBox("cc", 5, 1) #buildsCC #
app.addProperties("Task Type(s): ", typeList, 3, 0) #taskTypes # #
app.addProperties("Dependency(s): ", depList, 3, 1) #dependencies # #
app.addProperties("Goal(s): ", {"ai":False, "biz":False, "comms":False, "selfcare":False}, 3, 2) #goals #


def setAllEntryShit():
    app.setEntryFg("name", taskEntryTextColor)
    app.setTextAreaFg("description", taskEntryTextColor)
    app.setTextAreaBg("description", "Honeydew")
    app.setEntryFg("effective", taskEntryTextColor)
    app.setEntry("effective", 50)
    app.setEntryFg("netmoney", taskEntryTextColor)
    app.setEntry("netmoney", 0.00)
    app.setEntry("time estimate", 5)
    #app.setCheckBox("interrupt", False)
    app.getPropertiesWidget("Task Type(s): ").config(font="Courier 14")
    app.getPropertiesWidget("Dependency(s): ").config(font="Courier 14")
    app.getPropertiesWidget("Goal(s): ").config(font="Courier 14")
    app.getCheckBoxWidget("interrupt").config(font="Courier 14")
    app.getCheckBoxWidget("cc").config(font="Courier 14")
setAllEntryShit()
def setBackToNormal():
    app.setEntry("effective", 50)
    app.setEntry("netmoney", 0.00)
    app.setCheckBox("interrupt", False)
    app.setCheckBox("cc", False)
    app.clearEntry("name")
    app.clearTextArea("description")
    app.setEntry("time estimate", 5)
def submitTask(self):
    #makes list of checked goals
    losGoals = []
    for go, goVal in app.getProperties("Goal(s): ").items():
        if goVal == True:
            losGoals.append(go)
    #makes lists of types and dependencies.
    losTypes = []
    losDeps = []
    for ty, tyVal in app.getProperties("Task Type(s): ").items():
        if tyVal == True:
            losTypes.append(ty)
    for de, deVal in app.getProperties("Dependency(s): ").items():
        if deVal == True:
            losDeps.append(de)
    #actually makes the task.
    marcy.makeTask(taskName = app.getEntry("name"), taskDesc = app.getTextArea("description"), pEffective = app.getEntry("effective"), taskKind = "fun", buildsCC = app.getCheckBox("cc"), moneyNet = app.getEntry("netmoney"), canInterrupt = app.getCheckBox("interrupt"), taskTypes = losTypes, dependencies = losDeps, goals = losGoals, timeEst = app.getEntry("time estimate"))
    setBackToNormal()

app.addButton("Add it!", submitTask, 5, 2) #
app.stopTab()
app.stopTabbedFrame() #stop doing tabs.
app.go() #liftoff!
