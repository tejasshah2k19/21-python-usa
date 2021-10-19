names = ("shyam","ram","sita","gita","ravan")

search = input("Enter name that you want to search")


if search in names:
    print(search," found in tuple")
else:
    print(search," not found in tuple")