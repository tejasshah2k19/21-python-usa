user = {
        "firstName":"Raj",
        "email":"raj@gmail.com",
        "password":"raj123",
        "hobby" : ["swimming","reading","cricket"]
}

print(user)
print(user["firstName"])
print(len(user))
print(user["hobby"])
#print(user["firstname"]) #n is small

print(user.get("firstName"))
print(user.get("firstname")) #n is small

# given key is present in dictionary or not ?
# in

if "firstName" in user:
    print("Present")
else:
    print("not Present")


if "city" in user:
    print("Present")
else:
    print("not Present")

# update data in dictionary

print(user)
user["password"] = "secret123"
print(user)

#update()
user.update({"password":"password456"})
print(user)

#adding new item in dictionary

user["country"] = "india"
print(user)

user.update({"pincode":"123456"})
print(user)







