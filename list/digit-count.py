list = []

counter1 = 0
counter2 = 0
counter3 = 0

print("Enter 3 numbers")
for i in range(1,6): #1 2 3 4 5
    num = int(input())
    list.append(num) # 1 2 30 200 300

for num in list:
    if num >= 1 and num <=9 :
        counter1=counter1+1
    elif num >= 10 and num <= 99:
        counter2 = counter2+1
    elif num >= 100 and num <= 999:
        counter3 = counter3 + 1

print("1 Digit count = > ",counter1)
print("2 Digit count = > ",counter2)
print("3 Digit count = > ",counter3)



