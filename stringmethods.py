"""
str = "Royal Education"

print(str.lower())

str.upper()
print(str) #Royal Education

print("Enter a string")
str = input() #jony jony yes papa
print("Enter a sub string")
substr = input() # papa


if substr in str:
    print(str," contains ",substr)
else:
    print("SubString not Found")


str = "Jony Jony Yes PaPa"
str = str.replace("J","T")
print(str)


str = "Jony Jony Yes PaPa"
str = str.replace("Jony","Montu")
print(str)

"""

str = "jan,feb,march,apr"

data = str.split(",")

#print(data)

for months in data:
    print(months)

str = "jony jony yes papa"
word = "jony"





