import datetime

class student :
    def __init__(self,name_student,contact,email,gender,birthday):
        self.name = name_student
        self.contact = contact
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.student = []


    def add_student(self) :
        name_student = input("Enter student's name : ")
        contact =  input("Enter student's contact : ")
        email =  input("Enter student's email : ")
        gender =  input("Enter student's gender : ")
        print("student's birthday : ")
        y = int(input("Enter year of birthday : "))
        m = int(input("Enter month of birthday : "))
        d = int(input("Enter day of birthday : "))
        birthday = datetime.date(y, m, d)
        self.student.append(name_student)
        self.student.append(contact)
        self.student.append(email)
        self.student.append(gender)
        self.student.append(birthday)


    def edit_info_student(self) :
        print(" 0 : edit name of student","\n"
              ," 1 : edit student's contact ","\n"
              ," 2 : edit student's email","\n"
              ," 3 : edit student's gender ","\n"
              ," 4 : edit student's birthday " )

        choice = input("Enter your number! : ")
        if choice == "0" :
            entry = input("Enter your text : ")
            self.student[0] = entry
        elif choice == "1":
            entry = input("Enter your text : ")
            self.student[1] = entry
        elif choice == "2":
            entry = input("Enter your text : ")
            self.student[2] = entry
        elif choice == "3":
            entry = input("Enter your text : ")
            self.student[3] = entry
        elif choice == "4":
            print("student's birthday : ")
            y = int(input("Enter year of birthday : "))
            m = int(input("Enter month of birthday : "))
            d = int(input("Enter day of birthday : "))
            birth = datetime.date(y, m, d)
            self.student[4] = birth

        print(self.student)


    def search_student(self):
        x = input("Enter your student's name : ")
        exist = x in self.student
        if exist == True :
            print("This student exists !!")
        else :
            print("This student not exists")


    def show_student(self) :
        print("These are list of student's informations")
        print(self.student)


# For example :
student1= student("Alice",+19903457854,"Alice@gmail.com","Female",(1995,2,5))
student1.add_student()
student1.edit_info_student()
student1.search_student()
student1.show_student()














