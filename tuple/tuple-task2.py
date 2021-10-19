list = []
for i in range(0,5):
    print("Enter number")
    num = int(input())
    list.append(num)

#t = (1,2,33,44,55)

t = tuple(list)  # converting list into tuple -> tuple()

totalEven=0
max=0
for data in t:
    if data%2 == 0:
        totalEven=totalEven+1
    if max < data:
        max = data #55

print("max =>>",max)
print("total even =>> ",totalEven)