x = (1,22,33,44,55,66,66,77)

print(x)

#how to find out size of tuple?
print(len(x))

#access tuple using index
print(x[0])

#negative indexing
print(x[-1])

#slicing
print(x[2:5]) # 2 3 4 index will print

# now we can not add / remove / modify data items - because tuple is a read only data type

#can we have in ? and not in ?
if 23 in x:
    print("23 is present")
else:
    print("23 is not present")

# read all the items from - one by one
# extract data items from tuple

t = (11,22,33,44,55)

for data in t:
    print(data)

# functions in tuple ?
#count -> it will count how many times a given data item is present in tuple

t = (2,3,4,5,6,6,7)
print(t.count(6)) # 2
print(t.count(7)) # 1
print(t.count(10)) # 0

#index -> search a data item in tuple and return the index of data item

t = ("ram","shyam","gita","ravan","gita")
print(t.index("gita")) # 2






