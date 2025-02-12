
my_dict = {}
while True:
    choice = int(input("Do you want to enter the number press 1 to Display, 2 to Update, 3 to Insert, 4 to Delete and 5 to Exit"))
    if choice == 1:
        key1 = input("Enter the key to add")
        key2 = input("Enter the key to add")
        key3 = input("Enter the key to add")
        
        if key1 != my_dict.keys():
            val1 = input("Enter the value for key")
            my_dict["name"] = val1
            val2 = input("Enter the value for key")
            my_dict["address"] = val2
            val3 = input("Enter the value for key")
            my_dict["age"] = val3
    elif choice == 2:
        key1 = input("Enter the  key to update")
        print(my_dict.keys())
        if key1 in list(my_dict.keys()):
            val1 = input("Enter the value for new key")
            my_dict.update({key1: val1})
        else:
            print("Given key is already exists")
    elif choice == 3:
        key1 = input("Enter the new key")
        if key1 != my_dict.keys():
            val1 = input("Enter the value for new key")
            my_dict[key1] = val1
        else:
            print("Given key is already exists")
    elif choice == 4:
        key1 = input("Enter the key to delete")
        if key1 != my_dict.keys():
            my_dict.pop(key1) 
        else:
            print("Given key is already exists")
    else:
            break
    print(my_dict)