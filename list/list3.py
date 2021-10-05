# take 5 numbers from the user and store into list
list = []
for i in range(0,5):
    print("Enter a number")
    num = int(input())
    list.append(num)
#12 34 54 6 7
#max = 54
max = list[0]
for num in list:
    print(num)
    if max < num:
        max = num

print("MAX = ",max)
#take 5 numbers from user and count total odd and even also perform sum of odd and even numbers.


