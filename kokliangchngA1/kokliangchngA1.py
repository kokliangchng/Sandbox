"""
Name:Ch'ng Kok Liang
Date:6/1/2017
Description:This program is a simple reading list that allows a user to track books they wish to read and books they have completed reading. The program maintains a list of books in a file, and each book has:
GitHub link:
"""
import time, sys, csv


usernames_input = ['']
user_input = ['']
bookdata = []
bookori = []
valid_menu=['R','r','C','c','A','a','M','m''Q','q']

def booklist():
    del bookdata[:]
    del bookori[:]
    con = 0
    with open('book.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rowX = row[:]
            rowX += str(con)
            bookdata.append(rowX)
            bookori.append (row)
            con += 1
    csvfile.close()
    return



print("Reading List 1.0 -  by chngkokliang")
booklist()
print ("%s books loaded from books.csv"%len(bookdata))
print("Menu:")
print (" R - List required books\n C-List completed books\n A-Add new book\n M-Mark a book as completed\n Q-Quit")
print(">>>")

while not (user_input =='R' or user_input =='r' or user_input=='C' or user_input=='c'or user_input=='A' or user_input=='a' or user_input=='M' or user_input=='m' or user_input =='Q' or user_input=='q' ):
    user_input = str(input()) # Read input value
    while user_input not in valid_menu:
        print("Invalid menu choice")
        break
    #if(user_input =='R' or user_input =='C' or user_input=='A' or user_input=='M'or user_input =='Q' ):
        # break
        #print("TEST")

    #RequiredBook
    if (user_input =='R' or user_input=='r'):
        print ("Required books: ")
        RequiredBook = []
        count = 0
        for row in bookdata :
            if (row[3] == 'r'):
                print("%s. %s   by %s   %s pages" % (row[4], row[0], row[1], row[2]))
                count = count + int(row[2])
                RequiredBook.append(row)
        print("Total pages for %s books: %s"%(len(RequiredBook), count))

    #CompletedBook
    elif (user_input =='C'or user_input=='c'):
        print("Completed books: ")
        CompletedBook = []
        count = 0
        for row in bookdata:
            if (row[3] == 'c'):
                print("%s. %s   by %s   %s pages" % (row[4], row[0], row[1], row[2]))
                count = count + int(row[2])
                CompletedBook.append(row)
        print("Total pages for %s books: %s" % (len(CompletedBook), count))

    #AddBook
    elif(user_input =='A' or user_input=='a'):
        input_title = ""
        input_author = ""
        input_num = -1
        print("Menu:")
        while(input_title == ""):
            input_title=str(input("Title: "))
            if (input_title == "") :
                print("Input can not be blank")
        while(input_author == ""):
            input_author=str(input("Author: "))
            if (input_author == ""):
                print("Input can not be blank")
        while(input_num < 0):
            input_num=int(input("Pages: "))
            numb = int(input_num)
            if (int(input_num) < 0):
                print("Number must be >= 0")
        data = []
        data = [input_title, input_author, input_num, 'r']
        print(data)
        # open("book.csv", "a", newline='\n', encoding="utf-8") as output_file:
        #     writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        #     writer.writerow([])
        #     writer.writerow(data)
        output_file=open("book.csv", "a")
        output_file.write("{},{},{},r\n".format(input_title,input_author,input_num))

        output_file.close()

    elif(user_input =='M' or user_input=='m'):
        print("Required books: ")
        RequiredBook = []
        count = 0
        no_book = True
        for row in bookdata:
            if (row[3] == 'r'):
                print("%s. %s   by %s   %s pages" % (row[4], row[0], row[1], row[2]))
                count = count + int(row[2])
                RequiredBook.append(row)
                no_book = False
        if (no_book):
            print("No Books")
        else:
            while True:
                try:
                    book = int(input("Enter the number of a book to mark as completed: "))
                    break
                except:
                    print("Invalid input; enter a valid number")
                    continue


            if (int(book)+1 > len(bookdata)):
                print("your input not in the list")
                # add condition if input not in digit
            else:
                for row in bookdata:
                    if (row[3] == 'r'):
                        if (int(row[4]) == int(book)):
                            bookori[int(book)][3] = 'c'
                            #print(bookori)
                            with open('book.csv', 'w') as modified:
                                writer = csv.writer(modified, delimiter=',', lineterminator='\n')
                                writer.writerows(bookori)
                print(str(bookori[int(book)][0]) + " book already marked as completed")

    #Exits
    else:
         if (user_input =='Q' or user_input=='q'):
            print ("%s books saved from books.csv"%len(bookdata))
            print ("Have a nice day :)")
            sys.exit()

    # else : print ("Invalit Operation")
    # print ("\nThank You .... Bye")

    user_input = ""
    booklist()
    print("Menu:")
    print (" R - List required books\n C-List completed books\n A-Add new book\n M-Mark a book as completed\n Q-Quit")
    print(">>>")