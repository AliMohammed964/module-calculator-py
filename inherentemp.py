class Employee:
    def __init__(self, firstname, age, dept,phone):
        self.firstname = firstname
        self.age = age
        self.dept = dept
        self.phone = phone

class manager(Employee):
    def __init__(self, firstname, age, dept,phone, salary, title, field):
        self.salary = salary
        self.title = title
        self.field = field
        super().__init__(firstname,  age,  dept, phone)

    def showcv(self):

        print('name is : {} and age is : {} and dept is : {} and phone is : {}'.format(self.firstname, self.age, self.dept, self.dept))
        print('salary is : {} and title is : {} and field is : {}'.format(self.salary, self.title, self.field))


e1 = manager('ali',20,'Network','07722772',1000,'senior','marketing')
e1.showcv()