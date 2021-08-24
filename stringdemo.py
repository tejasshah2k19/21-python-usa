name = "royaleducation"
      # 01234567890123
"""
r 
o
y 
a
l
e

"""
counter = 0
space = 1
for i in range(0,len(name)):
    print(name[i])
    if name[i] == "a" or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":
        counter = counter + 1 #counter++
    if name[i] == " ":
        space = space + 1

print("total vowels : ",counter)

# take string from user and count total words ?

name = "jony jony yes papa" # input("Ente string with multiple words")

# 4 words are present

space = 1
for i in range(0,len(name)):
    if name[i] == " ":
        space = space + 1
print("total words : ",space)


# take a string from the user and print each character from even index.
      # 01234567890123
name = "royaleducation"
# =>  ryldcto
print(name[::2])


# take string from user and check it's palindrome or not

# royal == layor => not same => not palindrome
# madam == madam => same => palindrome



name = "royal"

print(name[::]) # name[::1] => starts with zero ends with length -1

print(name[::-1]) # starts with size-1 to zero index and decrement by 1 // inc by -1

print(name[::2]) # starts with  0 end with size-1 and increment by 2

if name == name[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



