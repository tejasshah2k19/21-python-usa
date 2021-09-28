# def for find out the max number from two
#no return and no argument
def maxNumber():
    print("Enter Two numbers")
    a = int(input())
    b = int(input())
    if a > b:
        print(a," is max")
        oddEvenNumber(a)
    else:
        print(b," is max")
        oddEvenNumber(b)


#no return , with argument
def oddEvenNumber(num):
    if  num%2 == 0:
        print(num," is even")
    else:
        print(num," is odd")


maxNumber()
# oddEvenNumber(25)
# oddEvenNumber(26)
