'''This is a simple example of how to use suggestion text.
In this example you setup a word_list at the begining. In this case
'the the quick brown fox jumps over the lazy old dog'. This list along
with any new word written word in the textinput is available as a
suggestion when you are typing. You can press tab to auto complete the text.
'''
import sys
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder


class MyTextInput(TextInput):

   def on_suggestion_text(self, instance, value):
        if not value:
            return
        super(MyTextInput, self).on_suggestion_text(instance, value)

   def keyboard_on_key_down(self, window, keycode, text, modifiers):
        '''
        '''
        if self.suggestion_text and keycode[1] == 'enter':  # complete suggestion_text
            self.insert_text(self.suggestion_text + ' ')
            self.suggestion_text = ''
            return True
        return super(MyTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)



class MyApp(App):

    def on_start(self):
        self.root.text = ""
        self.root.bind(text=self.on_text)
        self.word_list = ('the the quick brown fox jumps over the lazy old dog').split(' ')

    def on_text(self, instance, value):
        # include all current text from textinput into the word list
        # the kind of behavior sublime text has
        self.suggestion_text = ''
        word_list = list(set(self.word_list + value[:value.rfind(' ')].split(' ')))
        val = value[value.rfind(' ')+1:]
        if not val: return
        try:
            # grossly ineffecient just for demo purposes
            word = [word for word in word_list if word.startswith(val)][0][len(val):]
            if not word: return
            self.root.suggestion_text = word
        except IndexError:
            print('Index Error')

    def build(self):
        return Builder.load_string('''
MyTextInput
    readonly:False
    multiline:False
''')

if __name__ == "__main__":
    MyApp().run()
                     
