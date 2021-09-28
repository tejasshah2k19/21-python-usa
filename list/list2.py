numbers =  []

for i in range(1,6):
    num = int(input("Enter number"))
    numbers.append(num)

print(numbers)

print("single elements from list")
for i in range(0,len(numbers)):
    print(numbers[i])
