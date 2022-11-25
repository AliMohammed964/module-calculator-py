class employee():
    name = ''
    age = 0
    dept = ' '
    phone = 0

    def enterdata(self):
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.dept = input("Enter your department : ")
        self.phone = input("Enter your phone : ")

    def show(self):
        print('name : ' + self.name + ' // age : ' + " " + str(
            self.age) + '//Department : ' + self.dept + '//Phone : ' + str(self.phone))

    def compare(self, age):
        if 18 < self.age < 30:
            result = 'young'
        elif self.age > 30:
            result = 'old'
        elif self.age < 18:
            result = 'illegal age'

        return result


e1 = employee()
e1.enterdata()
e1.show()
print(e1.compare(e1.age))
