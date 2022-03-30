'''
this module is used for borrowing books, where the availability of book is checked
if the book is available the user can borrow the book
again the user is asked if they want to borrow more books
if they want to borrow they proceed with the borrowing process
a txt file is generated with the name of the borrower and details of the books borrowed
'''

import dt

#creating a function for borrowing books
def borrow_book():

    success = False
    while (True):
        firstName = input("ENTER THE FIRST NAME OF THE BORROWER: ")
        if firstName.isalpha(): #checking for alphabets
            break
        print("PLEASE INPUT LETTERS FROM A-Z")

    while (True):
        lastName = input("ENTER THE LAST NAME OF THE BORROWER: ")
        if lastName.isalpha():  #checking for alphabets
            break
        print("PLEASE INPUT LETTERS FROM A-Z")

    #creating a txt file to store the details of the borrower and the books borrowed
    borrow = "Borrow- " + firstName + ".txt"
    with open(borrow, "w+") as file:
        file.write("                  Library Management System\n")
        file.write("Borrowed by:\t" + "First Name: " + firstName + "     " + "Last Name: " + lastName + "\n")
        file.write("Borrowed on:\t" + "Date: " + dt.get_date() + "     " + "Time: " + dt.get_time() + "\n")
        file.write("S.N\t\t    Name of Book\t\t      Author" + "\n")

    #creating an empty 2d list to read and store data from stock.txt file
    data = []
    with open('Stock.txt', 'r') as file:
        for line in file:
            data.append(line.replace('\n', '').split(','))
    

    #creating loop for borrowing books
    while success == False:
        print("")
        print("PLEASE SELECT AN OPTION BELOW")
        for i in range(len(data)):
            print("Enter", i, "to borrow book", data[i][0])

        #checking for ivalid input using try, except
        try:
            a = int(input())
            try:
                if(int(data[a][2]) > 0):  #checking for availability of book
                    print("BOOK IS AVAILABLE FOR BORROWING")
                    with open(borrow, "a") as file:  # writing the details of the books in the borrower's txt file
                        file.write("1. \t\t     " + str(data[a][0]) + "\t\t     " + str(data[a][1]))
                        file.write("\n")

                    #updating the stock.txt file with new data
                    data[a][2] = (int(data[a][2]) - 1)
                    with open("Stock.txt", "w+") as file:
                        file.write("HarryPotter,Jk Rowling," + str(data[0][2]) + ",2")
                        file.write("\n")
                        file.write("The Silent Patient,Alex Michaelides," + str(data[1][2]) + ",1.5")
                        file.write("\n")
                        file.write("Programming with Python,John Smith," + str(data[2][2]) + ",3")
                        file.write("\n")
                        file.write("Pride and Prejudice,Jane Austen," + str(data[3][2]) + ",3")
                        file.write("\n")
                        file.write("Introduction to Java, Y. Daniel Lianf," + str(data[4][2]) + ",3")

                    #for multiple borrowing of the books
                    loop = True
                    count = 1
                    while loop == True:
                        choice =str(input("DO YOU WANT TO BORROW MORE BOOKS?(Y/N)(SAME BOOK CAN NOT BE BORROWED)"))
                        if (choice.upper() == "Y"):
                            count = count + 1
                            print("")
                            print("PLEASE SELECT A OPTION BELOW")
                            for i in range(len(data)):
                                print("Enter", i, "to borrow book", data[i][0])
                            a = int(input())
                                
                            if(int(data[a][2]) > 0):  #checking for availability of book
                                print("BOOK IS AVAILABLE FOR BORROWING")
                                with open(borrow, "a") as file:  # writing the details of the books in the borrower's txt file
                                    file.write(str(count) + ". \t\t" + str(data[a][0]) + "\t\t     " + str(data[a][1]))
                                    file.write("\n")

                                #updating the stock.txt file with new data
                                data[a][2] = (int(data[a][2]) - 1)
                                with open("Stock.txt", "w+") as file:
                                    file.write("HarryPotter,Jk Rowling," + str(data[0][2]) +",2")
                                    file.write("\n")
                                    file.write("The Silent Patient,Alex Michaelides," + str(data[1][2]) + ",1.5")
                                    file.write("\n")
                                    file.write("Programming with Python,John Smith," + str(data[2][2]) + ",3")
                                    file.write("\n")
                                    file.write("Pride and Prejudice,Jane Austen," + str(data[3][2]) + ",3")
                                    file.write("\n")
                                    file.write("Introduction to Java,Y. Daniel Lianf," + str(data[4][2]) + ",3")
                                    success = False
                                        
                            else:
                                loop = False
                                break;
          
                        elif(choice.upper() == "N"):
                            print("")
                            print("THANK YOU FOR BORROWING FROM US")
                            print("")
                            loop = False
                            success = True
                                    
                        else:
                            print("PLEASE CHOOSE AS SUGGESTED")
                            
                else:
                    print("BOOK IS NOT AVAILABLE FOR BORROWING")
                    borrow_book()
                    success = False
            #message when there is an invalid input
            except IndexError:
                print("")
                print("PLEASE SELECT BOOK ACCORDING TO THEIR NUMBER")
                        
        except ValueError:
            print("")
            print("PLEASE CHOOSE AS SUGGESTED")
    
                                            
    

                                  
