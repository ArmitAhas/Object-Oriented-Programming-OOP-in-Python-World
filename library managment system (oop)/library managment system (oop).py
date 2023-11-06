import datetime

class library :
    def __init__(self,name_book,name_author,code,publisher,genre):
        self.name = name_book
        self.author = name_author
        self.cods = code
        self.publisher = publisher
        self.genre = genre
        self.list = []
        self.issue = []


    def add_book(self) :
        name_book = input("Enter book's name : ")
        name_author =  input("Enter book's author : ")
        code =  input("Enter book's cods : ")
        publisher =  input("Enter book's publisher : ")
        genre =  input("Enter book's genre : ")
        self.list.append(name_book)
        self.list.append(name_author)
        self.list.append(code)
        self.list.append(publisher)
        self.list.append(genre)
        print(self.list)

   
    def issue_book(self) :
        stu_code = input("Enter membership code : ")
        book_n = input("Enter name of book  : ")
        book_c = input("Enter code of book : ")
        y = int(input("Enter year of delivery : "))
        m = int(input("Enter month of delivery : "))
        d = int(input("Enter day of delivery : "))
        book_t = datetime.date(y,m,d)
        self.issue.append(stu_code)
        self.issue.append(book_n)
        self.issue.append(book_c)
        self.issue.append(book_t)
        print(self.issue)


    def edit_book(self) :
        print(" 0 : edit name's book","\n"
              ," 1 : edit author's book ","\n"
              ," 2 : edit book's cods","\n"
              ," 3 : edit book's publisher ","\n"
              ," 4 : edit book's genre " )

        choice = input("Enter your number! : ")
        entry = input("Enter your text : ")
        if choice == "0" :
            self.list[0] = entry
        elif choice == "1":
            self.list[1] = entry
        elif choice == "2":
            self.list[2] = entry
        elif choice == "3":
            self.list[3] = entry
        elif choice == "4":
            self.list[4] = entry

        print(self.list)


    def return_book(self) :
        rebook = input("Enter name of book :  ")
        y = int(input("Enter year of delivery : "))
        m = int(input("Enter month of delivery : "))
        d = int(input("Enter day of delivery : "))
        booktime = datetime.date(y, m, d)
        if self.issue[1] == rebook :
            t1=self.issue[3]
            timecompare = t1 - booktime
            if timecompare != 0 :
                pay = timecompare
                print("your fine is ",pay,"and you must pay 1 Dollar per day")



    def search_book(self):
        x = input("Enter your book's name : ")
        exist = x in self.list
        if exist == True :
            print("This book exists !!")
        else :
            print("This book not exists")


  
    def show_book(self) :
        print("These are list of library's books")
        print(self.list)


# For example:
book1=library("Flowers","Kate Hills",2548,"Speech","Horror")
book1.add_book()
book1.issue_book()
book1.edit_book()
book1.return_book()
book1.search_book()
book1.show_book()















