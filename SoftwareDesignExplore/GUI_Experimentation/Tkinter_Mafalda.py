# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 12:42:03 2014

@author: maire
"""

import Tkinter
from Tkinter import *
import ttk

root=Tkinter.Tk()
root.title('Sentiment Test')
root.configure(background='white')
label1=Label(text='What would you like to compare? (ex #fail, oscars)',background='white',foreground="gray38").pack(side=TOP,padx=10,pady=10)

E1=Entry(root,width=10)
E1.pack(side=TOP,padx=10,pady=10)

label2=Label(text='And what is the other one?', background='white',foreground="gray38").pack(side=TOP,padx=10,pady=10)
E2=Entry(root, width=10)
E2.pack(side=TOP,padx=10,pady=10)

def onok():
    hashtag1=E1.get()
    hashtag2=E2.get()
    make_graph(function(hashtag1),function(hashtag2),hashtag1,hashtag2)
    
ttk.Style().configure("TButton",padding=6,relief="flat", background="white")

ttk.Button(root, text='OK', command=onok).pack(side=LEFT)
ttk.Button(root, text='CLOSE', command=root.quit).pack(side=RIGHT)

root.mainloop()