"""

Amazon Inventory :-

    For Amazon we have to maintain all the stocks details.
    stock contains information about products .
    products :-  unique id of product , name , category , quantity and price.

    1. Add Product
    2. List All Product
    3. Search Product By Id
    4. exit

"""
productList = []  # list is empty
while True:
    print("Press\n1. Add Product\n2. List All Product\n3. Search Product By Id\n4. exit")
    print("\nEnter your choice")

    choice = int(input())

    if choice == 1:
        productId = input("Enter ProductId")
        name = input("Enter Product Name")
        price = input("Enter Product Price")
        category = input("Enter Product Category")
        quantity = input("Enter Product Quantity")

        product = {"productId":productId,"name":name,"price":price,"category":category,"quantity":quantity}
        print(product)

        productList.append(product)

    elif choice ==2:
        print(productList)
    elif choice ==3:
        pass
    elif choice == 4:
        exit(0)













