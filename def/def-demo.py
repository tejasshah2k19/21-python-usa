def add():
    a = int(input("Enter no1"))
    b = int(input("Enter no2"))
    print("Add = ",(a + b))


def sub():
    a = int(input("Enter no1"))
    b = int(input("Enter no2"))
    print("Sub =>",(a - b))

def mul():
    a = int(input("Enter no1"))
    b = int(input("Enter no2"))
    print("Mul = ",(a * b))

while True:
    print("Press 1  Add \nPress 2 Sub\nPress 3 Mul\n4 For Exit\nEnter your choice:")
    choice = int(input())

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        print("Thank you....")
        exit(0)
    else:
        print("Invalid Choice....")


