# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:20:42 2023

@author: User
"""
import sqlite3
import json
from datetime import datetime
from Book_class import Book
class LibDatabase:
    
    
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        #self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS  books(
                isbn INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                issue_status TEXT,
                language TEXT,
                publication_date TEXT
                )""")
    
   


    def insertBook(self,b):    
        '''
        

        Parameters
        ----------
        b : INPUT BOOK(ISBN, TITLE, AUTHOR, ISSUE_STATUS, LANGUAGE, PUBLICATION_DATE)

        Returns
        -------
        INSERTS BOOK DETIALS INTO DATABASE

        '''
        with self.conn:
            self.c.execute('INSERT OR IGNORE INTO books VALUES(:isbn,:title,:author,:issue_status,:language,:publication_date)',
                           {'isbn':b.isbn,'title':b.title,'author':b.author, 
                            'issue_status':b.issue_status, 'language':b.language, 'publication_date':b.publication_date})

    def search(self,opt,s):
        '''
        

        Parameters
        ----------
        opt :INPUT SEARCH FILTER (SEARCH BY TITLE, AUTHOR, LANGUAGE, YEAR or ANY)
        
        s : SEARCH INPUT

        Returns
        -------
        LIST OF BOOKS CORRESPONDING WITH SEARCH INPUT
            

        '''
        s = '%'+s+'%'
        cmd = f'SELECT * FROM books WHERE {opt} LIKE :s'
        if opt in ['title','author','language']:
            self.c.execute(cmd, {'s':s})
                 
        elif opt == 'year':
            self.c.execute('SELECT * FROM books WHERE publication_date LIKE :s', {'s':s})
            # c.execute('SELECT * FROM books WHERE title =:s', {'s':s})
        else: 
            self.c.execute("""SELECT * FROM books WHERE author LIKE :s OR title LIKE :s 
                           OR language LIKE :s OR publication_date LIKE :s""", {'s':s})
            # c.execute('SELECT * FROM books WHERE author =:s', {'s':s})
        return self.c.fetchall()
        
            
        
        
    def getBooks(self,isbn):
        '''
        

        Parameters
        ----------
        isbn : INPUT ISBN

        Returns
        -------
        data : TITLE OF BOOK

        '''
        with  self.conn:
            self.c.execute('''SELECT isbn, title, author, language,
                           publication_date FROM books WHERE isbn = ?''',(isbn,))
            data = self.c.fetchone()
        return data
            
    def view_status(self,isbn):
        '''
        

        Parameters
        ----------
        isbn : INPUT ISBN

        Returns
        -------
        THE ISSUE STATUS OF BOOK (ISSUED, RETURNED OR NONE)

        '''
        with  self.conn:
            self.c.execute('SELECT issue_status FROM books WHERE isbn = ?', (isbn,))
            data = self.c.fetchone()
        return data[0]
        
    
    def issue_book(self, isbn):
        '''

        Parameters
        ----------
        isbn : INPUT ISBN

        Returns
        -------
        UPDATES THE ISSUE STATUS OF BOOK TO 'ISSUED'.

        '''
        with  self.conn:
            self.c.execute("""UPDATE books SET issue_status= 'issued'
                      WHERE isbn = ?""", (isbn,))
            return self.c.fetchone()
                      
    def return_book(self,isbn):
        '''

        Parameters
        ----------
        isbn : INPUTS ISBN

        Returns
        -------
        UPDATES THE ISSUE STATUS OF BOOK TO 'RETURNED'.

        '''
        with  self.conn:
            self.c.execute("""UPDATE books SET issue_status= 'returned'
                      WHERE isbn = ?""", (isbn,))
            return self.c.fetchone()
                      
    def remove_book(self,isbn):
        '''

        Parameters
        ----------
        isbn : INPUT ISBN OF BOOK TO DELETE FROM DATABASE

        Returns
        -------
        None.

        '''
        with  self.conn:
            self.c.execute("""DELETE from books WHERE isbn = ?""",
                      (isbn,))
            
    def update_lang(self, isbn, lang):
        '''

        Parameters
        ----------
        isbn : INPUT ISBN OF BOOK TO UPDATE
        lang : INPUT NEW LANGUAGE

        Returns
        -------
        None.

        '''
        with  self.conn:
            update_query = """UPDATE books SET language = ? WHERE isbn = ?"""
            data = (lang, isbn)
            self.c.execute(update_query,data)
    
    def update_pub_date(self, isbn, pub):
        '''

        Parameters
        ----------
        isbn : INPUT ISBN OF BOOK TO UPDATE
        
        pub : INPUT NEW PUBLICATION DATE

        Returns
        -------
        None.

        '''
        with  self.conn:
            update_query = """UPDATE books SET publication_date = ? WHERE isbn = ?"""
            data = (pub, isbn)
            self.c.execute(update_query,data)
            
    def add_book(self):
        '''
        INSERTS NEW BOOK INTO LIBRARY DATABASE

        Returns
        -------
        None.

        '''
        isbn = input("Enter isbn of book: ")
        title = input("Enter title of book: ")
        author = input("Enter author of book: ")
        language = input("Enter language of book: ")
        pub_date = str(input("Enter publication date of book: "))
        
        new_book = Book(isbn,title,author,None, language, pub_date)
        self.insertBook(new_book)
            
            
    def loadBooks(self):
        '''
        LOADS BOOKS FROM JSON FILE INTO LIBRARY DATABASE

        Returns
        -------
        None.

        '''
        with open('book2.json') as fd:
            books= json.load(fd)
            for b in books:
                #print(b)
                nb= Book(b["isbn"],b["title"],b["authors"],b["issue_status"], b["language_code"],b["publication_date"])
                print(nb)
                
                self.insertBook(nb)            

    
