#take number from user and find out number is odd or even

print("Enter a number")

num = int(input())
#if we divide number with 2 and if we got remainder 0 then number is even otherwise its odd

if num%2 == 0:
    print(num," is Even")
else:
    print(num," is Odd")
