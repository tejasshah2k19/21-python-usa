"""

n = int(input("Enter a number"))

i=1

while i<= n:
    print(i)
    i=i+1
"""

"""  

#Take start and end nummber from the user and print all number which is divisible by 3 or 5

#start : 10
#end   : 30
#10 12 15 18 20 21 24 25 27 30


start = int(input("Enter start number"))
end = int(input("Enter end number"))

i=start
while i<=end:
    if i%3 == 0 or i%5 == 0:
        print(i,end=" ")

    i=i+1

"""


"""
# take number from the user and find out the sun of digits.
# 256 => 2+5+6 = 13
# 124 => 1+2+4 = 7
#794
num =int(input("Enter a number ")) # 927

sum = 0
max= 0
while num > 0 :# 124 12 1 0
    last  = num % 10 # 927=>7 92=> 2  => 9 
    if max < last:
        max = last#  9 
    sum = sum + last # 7+2+9
    num = num // 10  # 0

print("sum : ",sum)
print("max : ",max)
"""

# modify the above logic and find out the sum of  first and last digit
# 125 => 6
# 5263 => 8
# 6325 => 11

num = 12345
sum = num %10 # 5

while num >= 10:
    num = num // 10 #1

sum =sum + num
print(sum)


#124   4
#453   4
#827   8


