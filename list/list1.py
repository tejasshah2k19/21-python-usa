numbers = [1,2,3,4,5]

print(numbers)
print(numbers[3])

data = [ 1,2,"royal",30.50,55]
print(data)
print(data[2])


#take 5 numbers from user and print sum of all numbers , also print all five numbers.
numbers = []

for i in range(0,5):
    num = int(input("Enter number"))
    numbers.append(num)

sum = 0
for i in range(0,5):
    sum = sum + numbers[i]
    print(numbers[i])

print("sum = ",sum)

#8.15
#8.00