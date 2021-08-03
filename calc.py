a = int(input("Enter a number"))
b = input("Enter second number")
b = int(b)

print("1 for Addition\n2 For Sub\n3 For Mul")
print("Enter your choice")

choice = int(input())

if choice == 1:
    ans = a+b
    print("addition = ",ans)
if choice == 2:
    ans = a-b
    print("sub = ",ans)
if choice == 3:
    ans = a*b
    print("mul = ",ans)

print("bye")