list1 = []
list2 = []
list3 = []

print("Enter 3 numbers")
for i in range(1,4): #1 2 3 4 5
    num = int(input())
    list1.append(num) # 10 20 30

print("Enter 4 numbers")
for i in range(1, 5):  # 1 2 3 4 5
    num = int(input())
    list2.append(num)  # 100 200 300 400

list3 = list1 + list2 # merge two list into 3rd list
print(list1)
print(list2)
print(list3)