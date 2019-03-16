class cms:
    is_max_3object = 0
    is_enter_Class = 0

    def __init__(self):
        self.__class__.is_max_3object += 1
        self.name = " "
        self.age = 5

    def __new__(cls, *args, **kwargs):
        if cls.is_max_3object == 3:
            if cms.is_enter_Class == 0:
                cms.is_enter_Class += 1
                cms.is_max_3object += 1
            print("Max Created 3 objects either delete or append any other")
            return
        return super().__new__(cls)


# noinspection SpellCheckingInspection
def displayall():
    for e in li:
        print("Customer details are: ", e[0], e[1], )


# noinspection SpellCheckingInspection
def adddata(obj):
    lis = [obj.name, obj.age]
    li.append(lis)


def search(getitem):
    for e in li:
        if e[0] == getitem:
            return e
    print("Not Found")


# noinspection SpellCheckingInspection
def modify(gotitem):
    gotitem[0] = input("Enter New Name")
    gotitem[1] = input("Enter New Age")
    print("Successfuly Edited")


# noinspection SpellCheckingInspection
def deleteitem(gotitem):
    li.remove(gotitem)
    print("SuccessFuly Deleted")
    cms.is_max_3object -= 1
    cms.is_enter_Class = 0


li = []

if __name__ == "__main__":
    while 1:
        choice = int(input('''
        Press 1  for Add Customer
        Press 2  for Show
        Press 3  for Search
        Press 4  for Edit
        Press 5  for Delete
        Press 6  for exit
        ENTER your Correct Choice, no Exception Handled, wrong entry will exit program HERE:\t'''))

        if choice == 1:
            obj = cms()
            if cms.is_max_3object <= 3:
                obj.name = input("Enter the name for customer")
                obj.age = input("Enter the age for customer")
                adddata(obj)

            else: continue

        elif choice == 2:
            displayall()
            print()

        elif choice == 3:
            item = input("Enter item by using name")
            name = search(item)
            print("Details are: ", name[0], name[1])

        elif choice == 4:
            item = input("Enter item by using name")
            obj = search(item)
            modify(obj)

        elif choice == 5:
            item = input("Enter item by using name")
            obj = search(item)
            deleteitem(obj)

        elif choice == 6:
            break
