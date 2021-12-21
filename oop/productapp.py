class Product:
    #constructor
    def __init__(self):
        self.name = ""
        self.price=0
        self.quantity = 0
    #method
    def getData(self):
        print("Enter Product Name : ")
        self.name = input()
        print("Enter Price : ")
        self.price = int(input())
        print("Enter Quantity")
        self.quantity = int(input())

    def printData(self):
        print(self.name,"  ",self.price,"  ",self.quantity)


# list -> can store multiple data items
list = []
while True:
    print("1 For Add Product\n2 For List Products\n3 For Exit")
    choice = int(input())
    if choice == 1:
        p = Product()
        p.getData()
        list.append(p)  # p , p , p ,p
    elif choice == 2:
        for p in list:
            p.printData()
    elif choice == 3:
        exit(0)
