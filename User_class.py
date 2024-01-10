# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:27:37 2023

@author: User
"""

class User:
    def __init__(self, db,acc):
        self.db = db
        self.acc = acc

        
    def __repr__(self):
        return f"{self.name}"
    
