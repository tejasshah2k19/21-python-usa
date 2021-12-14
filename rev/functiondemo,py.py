"""
    functions are the collections of multiple instructions
    which executes line by line and give some output
    in python we use def keyword to create function
    function need to call then only it executes and give output
"""

#no return - no argument
def add():
    a = int(input("enter no1 "))
    b = int(input("enter no2"))
    c = a+b

    print("add = ",c)

#no return - with argument
def mul(a,b):
    c=a*b
    print("mul = ",c)

#with return-no argument
def div():
    a = int(input("enter no1"))
    b= int(input("enter no2"))
    c = a/b
    return c

#with arg-with return
def sub(a,b):
    return a-b;


#calling
# add()
# mul(10,10)
# x = div()
# print("div = ",x)

print("sub  =  ",sub(10,2))


#create one function with no arg no return - your function will perform
#square of a number , number is enterd by user

