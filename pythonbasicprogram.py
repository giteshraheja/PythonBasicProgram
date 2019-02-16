while 1:
    choice = int(input(
        ''' \n \n Enter the choice \n 1. for Fibonacci Series \n 2. Print Average of numbers by my method \n 3. for right angled triangle by my method
 4. Print backward triangle containing numbers instead of stars using my method \n 5. Print a Diamond by my method \n 6. Print stars using official method with official for
 7. Printing 5th Figure of Diamond by official method\n 8. Printing 5th Figure of Diamond by my Method \n Press Enter To finish with error \n '''))

    if choice == 1:
        count = 0
        while 1:
            n = input(" \n Enter the series of fibo ")
            if len(n) == 0:
                print("Empty String Enter Again")
            elif not n.isdigit():
                print("Enter Integer Numbers only upto desired integer like upto 50: ")
            else:
                n = int(n)
                n1 = 0
                n2 = 1
                next = 1
                print(n1, end=" ")
                print(n2, end=" ")
                while next <= n:
                    next = n1 + n2
                    if next > n - 1:
                        count += 1
                        break
                    print(next, end=" ")
                    n1 = n2
                    n2 = next
            if count > 0:
                break

    if choice == 2:
        count = 0
        while 1:
            no = input("Enter total number of digits:")
            if len(no) == 0:
                print("Empty String Enter Again")
            elif not no.isdigit():
                print("Enter Integer Numbers only upto desired integer like upto 50: ")
            else:
                no = int(no)
                i, avg = 0, 0
                for e in range(no):
                    while 1:
                        i = (input("Enter all values one by one and press enter after each entry"))
                        if not len(i) == 0:
                            if not i.isdigit():
                                print("Enter Integer Value")
                            else:
                                i = int(i)
                                avg = i + avg
                                count += 1
                                break
                        else:
                            print("Empty! Input again")

                print()  # printing line
                for e in range(30):
                    print('*', end='*')

                print(" \n avg of {} no. entered by user is {}".format(no, avg / no))  # printing average of 10 no.

                for e in range(30):  # printing line
                    print('*', end='*')
            if count > 0:
                break

    if choice == 3:
        count = 0
        while 1:
            n = (input(" \nEnter no. of floors "))
            if len(n) == 0:
                print("Empty value enter again")
            elif not n.isdigit():
                print("Enter Integer no.")
            else:
                n = int(n)
                for e in range(1, n + 1):
                    e = int(e)
                    print('@' * e)
                    count += 1
            if count > 1:
                break

    if choice == 4:
        count = 0
        while 1:
            zerone = (input("Enter no. greater than 5 or odd"))
            z = 0
            if len(zerone) == 0:
                print("Empty value enter again")
            elif not zerone.isdigit():
                print("Enter Integer no.")
            else:
                zerone = int(zerone)
                mid = zerone // 2 + 1
                for e in range(zerone, -3, -2):
                    print(' ' * z, '10' * mid + '1')
                    mid -= 1
                    z += 1
                    count += 1
            if count > 1:
                break

    if choice == 5:
        count = 0
        while 1:
            diamond = input("Enter size of diamond and use greater than 5 or odd no.")
            if len(diamond) == 0:
                print("Empty value enter again")
            elif not diamond.isdigit():
                print("Enter Integer no.")
            else:
                diamond = int(diamond)
                i = 1
                n2 = int(diamond // 2)
                for e in range(n2 + 1, 0, -1):
                    print(' ' * e, '*' * i, e * ' ')
                    i += 2
                i = diamond + 1
                for this in range(diamond):
                    print(' ' * (this + 1), '*' * i, this * ' ')
                    i -= 2
                    count += 1
            if count > 0:
                break

    if choice == 6:
        count = 0
        while 1:
            lines = input("Enter No. of Lines")
            if len(lines) == 0:
                print("Empty value enter again")
            elif not lines.isdigit():
                print("Enter Integer no.")
            else:
                lines = int(lines)
                for i in range(lines):  # Top to bottom stars Reverse Triangle
                    for e in range(lines - i):
                        print('*', end='')
                    print()
                    count += 1
                for i in range(lines):  # Top to bottom stars reverse Triangle Mirrored version
                    for e in range(i):
                        print(' ', end='')
                    for j in range(lines - i):
                        print('*', end='')
                    print()
                    count += 1
                for i in range(lines):  # Normal Triangle stars
                    for e in range(i + 1):
                        print('*', end='')
                    print()
                    count += 1
                for i in range(lines):  # Normal Star Triangle Mirrored Version
                    for e in range(lines - (i + 1)):
                        print(' ', end='')
                    for j in range(i + 1):
                        print('*', end='')
                    print()
                    count += 1
            if count >= 4:
                break

    if choice == 7:
        count = 0
        while 1:
            lines = input("Enter No. of Lines greater than 3 to make diamond")
            if len(lines) == 0:
                print("Empty value enter again")
            elif not lines.isdigit():
                print("Enter Integer no.")
            else:
                lines = int(lines)
                for i in range(lines):
                    for e in range(lines - i):
                        print('*', end='')
                    for j in range(i * 2):
                        print(' ', end='')
                    for k in range(lines - i):
                        print('*', end='')
                    print()
                for i in range(lines):
                    for e in range(i + 1):
                        print('*', end='')
                    for j in range((lines - (i + 1)) * 2):
                        print(' ', end='')
                    for k in range(i + 1):
                        print('*', end='')
                    print()
                    count += 1
            if count > 0:
                break

    if choice == 8:
        count = 0
        while 1:
            lines = input("Enter No. of Lines than 3 to make diamond")
            if len(lines) == 0:
                print("Empty value enter again")
            elif not lines.isdigit():
                print("Enter Integer no.")
            else:
                lines = int(lines)
                for i in range(lines):
                    print('*' * (lines - i), ' ' * i, ' ' * i, '*' * (lines - i), sep='')
                for i in range(lines):
                    print('*' * (i + 1), ' ' * (lines - (i + 1)), ' ' * (lines - (i + 1)), '*' * (i + 1), sep='')
                count += 1
            if count > 0:
                break

    if choice == 9:

        x, i = 5, 0
        n = 0
        for i in range(x):  # printing floor
            for j in range((x - 1), i, -1):
                print(' ', end='')
            for in_ in range((x - 1) - i, x + 1):
                if not (in_ + 1) % 2 == 0:
                    print(in_ + 1, end='')
                else:
                    print(' ', end='')
            for in_ in range((x - 1) - i, x):
                if (in_ + 1) % 2 == 0:
                    print(in_ + 1, end='')
                else:
                    print(' ', end='')
            print()

