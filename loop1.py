"""

sum=0
print("How many Numbers You want to add?")
totalNum = int(input())

for i in range(1,totalNum+1):
    print("Enter a number")
    num = int(input())# 5
    sum = sum + num

print("Sum = ",sum)

#modify the above code , instead of 10 times fix we ask users that how many number they want to input?
"""


#take number from the user and print multiplication table of it.
"""
    output:
            enter a number
            5
            
            5 * 1 = 5 
            5 * 2 = 10 
            ..
            ..
            5 * 10 = 50  
 """

""" 
print("enter a number")
num = int(input())

for i in range(1,11):
    print(num," * ",i," = ",num*i)
"""


# take number from user and print all the odd numbers between 1 to n

"""
output:
    Enter a number
    15
    
    1 3 5 7 9 11 13 15
"""
print("Enter a number")
num  = int(input())

for i in range(1,num+1):
    if i  % 2 != 0:
        print(i)







