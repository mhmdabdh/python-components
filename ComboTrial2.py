import Tkinter
import ttk
import sqlite3

#__version__ = "1.1"

# I may have broken the unicode...
#Tkinter_umlauts=['odiaeresis', 'adiaeresis', 'udiaeresis', 'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']

class AutocompleteCombobox(ttk.Combobox):

        def set_completion_list(self, completion_list):
                """Use our completion list as our drop down selection menu, arrows move through menu."""
                self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)
                self['values'] = self._completion_list  # Setup our popup menu

        def autocomplete(self, delta=0):
                """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
                if delta: # need to delete selection otherwise we would fix the current position
                        self.delete(self.position, Tkinter.END)
                else: # set position to end so selection starts where textentry ended
                        self.position = len(self.get())
                # collect hits
                _hits = []
                for element in self._completion_list:
                        if element.lower().startswith(self.get().lower()): # Match case insensitively
                                _hits.append(element)
                # if we have a new hit list, keep this in mind
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
                # only allow cycling if we are in a known hit list
                if _hits == self._hits and self._hits:
                        self._hit_index = (self._hit_index + delta) % len(self._hits)
                # now finally perform the auto completion
                if self._hits:
                        self.delete(0,Tkinter.END)
                        self.insert(0,self._hits[self._hit_index])
                        self.select_range(self.position,Tkinter.END)

        def handle_keyrelease(self, event):
                """event handler for the keyrelease event on this widget"""
                if event.keysym == "BackSpace":
                        self.delete(self.index(Tkinter.INSERT), Tkinter.END)
                        self.position = self.index(Tkinter.END)
                if event.keysym == "Left":
                        if self.position < self.index(Tkinter.END): # delete the selection
                                self.delete(self.position, Tkinter.END)
                        else:
                                self.position = self.position-1 # delete one character
                                self.delete(self.position, Tkinter.END)
                if event.keysym == "Right":
                        self.position = self.index(Tkinter.END) # go to end (no selection)
                if len(event.keysym) == 1:
                        self.autocomplete()
                # No need for up/down, we'll jump to the popup
                # list at the position of the autocompletion


def test(test_list):
        """Run a mini application to test the AutocompleteEntry Widget."""
        root = Tkinter.Tk(className='AutocompleteCombobox')

        combo = AutocompleteCombobox(root)
        combo.set_completion_list(test_list)
        combo.pack()
        combo.focus_set()
        # I used a tiling WM with no controls, added a shortcut to quit
        root.bind('<Control-Q>', lambda event=None: root.destroy())
        root.bind('<Control-q>', lambda event=None: root.destroy())
        root.mainloop()

if __name__ == '__main__':
        #test_list = ('apple', 'banana', 'CranBerry', 'dogwood', 'alpha', 'Acorn', 'Anise', 'crannotberry' )
        #test(test_list)

        connection = sqlite3.connect('sicotrichy_qa')
        cur = connection.cursor()
        cur.execute("select  stock_item_name  from tr_inventory")
        sqloutput = cur.fetchall()  #This contains the SQL output in format [(u'data1',), (u'data2',), (u'data3',)]
        sqloutput_2 = [item[0] for item in sqloutput]  #This is manipulated to the format [u'data1',u'data2',u'data3']
        test_list = tuple(map(str, sqloutput_2))  #This will remove the unicode data and final format [data1,data2,data3]
        #print test_list
        test(test_list)