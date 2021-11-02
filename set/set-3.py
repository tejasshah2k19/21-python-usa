


s = set() # s => set => an empty

for i in range(0,5):
    print("Enter number")
    num = int(input())
    s.add(num)

print("all elements:- ")
print(s)

print("even numbers:- ")
for data in s:
    if data % 2 == 0:
        print(data)

#take 5 numbers from user and find out the max from it using set
#take 5 numbers from user and count how many 1 , 2 and 3 digit numbers present in set
#e.g -> 5 numbers -> {1,22,333,4,55}
#   output :-   1 digit total numbers => 2
#               2 digit total number => 2
#               3 digit total number => 1





