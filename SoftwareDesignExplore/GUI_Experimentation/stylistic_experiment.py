# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 13:11:47 2014

@author: maire
"""

import ttk
import Tkinter

root=Tkinter.Tk()

##Style thingy 1
ttk.Style().configure("TButton",padding=16,relief="flat", background="#ccc")

btn=ttk.Button(text="Sample").pack()
#btn.pack()

##Style thingy 2
style=ttk.Style()
style.map("C.TButton", 
          foreground=[('pressed','red'),('active','blue')],
          background=[('pressed','!disabled','black'),('active','white')]
          )
colored_btn= ttk.Button(text="Test",style="C.TButton").pack()

##Experimental
root.mainloop()