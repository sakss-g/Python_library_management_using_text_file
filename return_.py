'''
this module is used for returning books, where whether the borrower exists or not is checked
it also asks if the borrower is late to return
if late a fine is charged by the number of days the borrower is late
a txt file is generated with the name of the returner and details of the books returned
'''

import dt

# creating a function for returning books
def return_book():
    name = input("ENTER THE FIRST NAME OF THE BORROWER: ")
    a = "Borrow- " + name + ".txt"

    #creating an empty 2d list to read and append data from stock.txt file
    data = []
    with open('Stock.txt', 'r') as file: 
        for line in file:
            data.append(line.replace('\n', '').split(','))
    total_cost = 0.0

    # checking if the borrower exists or not
    try:
        with open(a, "r") as file:
            lines = file.readlines()

        with open(a, "r") as file:
            re = file.read()
            print(re)
    except:
        print("THE BORROWER NAME IS INCORRECT")
        return_book()

    #creating a txt file for the borrower who is returning the books
    returnb = "Return- " + name + ".txt"
    with open(returnb, "w+") as file:
        file.write("                  Library Management System\n")
        file.write("Returned by:\t" + name + "\n")
        file.write( "Date: " + dt.get_date() + "     " + "Time: " + dt.get_time() + "\n")
        file.write("S.N\t\t     Name of Book\t\t      Cost\n")

    #calculating the total cost for borrowing books
    for i in range(len(data)):
        if data[i][0] in re:
            with open(returnb, "a") as file:
                file.write(str(i+1)+ "\t\t     " + str(data[i][0]) + "\t\t\t $" + str(data[i][3]) + "\n")
                data[i][2] = (int(data[i][2])+ 1)
            total_cost += float(data[i][3])

    #checking if the borrower is late to return the books
    print("")
    print("\t\t\t\t\t\t\t" + "$" + str(total_cost))
    print("")
    print("IS THE RETURN DATE FOR BOOK EXPIRED?(Y for yes / N for no)")
    check = input()

    if (check.upper() == "Y"):
        print("BY HOW MANY DAYS WAS THE BOOK RETURNED LATE")
        day = int(input())
        fine = 2 * day
        with open(returnb, "a") as file:
            file.write("\t\t\t\t\t\t  Fine: $ " +str(fine) + "\n")

        total_cost = total_cost + fine

    print("Final Total: " + "$" + str(total_cost))
    with open(returnb, "a") as file:
        file.write("\t\t\t\t\t\t Total: $ " + str(total_cost))

    #updating the stock.txt file after the borrower has returned the books
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
        file.write("\n")
            
