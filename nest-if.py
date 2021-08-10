#three numbers from user
#find out max

a = int(input("Enter first Num"))
b = int(input("Enter second Num"))
c = int(input("Enter third Num"))


if a>b:
    if a>c:
        print(a," is MAX")
    else:
        print(c," is MAX")
else:
    if b>c:
        print(b," is MAX")
    else:
        print(c," is MAX")

if a>b and a>c:
    print(a," is max")
elif b>a and b>c:
    print(b," is max")
elif c>a and c>b:
    print(c," is max")
else:
    print("ALL ARE EQUAL")