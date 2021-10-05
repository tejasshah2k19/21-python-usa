#take 5 numbers from user and count total odd and even also perform sum of odd and even numbers.
list = []
for i in range(0,5):
    print("Enter number")
    num = int(input())
    list.append(num)
# 11 22 33 44 55
odd=0
even=0
oddSum = 0
evenSum = 0
for num in list:
    if num%2 == 0:
        even = even + 1
        evenSum = evenSum + num
    else:
        odd = odd + 1
        oddSum = oddSum + num
print("total odd  => ",odd)
print("total even => ",even)
print("sum of odd  => ",oddSum)
print("sum of even => ",evenSum)
#odd 3
#even 2