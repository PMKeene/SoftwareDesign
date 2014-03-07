# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 12:05:58 2014

@author: maire
"""

import easygui as eg
import sys

while 1:
    title="Message from that random program"
    eg.msgbox("Hello, World!",title)
    
    msg="What is your favorite flavor?"
    title="Ice Cream Survey"
    choices=["Vanilla-based", "Chocolate-based", "Mint-based"]
    choice= eg.choicebox(msg, title, choices)
    
    #having the choices as strings means that a cancel returns None
    eg.msgbox("You chose: " + str(choice), "Survey Result")
    
    msg="Do you want to continue?"
    title="Please Confirm"
    if eg.ccbox(msg, title):
        pass
    else:
        sys.exit(0)