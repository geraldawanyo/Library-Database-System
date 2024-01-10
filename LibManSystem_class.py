# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:30:24 2023

@author: User
"""
from Account_class import Account
from Library_database_class import LibDatabase

import json

class LibManSystem:
    
# Creates an instance of the database class
    db = LibDatabase()
    
# Loads the books from json file into database
    db.loadBooks()
    def __init__(self):
        
# Calls Registration or Log in Function
        LibManSystem.reg_or_login()
        
        
    
   
    # Checks if Login Details entered are correct
    @classmethod                                            
    def authenticate(cls,uid,pswd):
        '''
        

        Parameters
        ----------
        
        uid : ID NUMBER
        
        pswd : PASSWORD.

        Returns
        -------
        CHECKS IF THE ID AND PASSWORD
        THAT WAS INPUTTED BY THE USER MATCHES
        THE LOGIN DETIALS THAT ARE ON THE SYSTEM

        '''
        with open("accounts.json", "r") as fd:
            acc = json.load(fd)
        if uid in acc:
            if acc[uid]['password'] == pswd:
                return True, acc[uid]
        return False, None

    
    @classmethod       
    def login(cls):
        '''
        

        ALLOWS USER TO GET
        INTO LIBRARY SYSTEM 
        AND ACCESS ITS FEATURES BY 
        ENTERING ID NUMBER AND PASSWORD.

        Returns
        -------
        None.

        '''
        print("Welcome to BCU Lib System")
        uid = input("Enter uid: ")
        pswd = input("Enter your password: ")
        v, u = LibManSystem.authenticate(uid, pswd)
        print(u)
        if v:
            print("Welcome....")
            if u["u_type"] == "Staff":
                usr = Staff(LibManSystem.db,Account(u["id"],
                                    u["password"],
                                    u["f_name"],
                                    u["u_type"],
                                    u["l_books_borrowed"],
                                    u["l_books_reserved"],
                                    u["l_return_books"],
                                    u["l_lost_books"],
                                    u["acc_fine"]))
                    
              
                usr.menu()
            elif u["u_type"] == "Student":
                usr = Student(LibManSystem.db,Account(u["id"],
                                      u["password"],
                                      u["f_name"],
                                      u["u_type"],
                                      u["l_books_borrowed"],
                                      u["l_books_reserved"],
                                      u["l_return_books"],
                                      u["l_lost_books"],
                                      u["acc_fine"]))
                usr.menu()
            elif u["u_type"] == "Librarian":
                usr = Librarian(LibManSystem.db,Account(u["id"],
                                      u["password"],
                                      u["f_name"],
                                      u["u_type"],
                                      u["l_books_borrowed"],
                                      u["l_books_reserved"],
                                      u["l_return_books"],
                                      u["l_lost_books"],
                                      u["acc_fine"]))
                usr.menu()
            else:
                print("Data error")
            

        else:
            print("Login failure")
            LibManSystem.login()
            
    
    @classmethod
    def reg(cls):
        '''
        

        
        ALLOWS USER TO CREATE A NEW ACCOUNT AND INPUT ACCOUNT 
        DETAILS SUCH AS ID NUMBER, PASSWORD, FIRST NAME AND USER TYPE

        Returns
        -------
        None.

        '''
        u_id = input("Enter an id number: ")
        password = str(input("Enter a password: "))
        f_name = str(input("Enter your Name: "))
        u_type = str(input("Enter User Type: "))
        
       
        
        if u_type == "Student":
           usr = Student(LibManSystem.db, Account(u_id, password, f_name, u_type, 
                                                [], [], [], [], None))
           usr.menu()
         
        elif u_type == "Staff":
             usr = Staff(LibManSystem.db, Account(u_id, password, f_name, u_type, 
                                                  [], [], [], [], None))
             usr.menu()
        elif u_type == "Librarian":
             usr = Librarian(LibManSystem.db, Account(u_id, password, f_name, u_type, 
                                                  [], [], [], [], None))
             usr.menu()
        
    
    @classmethod
    def reg_or_login(cls):
        '''
        

        ALLOWS USER TO CHOOSE WHETHER THEY WANT TO REGISTER A NEW ACCOUNT OR
        LOG INTO EXISITING ACCOUNT.

        Returns
        -------
        None.

        '''
        opt = str(input("Register or Login: "))
        if opt == "Register":
            LibManSystem.reg()
            
        elif opt == "Login":
            LibManSystem.login()
        
        
    def logout(self):
        pass

    
from Student_class import Student
from Staff_class import Staff
from Librarian_class import Librarian



        

    

        

        
        

    