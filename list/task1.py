list = []

print("Enter 5 numbers")
for i in range(1,6): #1 2 3 4 5
    num = int(input())
    list.append(num) # 10 20 30 40 50

print("Enter number for search :- ")
num = int(input())

counter = list.count(num) # 0

if counter == 0:
    print("Num not found in list")
else:
    list.remove(num)
    print("Num Removed => ",list)

