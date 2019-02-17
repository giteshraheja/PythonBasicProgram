# Todo: add if __name__ == "__main__":
# BLL

# 1.add_function_performed


import random


class cms:

    def __init__(self):
        self.id = 0
        self.name = ''
        self.age = 0
        self.mobile = 0

    def getid(self, name):
        while 1:
            ran = int(random.random() * (10 ** 6))
            ran = str(ran)
            self.id = name[0:2] + ran
            if self.id in dic:
                print("id already enrolled, Choose another id ")
                break
            else:
                return self.id

    def getname(self):
        while 1:
            self.name = input("Enter Name to be added in record ")
            if len(self.name) == 0:
                print("Empty String Enter Any Value")
            elif not self.name.isdigit():
                return self.name.lower()
            else:
                print("Enter Name in correct format without integer value ")

    def getage(self):
        while 1:
            self.age = input("Enter Age between 10 to 90 to be added in record ")
            if self.age.isdigit():
                aget = int(self.age)
                if 9 < aget < 91:
                    return self.age
                else:
                    print("Age entered is Incorrect, choose between 10 to 90 ")
            else:
                print("Enter Age in Correct format or Integer Value ")

    def getmobile(self):
        while 1:
            self.mobile = input("Enter Mobile Number Of User ")
            if not self.mobile.isdigit():
                print("Enter Integer Value in Mobile ")
            else:
                if not len(self.mobile) == 10:
                    print("Enter ten Digit Mobile Number ")
                else:
                    return self.mobile

    # searchmobile

    def searchmobile(self):
        while 1:
            i = 0
            if len(dic) == 0:
                print("Dic is empty")
                i += 1
                return False
            self.mobile = input("Enter the mobile number to search ")
            if not self.mobile.isdigit():
                print("Enter integer values only ")
                i += 1
            if not len(self.mobile) == 10:
                print("Enter Ten digits only ")
                i += 1
            if i == 0:
                return self.mobile

    def displayusingdict(self):
        if self.mobile in dic:
            u = list(dic.get(self.mobile))
            print(" Id is {id} \n Name is {name} \n Age is {age} \n Mobile is {mobile}".format(id=u[0],
                                                                                               name=u[1].capitalize(),
                                                                                               age=u[2], mobile=u[3]))

    # 3.delete_performed_function

    @staticmethod
    def deleteusingmobile():
        while 1:
            if len(dic) == 0:
                print("Dic is Empty")
                return False
            m = input("Enter Mobile No. which will be used to delete record ")
            if not m.isdigit():
                print("Enter Integer Value only")
            else:
                if not len(m) == 10:
                    print("Enter ten digit mobile no.")
                else:
                    if m in dic:
                        dic.pop(m)
                        print("Element deleted")
                        break
            if len(dic) == 0:
                print("Dic is Empty")
                return False

    # 4.modify_performed_function

    # modifyusingmobile

    @staticmethod
    def um():
        while 1:
            u2 = input("Enter Modified Age")
            if u2.isdigit():
                if len(u2) == 2:
                    return u2
                else:
                    print("Enter Ten digits only")
            else:
                print("Enter Integer Values only")

    @staticmethod
    def uo():
        while 1:
            u3 = input("Enter Modified Mobile")
            if u3.isdigit():
                if len(u3) == 10:
                    return u3
            print("Enter Ten Digits only")

    @staticmethod
    def un():
        while 1:
            u1 = input("Enter Modified Name")
            if not u1.isdigit():
                return u1
            else:
                print("Enter Alphabets Only")

    def modifyusingmobie(self, dic=None):
        mobile = input("Enter Mobile number ")
        if not mobile.isdigit():
            print("Enter integer values only ")
        else:
            if not len(mobile) == 10:
                print("Enter ten digits only ")
            else:
                if mobile in dic:
                    self.name = cms.un()
                    self.age = cms.um()
                    self.mobile = cms.uo()
                    self.id = dic[mobile][0]
                    u = [self.id, self.name, self.age, self.mobile]
                    print(u, "Modified")
                    dic[mobile] = u
                    dic[self.mobile] = dic.pop(mobile)
                    print(dic)

    # 5.display_performed_function

    @staticmethod
    def displayalldata():
        if len(dic) == 0:
            print("Empty Dic")
        for k, n in dic.items():
            print('Id is {} , Name is {}, Age is {}, Mobile is {}'.format(n[0], n[1], n[2], n[3]))


# 6.exit_performed_function

# Exit


def exit():
    quit()


# PL
# Create PL

if __name__ == "__main__":

    dic = {'1234567890': ['id123456', 'idane', 35, 1234567890], '9541214954': ['id098765', 'idname', 26, 9541214954]}

    i = 0

    while 1:
        print("\n 1. Add Customer \n 2. Search \n 3. Delete \n 4. Modify \n 5. Display All \n 6. Exit \n")
        choice = input("Enter your Choice ")
        if choice == '1':
            obj = cms()
            obj.name = obj.getname()
            obj.id1 = obj.getid(obj.name)
            obj.age = obj.getage()
            obj.mobile = obj.getmobile()
            li = [obj.id1, obj.name, obj.age, obj.mobile]
            dic.update({obj.mobile: li})
            for e in range(30):
                print("*", end='*')
            print("\nRecord Added Successfully")
            for e in range(30):
                print("*", end='*')
        elif choice == '2':
            obj = cms()
            obj.mobile = obj.searchmobile()
            obj.displayusingdict()
            for e in range(30):
                print("*", end='*')
        elif choice == '3':
            cms.deleteusingmobile()
            for e in range(30):
                print("*", end='*')
        elif choice == '4':
            obj = cms()
            obj.modifyusingmobie(dic)
            for e in range(30):
                print("*", end='*')
        elif choice == '5':
            cms.displayalldata()
            for e in range(30):
                print("*", end='*')
        elif choice == '6':
            exit()

