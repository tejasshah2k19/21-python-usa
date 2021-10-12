list = []


print("Enter 5 numbers")
for i in range(1,6): #1 2 3 4 5
    num = int(input())
    list.append(num) # 1 2 30 200 300

for num in list:
    if num%3 == 0 or  num%5 ==0:
        print(num)



