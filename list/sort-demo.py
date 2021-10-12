list = []

print("Enter 7 numbers")
for i in range(1,8): #1 2 3 4 5
    num = int(input())
    list.append(num) # 10 20 30


print("Before Sort => ",list)
#sorting
list.sort()
#list.reverse()
print("After Sort => ",list)