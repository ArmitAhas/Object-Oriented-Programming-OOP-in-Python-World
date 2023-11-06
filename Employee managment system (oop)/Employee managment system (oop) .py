class employee :
    def __init__(self,id,name,email,phone_no,Address,Post,Salary):
        self.id = id
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.address = Address
        self.post = Post
        self.salary = Salary
        self.employee = []


    def add_employee(self) :
        id = input("Enter employee's id : ")
        name = input("Enter employee's name : ")
        email =  input("Enter employee's email : ")
        phone_no =  input("Enter employee's phone_no : ")
        address =  input("Enter employee's address : ")
        post = input("Enter employee's post : ")
        salary = input("Enter employee's salary : ")
        self.employee.append(id)
        self.employee.append(name)
        self.employee.append(email)
        self.employee.append(phone_no)
        self.employee.append(address)
        self.employee.append(post)
        self.employee.append(salary)
        print(self.employee)

   
    def update_employee(self) :
        print(" 0 : update employee's id","\n"
              ," 1 : update employee's name ","\n"
              ," 2 : update employee's email","\n"
              ," 3 : update employee's phone_n ","\n"
              ," 4 : update employee's address ","\n"
              ," 5 : update employee's post ","\n"
              ," 6 : update employee's salary")
        choice = input("Enter your number! : ")
        entry = input("Enter your information : ")
        if choice == "0" :
            self.employee[0] = entry
        elif choice == "1":
            self.employee[1] = entry
        elif choice == "2":
            self.employee[2] = entry
        elif choice == "3":
            self.employee[3] = entry
        elif choice == "4":
            self.employee[4] = entry
        elif choice == "5":
            self.employee[5] = entry
        elif choice == "6":
            self.employee[6] = entry

        print(self.employee)


    def search_employee(self):
        x = input("Enter your employee's id : ")
        exist = x in self.employee
        if exist == True :
            print("This id exists !!")
            print(self.employee)
        else :
            print("This employee not exists")

    
    def promote_employee(self) :
        id_search = input("Enter your employee's id : ")
        exist = id_search in self.employee
        if exist == True:
            extra = int(input("Amount of extra salary  : "))
            extra_salary = self.salary + extra
            print("this is additional salary of the employee : ",extra_salary)

        else:
            print("This employee not exists")




# For example:
emp1 = employee(125,"Jack","Jack@gmail.com",+18185642458,"No.23,Green Ave.",1245354,5200000)
emp1.add_employee()
emp1.update_employee()
emp1.search_employee()
emp1.promote_employee()












