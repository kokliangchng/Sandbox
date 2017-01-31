"""
Name:Chng Kok Liang
Date:31/1/2017
Brief Project Description:This project is use kivy to create a layout for user easily to test it . And this prokect is for user to store the book data.
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
#from booklist import BookList
from kivy.uix.button import Button
import csv
bookdata = []
bookori = []
book=[]

# Create your main program in this file, using the ReadingListApp class

class ReadingListApp(App):
    def on_start(self):
        count=0
        print("on_start is called")
        myfile=open("books.csv","r")
        for each in myfile:
            data = each.split(",")
            temp_button = Button(text=data[0])
            temp_button.bind(on_release=self.press)
            self.root.ids.entriesBox.add_widget(temp_button)
            self.root.ids.output_message.text="Total pages of".format(count)


    def build(self):
        self.title="Reading list 2.0"
        self.root=Builder.load_file("app.kv")
        return self.root

    def press(self,instance):
        name=instance.text
        self.root.ids.output_message.text=name

    def completed_list(self):
        myfile=open("books.csv","r")
        for each in myfile:
            data = each.split(",")
            temp_button = Button(text=data[0])
            temp_button.bind(on_release=self.press)
            self.root.ids.entriesBox.add_widget(temp_button)
            self.root.ids.entriesBox.clear_widgets()

    def add_list(self):
        title=self.root.ids.input_title.text
        author=self.root.ids.input_author.text
        pages=self.root.ids.input_pages.text
        myfile=open("books.csv",'a')
        myfile.write("{},{},{},r\n".format(title,author,pages))
        myfile.close()

    def required_list(self):
        self.root.ids.entriesBox.clear_widgets()
        myfile = open("books.csv", "r")
        for each in myfile:
            data = each.split(",")
            temp_button = Button(text=data[0])
            temp_button.bind(on_release=self.press)
            self.root.ids.entriesBox.add_widget(temp_button)

    def marks_list(self):
        self.root.ids.entriesBox.clear_widgets()
        self.root.ids.output_message.text="marks books"
        myfile = open("books.csv", "r")
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
                    for each in myfile:
                        data = each.split(",")
                        temp_button = Button(text=data[0])
                        temp_button.bind(on_release=self.press)
                        self.root.ids.entriesBox.add_widget(temp_button)
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
                        if (int(row[3]) == int(book)):
                            bookori[int(book)][3] = 'c'






    def handle_clear(self):
        self.root.ids.input_title.text=""
        self.root.ids.input_author.text=""
        self.root.ids.input_pages.text=""
        self.root.ids.output_message.text=""

    def press_entry(self,input_title,input_author,input_pages):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        # name = instance.text
        self.status_text = "{}{}{}".format(input_title,input_author,input_pages)
        # set button state
        # print(instance.state)
        # instance.state = 'down'

        # pass

ReadingListApp().run()
