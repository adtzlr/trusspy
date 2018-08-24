# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:25:00 2018

@author: dutzi
"""

def licen():
    import os
    print(os.getcwd())
    with open('trusspy/LICENSE', 'r') as f: 
        for i,line in enumerate(f): 
            if i < 622:
                print(line)

def warran():
    with open('trusspy/LICENSE', 'r') as f: 
        for i,line in enumerate(f): 
            if i>587 and i<620:
                print(line)