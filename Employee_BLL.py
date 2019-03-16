# import py_compile
# py_compile.compile(r"d:/cms.py")
# Todo: add __doc__ in method and everywhere
# BLL

employeelist = [['dir', 10, 9541214954, 1, 'director', 50],
                ['man', 20, 9541214955, 2, 'manager', 'sonipat'],
                ['tra', 30, 9541214956, 3, 'trainer', 'python']]


class employee:
    temp_list = []

    def __init__(self):
        self.name = "d"
        self.age = 1
        self.mobile = 1
        self.id = 1

    def addemployee(self):
        temp_list = [self.name, self.age, self.mobile, self.id]
        employee.temp_list.extend(temp_list)

    @staticmethod
    def searchemployee(name):
        for e in employeelist:
            if e[0] == name:
                return e

    @staticmethod
    def delete(name):
        for e in range(len(employeelist)):
            if employeelist[e][0] == name:
                employeelist.pop(e)

    @staticmethod
    def display(found='NaN', display='all'):
        for e in employeelist:
            if display == 1:
                e = found
            print("\t \tName: {}, Age: {}, Mobile: {}, Id: {}".format(e[0].capitalize(), e[1], e[2], e[3]), end=" ")
            if e[4] == 'director':
                print(", Type: {}, Share: {}".format(e[4].capitalize(), e[5]))
            elif e[4] == 'manager':
                print(", Type: {}, Area: {}".format(e[4].capitalize(), e[5].capitalize()))
            elif e[4] == 'trainer':
                print(", Type: {}, Course: {}".format(e[4].capitalize(), e[5].capitalize()))

            if display == 1:
                return True


class director(employee):

    def __init__(self):
        self.type = "director"
        self.share = 0
        super(director, self).__init__()

    def add(self):
        temp_list = [self.type, self.share]
        employee.temp_list.extend(temp_list)
        employeelist.append(employee.temp_list)


class trainer(employee):

    def __init__(self):
        self.type = "trainer"
        self.course = 'NaN'
        super(trainer, self).__init__()

    def add(self):
        temp_list = [self.type, self.course]
        employee.temp_list.extend(temp_list)
        employeelist.append(employee.temp_list)


class manager(employee):

    def __init__(self):
        self.type = "manager"
        self.area = 'NaN'
        super(manager, self).__init__()

    def add(self):
        temp_list = [self.type, self.area]
        employee.temp_list.extend(temp_list)
        employeelist.append(employee.temp_list)


if __name__ == '__main__':
    while 1:
        choice = int(input('''
        1. For add new Member
        2. Search Particular Member
        3. For delete Member
        4. To modify Member
        5. To Display all Members
        6. Exit \n
        '''))

        if choice == 1:
            while 1:
                type = int(input('''
        1. For Director
        2. For Manager
        3. For Trainer \n
        '''))
                if type == 1 or type == 2 or type == 3:
                    break
                print("you didn't put correct choice")

            if type == 1:
                employeer = director()
            elif type == 2:
                employeer = manager()
            elif type == 3:
                employeer = trainer()

            employeer.name = input("\n\t \tEnter Name of {}: ".format(employeer.type.capitalize()))
            employeer.age = input("\t \tEnter Age: ")
            employeer.mobile = input("\t \tEnter Mobile: ")
            employeer.id = input("\t \tEnter Id: ")
            employee.addemployee(employeer)

            if type == 1:
                employeer.share = input("\t \tEnter Director's Share")
            elif type == 2:
                employeer.area = input("\t \tEnter Manager's Area")
            elif type == 3:
                employeer.course = input("\t \tEnter Trainer's Course")
            employeer.add()

            print('\t \tSuccessfully Added Record')

        if choice == 2:
            search = input("\t \tEnter Name of Member")
            found = employee.searchemployee(search)
            display = 1
            employee.display(found, display)

        if choice == 3:
            search = input("\t \tEnter Name of Member to be deleted")
            employee.delete(search)
            print('\t \tRecord Deleted')

        if choice == 4:
            search = input("\t \tEnter Name of Member")
            found = employee.searchemployee(search)
            found[0] = input("\t \tEnter Modified Name of {}".format(found[4].capitalize()))
            found[1] = input("\t \tEnter Modified Age")
            found[2] = input("\t \tEnter Modified Mobile")
            found[3] = input("\t \tEnter Modified Id")

            if found[4] == 'director':
                found[5] = input("\t \tEnter Director's Modified Share")
            elif found[4] == 'manager':
                found[5] = input("\t \tEnter Manager's Modified Area")
            elif found[4] == 'trainer':
                found[5] = input("\t \tEnter Trainer's Modified Course")

            print('\t \tSuccessfully Modified Record')

        if choice == 5:
            employee.display()

        if choice == 6:
            exit()
