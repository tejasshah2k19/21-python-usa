product = { }


print("Enter name and price for product")
name = input()
price = int(input())

print("Enter qty , Category , mfgDate and expDate For Product")
qty = int(input())
category = input()
mfgDate = input()
expDate = input()


product.update({"name":name,"price":price,"qty":qty,"category":category,"mfgDate":mfgDate,"expDate":expDate})

print(product)

print(product["name"])
print(product.get("price"))






