#take a number from the user and check it's positive or negative number.

#12  -> positive
#-12 -> negative

num = int(input("Enter a number"))

if num > 0:
    print(num," is Positive")
elif num < 0:
    print(num," is negative")
else:
    print("It's ZERO")

