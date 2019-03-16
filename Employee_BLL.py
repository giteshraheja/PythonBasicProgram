import py_compile
py_compile.compile(r"d:/cms.py")
# Todo: add __doc__ in method and everywhere
# BLL

employeelist = []

class employee:

    def __init__(self, name, age, mobile, id, input):
        self.name = name
        self.age = age
        self.mobile = mobile
        self.id = id
        self.type = input

    def addemployee(self):
        employee.emplist.append(self)

    @staticmethod
    def searchemployee(id):
        for e in employeelist:
            if e[3] == id:
                return e

    @staticmethod
    def delete(id):
        a = employee.searchemployee(id)
        employeelist.pop(a)
        return a

class director(employee):

    def __init__(self, share):
        self.share = share


class trainer(employee):

    def __init__(self, course):
        self.course = course


if __name__ == '__main__':
    choice = int(input(
    '''))

    if choice == 1:
        director = director()
        
        director.name = input("Enter Name")
        director.age = input("Enter Age")
        director.mobile = input("Enter Mobile")
        director.id = input("Enter Id")
        director.type = "Director"

    if choice == 1:
        director = director()
        director.name = input("Enter Name")
        director.age = input("Enter Age")
        director.mobile = input("Enter Mobile")
        director.id = input("Enter Id")

    if choice == 1:
        director = director()
        director.name = input("Enter Name")
        director.age = input("Enter Age")
        director.mobile = input("Enter Mobile")
        director.id = input("Enter Id")
