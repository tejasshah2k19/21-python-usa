"""
str = input("Enter a string")

print(len(str))
print("str => ",str)
str = str.strip() # it will remove blank space from beg and end

print(len(str))
print("str => ",str)
"""


"""
str = input("Enter a string")

print(len(str))
print("str => ",str)
str = str.strip("$") # it will remove $  from beg and end

print(len(str))
print("str => ",str)

"""


"""
str ="$$$$royal$$$$"

print("str => ",str)
print(str.lstrip("$")) # it will remove $  from left
print(str.rstrip("$")) # it will remove $  from right
"""


#Task:
# i have string that has $ in the beginning , your task is to remove that extra $ from beg.
# do not use strip method
# str = "$$$$$$$royal$$$"
# expected str => royal$$$

"""
str ="$$$$$royal$$$"

newStr = ""
count=0
for c in str:
    if c == "$" and count == 0:
         pass
    else:
        newStr = newStr + c #royal$$$
        count = count + 1   #8
print(newStr)
"""


