# Multi level

# Class1

class person:
    def __init__(self, age, salary):
        self.age = age
        self.salary = salary

    def Person_age(self):
        print(f"This person is 45 years old: {self.age}")

    def Person_salary(self):
        print(f"he is making good amount of salary: {self.salary}")

# class2

class Employee(person):
    def __init__(self,age, salary, name, jobtitle):
        super().__init__(age, salary)
        self.name = name
        self.jobtitle = jobtitle

    def Employee_name(self):
        print(f"employer name is :{self.name}")

    def Employee_jobtitle(self):
        print(f"Employer's salary is 1 lakh :{self.salary}")
# class3

class developer(Employee):
    def __init__(self,age, salary,name, jobtitle, company, module):
        super().__init__(age, salary,name, jobtitle)
        self.company = company
        self.module = module

    def Developer_company(self):
        print(f"the name of the company is : {self.company}")

    def developer_module(self):
        print(f"the module is on payment system:{self.module}")


obj1 = developer("32", "10000","vrushti","QA","Cognizant","Payment")
obj1.Developer_company()
obj1.Person_age()
obj1.Employee_name()

obj2 = developer("40", "100000","padma","Developer","Apex","Billing")
obj2.Developer_company()
obj2.Person_age()
obj2.Employee_name()
