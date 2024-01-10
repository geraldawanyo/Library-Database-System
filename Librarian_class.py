# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:26:31 2023

@author: User
"""
from Book_class import Book
from User_class import User

class Librarian(User):
    def __init__(self,db,acc,):
        super().__init__(db,acc)
        

        
    def menu(self):
        '''
        EXECUTES LIBRARIAN MENU OF LIBRARY FUNCTIONS

        Returns
        -------
        None.

        '''
        
        print(f"""menu for Librarian
1. Option 1 ~Search books
2. Option 2 ~User Record
3. Option 3 ~Add book
4. Option 4 ~Return book
5.  Option 5 ~Reserve book
q. Return

""")
        while True:
            c = input("\nSelect Option (1-5|q): ")
            choice1 = {"1" :self.f_opt1,
                  "2" :self.f_opt2,
                  "3" :self.f_opt3,
                  "4" :self.f_opt4,
                  "5" :self.f_opt5,
                  "q" :"q"}.get(c,"invalid")        
            if choice1 == "q":
                print('Bye..')
                LibManSystem.reg_or_login()
                break
            elif choice1 != "invalid":
                choice1()
            else:
                print("Try again...")
    def f_opt1(self):
        '''
        ALLOWS USER TO SEARCH UP BOOKS IN LIBRARY DATABASE

        Returns
        -------
        None.

        '''
        print("option-1")
        print(f'options:isbn, title,author')
        opt = str(input("Search options: title, author, language, year  or any: " ))
        s = str(input("Enter title/author: "))
        data = self.db.search(opt,s)
        print('\nSearch Results:\n','-'*20)
        for i , b in enumerate(data):
             print("isbn =", {b[0]})
             print("title =", b[1])
             print("author =", b[2])
             print("issue_status =", b[3])
             print("Language =", b[4])
             print("Publication year =", b[5])
             print('-'*20)
             
             
    def f_opt2(self):
        '''
        ALLOWS USER TO UPDATE THE DETAILS OF A BOOK ON THE LIBRARY DATABASE

        Returns
        -------
        None.

        '''
        print("option-2")
        isbn = input("Enter isbn: ")
        print('\nBook details:\n','-'*20)
        print(self.db.getBooks(isbn))
        updt_lang = input("Update Language of Book?: ")
            
        if updt_lang == "Yes":
            lang = input("Enter Language: ")
            self.db.update_lang(isbn,lang)
                
        elif updt_lang == "No":
            pass
            
        updt_pub = input("Update publication date?: ")
            
        if updt_pub == "Yes":
                
            pub = input("Enter date: ")
            self.db.update_pub_date(isbn, pub)
                
        elif updt_pub == "No":
            pass
            
        if updt_lang == "Yes" or updt_pub == "Yes":
                print('\nUpdated Book details:\n','-'*20)
                print(self.db.getBooks(isbn))
                
        else:
            pass

    def f_opt3(self):
        '''
        ALLOWS USER TO ADD A BOOK TO THE LIBRARY DATABASE

        Returns
        -------
        None.

        '''
        self.db.add_book()
    
    def f_opt4(self):
        '''
        ALLOWS USER TO REMOVE A BOOK FROM THE LIBRARY DATABASE

        Returns
        -------
        None.

        '''
        isbn = input("Enter isbn: ")
        self.db.remove_book(isbn)
        
            
    def f_ex(self):
            pass
    def __repr__(self):
            return f"{self.f}\n {self.acc}"
   
    
from LibManSystem_class import LibManSystem