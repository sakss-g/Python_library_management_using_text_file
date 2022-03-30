'''
this module is used for using the library management system
various functionality is provided which proceeds according to user input
'''

import dt
import borrow
import return_

# creating a funtion to use library management system
def main():
    while(True):
        print("             Welcome to Library Management System             ")
        print("")
        print("-----------------------------------------------------------------")
        print("")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")

        #checking for valid input
        try:
            a = int(input("Select an option from 1-4: "))
            print()
            if(a == 1): #for displaying the available books
                with open("stock.txt", "r") as file:
                    lines = file.read()
                    print(lines)
                    print()
            elif(a == 2): # for borrowing process
                borrow.borrow_book()
            elif(a == 3):  # for returning process
                return_.return_book()
            elif(a == 4):  # for exiting
                print("THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM")
                break
            else:
                print("PLEASE ENTER A VALID OPTION FROM 1-4")
        except ValueError as e:
            print(e)
            print("PLEASE INPUT AS SUGGESTED")
main()
