class Student:
    #default constructor
    def __init__(self):
        self.name = ""
        self.maths = 0
        self.sci = 0
        self.eng = 0
        self.perc = 0

    def getData(self):
        print("Enter name")
        self.name = input()
        print("Enter maths sci and english marks")
        self.maths = int(input())
        self.sci = int(input())
        self.eng = int(input())

    def calculateResult(self):
        self.perc =( self.maths + self.sci + self.eng )/3

    def printData(self):
        print("Name : ",self.name)
        print("Maths : ",self.maths)
        print("Sci : ",self.sci)
        print("Eng : ",self.eng)
        print("Perc : ",self.perc)

# create object

s = Student()
s.getData()
s.calculateResult()
s.printData()


