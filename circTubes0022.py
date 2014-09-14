#!/usr/local/bin/python     
from Tkinter import *
import math
#import Pmw

master = Tk()

c = Label(master, text = "Select correlation")
c.grid(row = 0, column = 3)

w = Spinbox(values = ("Petukhov","Gnielinski","Dittus - Boelter","Sieder and Tate"))
w.grid(row = 1, column = 3)

def callback():
    if w.get() == "Dittus - Boelter":
        import DittusBoetler02
        DittusBoetler02       
           
    elif w.get() == "Sieder and Tate":
        import SiederTate02
        SiederTate02
        
    elif w.get() == "Petukhov":
        import Petukhov02
        Petukhov02
    elif w.get() == "Gnielinski":
        import Gnielinski02
        Gnielinski02
        


def about():
    def quit2():
        root.destroy()
    
    if __name__ == '__main__':
       root = Tk()
       #print units.get()
       lab1 = Label(root, text = 'circTubes v 0.2')
       lab1.pack(side = TOP)
       lab2 = Label(root, text = 'By W. Lamont')
       lab2.pack(side = TOP)
       lab3 = Label(root, text = 'Oct, 2012')
       lab3.pack(side = TOP) 
       #print ents 
       b3 = Button(root, text='Quit', command=quit2)
       b3.pack(side=LEFT, padx=5, pady=5)
       root.mainloop()

def quit():
    global master
    master.destroy()

b = Button(master, text="Ok", width=10, command=callback)
b.grid(row = 2, column = 3)
b4 = Button(master, text='About', width=10, command=about)
b4.grid(row = 3, column =3)
b5 = Button(master, text='Quit', width=10, command=quit)
b5.grid(row = 4, column =3)


#Button(master, text='Quit', command=master.quit).grid(row=5, column=2, sticky=W, pady=4)

mainloop()
