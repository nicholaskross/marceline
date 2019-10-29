#import shit
import marcy
import kivy
import tinydb
#IMPORT THE OTHER STUFF FROM MARCY!

#https://kivy-designer.readthedocs.io/en/latest/tools.html
#https://kivy.org/docs/gettingstarted/examples.html
#https://github.com/kivy/kivy-designer
#http://stackoverflow.com/questions/31458331/running-multiple-kivy-apps-at-same-time-that-communicate-with-each-other?noredirect=1&lq=1

#https://github.com/kivy/kivy/wiki/Snippets
#https://github.com/kivy/kivy/wiki/User-Snippets

#http://stackoverflow.com/a/38057351


#interface usability variables (timing, colors, etc)
#big/display text: Chewy (color: ff531c; )
#normal interface text: Roboto Regular (color: HTML; )
#http://cheparev.com/kivy-connecting-font/
#color for currently-satisfied conditions: 5cb85c
#else (background, etc): white

#the stuff begins
#MAKE IT TABBED! (L->R: Do, Add, Conditions)

kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.label import Label


class Marceline(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    Marceline().run()
