# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:29:58 2023

@author: User
"""

from datetime import datetime
import json

class Account:
    def __init__(self,a_id, password, f_name, u_type, l_books_borrowed=[],l_books_reserved=[],
                 l_return_books=[],l_lost_Books = [], acc_fine=None):
        self.a_id=a_id
        self.password = password
        self.f_name = f_name
        self.u_type = u_type
        self.l_books_borrowed=l_books_borrowed
        self.l_books_reserved=l_books_reserved
        self.l_return_books = l_return_books
        self.l_lost_Books = l_lost_Books
        self.acc_fine = acc_fine
        
        
 
    
    @classmethod
    def load_account(cls, a_id):
        '''

        Parameters
        ----------
        
        a_id : ACCOUNT ID.

        Returns
        -------
        RETURNS ACCOUNT DETAILS

        '''
        with open("accounts.json") as fd:
            acc = json.load(fd)
            return Account(acc[a_id]["id"],
                           acc[a_id]["password"], 
                           acc[a_id]["f_name"],
                           acc[a_id]["u_type"].
                           acc[a_id]["l_books_borrowed"], 
                           acc[a_id]["l_books_reserved"],
                           acc[a_id]["l_return_books"],
                           acc[a_id]['l_lost_books'],
                           acc[a_id]["acc_fine"]
                            )
    
    
    def printBorrowedBooks(self):
        '''
        PRINTS USER'S BORROWED BOOKS AND BORROW DATE'

        Returns
        -------
        None.

        '''
        print('\nBorrowed Books:\n','-'*20)
        for i , b in enumerate(self.l_books_borrowed):
            #if i == 1: 
            # print(f"{i}:  {LibaryData.d_books.get(b,'Unkown')}")
            print(b)
            print('-'*20)
            
    def printReturnedBooks(self):
        '''
        PRINTS USER'S RETURNED BOOKS AND THE DATE OF RETURN'

        Returns
        -------
        None.

        '''
        print('\nReturned Books:\n','-'*20)
        for i , b in enumerate(self.l_return_books):
            #if i == 1: 
            # print(f"{i}:  {LibaryData.d_books.get(b,'Unkown')}")
            print(b)
            print('-'*20)
            
    def printReservedBooks(self):
        '''
        PRINTS USER'S RESERVED BOOKS AND THE DATE THEY WERE RESERVED'

        Returns
        -------
        None.

        '''
        print('\nReserved Books:\n','-'*20)
        for i , b in enumerate(self.l_books_reserved):
            #if i == 1: 
            # print(f"{i}:  {LibaryData.d_books.get(b,'Unkown')}")
            print(b)
            print('-'*20)
            
    def printLostBooks(self):
        '''
        PRINTS THE BOOKS THAT THE USER HAS LOST

        Returns
        -------
        None.

        '''
        print('\nLost Books:\n','-'*20)
        for i , b in enumerate(self.l_lost_Books):
             
            print(b)
            print('-'*20)
             
    def printAccFine(self):
        '''
        PRINTS THE USER'S TOTAL FINE FOR LOST AND OVERDUE BOOKS'

        Returns
        -------
        None.

        '''
        print('\nAccount Fine:\n','-'*20)
         
        f"£{self.acc_fine}"
         
        print('-'*20)
        
    def cal_fine(self, b_date):
        '''
        

        Parameters
        ----------
        b_date : BORROW DATE

        Returns
        -------
        CHECKS WHETHER A USER HAS EXCEEDED BORROW TIME FOR A PARTICULAR BOOK.
        IF THE USER HAS BORROW THE BOOK FOR MORE THAN 7 DAYS THEN IT WILL BE 
        CHARGED TO THE USER'S ACCOUNT. IF NOT, THE METHOD WILL OUTPUT THE DAYS
        THE DAYS LEFT TO RETURN.

        '''
        date_format = "%m/%d/%Y"
        for i , b in enumerate(self.l_books_borrowed):
            
            c_date = b[1]
            a = datetime.strptime(c_date, date_format)
            b = datetime.strptime(b_date, date_format)
        delta = b - a
        if delta.days > 7:
            
            if self.acc_fine == None:
                self.acc_fine = 20
            else:
                self.acc_fine = self.acc_fine + 20
                
        else:
            f"Member has {7 - delta.days} days left"
    
    def check_b_time(self):
        '''
        OUTPUTS THE BOOKS THAT HAVE BEEN BORROWED BETWEEN TWO PARTICULAR DATES

        Returns
        -------
        None.

        '''
        opt = input("Check books borrowed between two particular times? (Yes or No): ")
        
        if opt == "Yes":

            l_date = input("check books borrowed from date: ")
            
            h_date = input("To date: ")
            date_format = "%d/%m/%Y"
            print('\nBooks borrowed between',l_date,'and',h_date,'\n','-'*20)
            
            for i , b in enumerate(self.l_books_borrowed):
                
                
                c = list(b[1])
                
                if c[0] == "0" and c[3] == "0":

                    a= c[:0]+c[1:3]+c[4:] 
              
                elif c[0] == "0":
                    a= c[:0]+c[1:]
              
                elif c[3] == "0":
                    a= c[:3]+c[4:]
                
                else:
                    a = c
                    print(c)
                    c_date="".join(a)
                    a = datetime.strptime(l_date, date_format)
                    b = datetime.strptime(c_date, date_format) # Date to be checked
                    c = datetime.strptime(h_date, date_format)
                    d = datetime.strptime(l_date, date_format)  #Date entered here should always be the same as 'a'

                    delta1 = b - a
                    delta2 = c - b
                    delta3 = d - a
            
                    if delta1.days >= delta3.days and delta2.days >= delta3.days:
                        print(borrow)
                        print('-'*20)
                    
                    else:
                        print('No books were borrowed between',l_date,'and',h_date)
                        
        else:
            pass
             
               
    
        
        
        
        
    def __repr__(self):
        
            
        return f"""{'*'*20}
id: {self.a_id}
books_borrowed: {self.l_books_borrowed}
    """
#         return None

    
