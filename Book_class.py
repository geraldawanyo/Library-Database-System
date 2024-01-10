# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:22:31 2023

@author: User
"""
class Book:
  def __init__(self,isbn,title,author, issue_status, language, publication_date):
      self.isbn = isbn
      self.title = title
      self.author = author
      self.issue_status = issue_status
      self.language = language
      self.publication_date = publication_date
      
      
      

  def __repr__(self): 
      return f"isbn:{self.isbn},\ntitle:{self.title},\nauthor:{self.author},\nissue_status:{self.issue_status}, \nlanguage:{self.language}, \npublication_date:{self.publication_date}"
  
  
