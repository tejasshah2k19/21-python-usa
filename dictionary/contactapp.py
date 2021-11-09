"""

    in phoneBook App we have information of the users , firstname email and   contact number

    we need to make menu driven app so user can add any new contact, search existing contact by name
    also modify existing contacts.

"""

users = []  # main list in which all users information will store

while True:
    print("Press\n1 For New Contact\n2 For Search Contact\n3 For Modify Contact\n0 for Exit \nEnter Your choice")
    choice = int(input())

    if choice == 1:
        # add contact
        print("Enter firstname")
        firstName = input()
        print("Enter Email")
        email = input()
        print("Enter Contact Num")
        contactNum = input()

        #single user information
        user = {"firstName":firstName,"email":email,"contactNum":contactNum}
        users.append(user)
    elif choice == 2:
        #search contact
        print(users)
    elif choice ==  3:
        #modify
        pass
    elif choice == 0:
        exit(0)
    else :
        print("Invalid choice try again!!!")