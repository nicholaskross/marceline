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
import marcy
from appJar import gui

#USE THIS ONE: http://appjar.info/
#CHECK THEIR HELP, TOO!

#interface usability variables (timing, colors, etc)
activeTabColor = "White"
inactiveTabColor = "LightSalmon"
satisfiedConditionColor = "Lime"
tabTextColor = "Red"
entryBgColor = "Coral"
entryTextColor = "White"
#icon = "newicon_rightsize.gif"

marcy.runAllHelpers()
marcy.bigRecalc() #ALSO run when a dependency is changed at all.

app = gui("Marceline") #starts up the window
app.startTabbedFrame("Tabs") #start up tabs
def setInterfaceStuff():
    #app.setIcon(icon)
    app.setGeometry("940x680")
    #app.setResizable(canResize=False)
    app.setLocation(480, 180)
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
app.addEmptyLabel("task title", 1, 1, 1, 1)
app.addLabel("descIndicator", "Description:", 2, 1)
app.addEmptyLabel("task description", 3, 1, 1, 2)

app.setLabelFg("titleIndicator", tabTextColor)
app.setLabelFg("descIndicator", tabTextColor)

def submitNeeded(self):
    t = marcy.getNeededTask(app.getEntry("timeNeededInput"), app.getOptionBox("Task Kind"))
    if t == "Nope":
        app.setLabel("task title", "Try Again!")
        app.setLabel("task description", "")
        print("No task available! Try again!")
    else:
        app.setLabel("task title", t["taskName"])
        app.setLabel("task description", t["taskDesc"])

app.addButton("Let's do it!", submitNeeded, 3, 0)
app.addLabelOptionBox("Task Kind", ["fun", "work", "either"], 4, 0)
app.setOptionBox("Task Kind", 0)
#keybinding stuff
app.enableEnter(submitNeeded)
def changeTaskKind(self):
    if app.getOptionBox("Task Kind") == "either":
        app.setOptionBox("Task Kind", 0)
    else:
        app.setOptionBox("Task Kind", (["fun", "work", "either"].index(app.getOptionBox("Task Kind")) + 1))
app.bindKey("c", changeTaskKind)
def quit(self):
    app.stop()
app.bindKey("Q", quit) # press shift-q to quit!!!!!!!!!!
#SOMEHOW MAKE IT CHANGE ITS INTERFACE (TO SHOW TASK, ETC) WITHOUT LEAVING THE TAB OR WINDOW. IF POSSIBLE.
#if the task description has a URL in it, do app.addWebLink("http:666ETCtheurl.cock", "http://appJar.info")
app.stopTab()


app.startTab("Add")
#interface stuff
#USE AUTO ENTRY STUFF! AND .setEntryDefault(title, text)
app.addLabel("addPlaceholder", "add tasks")
#add stuff
app.stopTab()









app.startTab("Conditions")
#interface stuff
app.addLabel("conditionsPlaceholder", "view and change conditions")
#add stuff in the Conditions tab.
app.stopTab()


app.stopTabbedFrame() #stop doing tabs.
app.go() #liftoff!
