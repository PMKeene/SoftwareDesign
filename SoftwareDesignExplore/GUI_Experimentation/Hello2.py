# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 01:57:24 2014

@author: maire
"""
##AAAAAANNNNDDDD Errors
from Tkinter import *

class App:
    def _init_(self,master):
        frame=Frame(master)
        frame.pack()
        
        self.button=Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        
        self.hi_there=Button(frame, text="Hello", command= self.say_hi)
        self.hi_there.pack(side=LEFT)
        
    def say_hi(self):
        print "Howdy thar!"
    
root=Tk()

app=App(root)

root.mainloop()
root.destroy()
