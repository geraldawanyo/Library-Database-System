# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:28:26 2023

@author: User
"""
from datetime import datetime
from User_class import User

class Student(User):
    b_limit = 5
    def __init__(self,db,acc):
        super().__init__(db,acc)
        



    def menu(self):
        '''
        EXECUTES STUDENT MENU OF LIBRARY FUNCTIONS

        Returns
        -------
        None.

        '''
        
        print(f"""menu for Student
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
        print("option-1 - Search Library")
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
        PRINTS THE STUDENT USER'S LIBRARY REPORT

        Returns
        -------
        None.

        '''
        print("option-2 - View User Record")
        self.acc.printBorrowedBooks()
        self.acc.printReturnedBooks()
        self.acc.printReservedBooks()
        self.acc.printLostBooks()
        self.acc.printAccFine()
        self.acc.check_b_time()
        
    def f_opt3(self):
        '''
        ALLOWS USER TO INPUT ISBN OF BOOK TO BORROW. METHOD CHECKS THE 
        BOOK AVAILABILITY AND WHETHER USER HAS REACHED BOOK LIMIT BEFORE ADDING 
        BOOK TO THE USER'S ACCOUNT ALONG WITH THE DATE IT WAS BORROWED

        Returns
        -------
        None.

        '''
        print("option-3 - Borrow a Book")
        c_date_us = datetime.now()    # Current date in US format
        c_date_uk = c_date_us.strftime("%d/%m/%Y")    # Convert date to UK format


        isbn = input("Enter isbn: ")    
        if self.db.view_status(isbn) != "issued":    
            books_borrowed = self.acc.l_books_borrowed
          
            if  books_borrowed != None:    
                
                if len(books_borrowed) < Student.b_limit: 
                    self.db.issue_book(isbn)
                    data = self.db.getBooks(isbn)
                    book = [data[1],    
                           c_date_uk]
                    self.acc.l_books_borrowed.append(book)    
                else:
                    print("You have reached your borrow limit")
            else:
              self.db.issue_book(isbn)
              data = self.db.getBooks(isbn)
              book = [data[1], c_date_uk]
              self.acc.l_books_borrowed.append(book)

        else:
            print("Book has already been issued")
        
    def f_opt4(self):
        '''
        ALLOWS USER TO RETURN THE BOOKS THEY HAVE BORROWED. METHOD CHECKS 
        WHETHER THE BOOK IS IN LIBRARY BEFORE PROCESSING RETURN, AS WELL AS 
        WHETHER THE RETURN WAS MADE WITHIN 7 DAYS OF BORROWING THE BOOK. IF 
        THE RETURN IS LATE THEN IT WILL BE CHARGED TO THE USER'S ACCOUNT.

        Returns
        -------
        None.

        '''
        print("option-4 - Return a Book")

        #c_date_us = datetime.now()    # Current date in US fromat
        #c = list(c_date_us.strftime("%d/%m/%Y"))    # Convert date to UK format
        c = "07/10/2023"
        d =None
        if c[0] == "0" and c[3] == "0":    # Removes 0 if its in front of figures
           
            d= c[:0]+c[1:3]+c[4:]
         
         
        elif c[0] == "0":
           
            d= c[:0]+c[1:]
        
         
        elif c[3] == "0":
           
            d = c[:3]+c[4:]
           
        else:
            d = c
       
        c_date_uk = "".join(d)
        print(c_date_uk)
        
        isbn = input("Enter isbn: ")    # Input isbn
       
        if self.db.view_status(isbn) == "issued": # Checks if books is issued
            self.db.return_book(isbn)
            data = self.db.getBooks(isbn)
            book = [data[1], c_date_uk]
            self.acc.l_return_books.append(book)
            date_format = "%d/%m/%Y"
            for i , b in enumerate(self.acc.l_books_borrowed):
                
                if b[0] == self.db.getBooks(isbn):
                    print(b)
                    borrow = b
                    d = b[1]
                    c = list(d)
                  
                    if c[0] == "0" and c[3] == "0":

                        a= c[:0]+c[1:3]+c[4:] 
                    
                    elif c[0] == "0":
                        
                        a= c[:0]+c[1:]
                    
                    elif c[3] == "0":
                        
                        a= c[:3]+c[4:]
                      
                    else:
                      a = d
                      
                    b_date="".join(a)
                    print(b_date)
                    print(c_date_uk)
                    a = datetime.strptime(c_date_uk, date_format)
                    b = datetime.strptime(b_date, date_format)
                    delta = a - b
                    print(delta)
                    
                    if delta.days >7:
                        
                        self.acc.l_lost_Books.append(book)
                        self.acc.l_books_borrowed.remove(book)
                        
                        if self.acc.acc_fine == None:
                        
                            self.acc.acc_fine = 20
                        
                        else:
                            self.acc.acc_fine = self.acc.acc_fine + 20
                        
                        self.acc.l_lost_Books.remove(book)
                        
                    else: 
                        self.acc.l_books_borrowed.remove(book)
                    
                else:
                    pass
 
          
        else:
            print("Book is in library")
           
                   
     
    def f_opt5(self):
        '''
        ALLOWS USER TO RESERVE A BOOK IF IT IS NOT AVAILABLE.

        Returns
        -------
        None.

        '''
        print("option-5 - Reserve a Book")
        c_date_us = datetime.now()
        c_date_uk = c_date_us.strftime("%d/%m/%Y")
        isbn = input("Enter isbn: ")
        
        if self.db.view_status(isbn) == "issued":
            data = self.db.getBooks(isbn)
            for i , b in enumerate(self.acc.l_books_borrowed):
                
                if b[0] != data[1]:
           
                    book = [data[1], c_date_uk]
                    self.acc.l_books_reserved.append(book)
                
                else:
                    
                    print("You are currently borrowing this book")
            
        else:
            
            print("Book is in library")
            
            
    def __repr__(self):
        return f"{self.f}\n {self.acc}"
    
from LibManSystem_class import LibManSystem