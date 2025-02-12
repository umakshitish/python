
fruits = ["mango", "apple", "cherry", "mango", "mango"]

# while True:
#     choice = int(input("Do you want to enter the number press 1 to append"))
#     if choice == 1:
#         new_fruits = input("Enter the fruit to add")
#         fruits.append(new_fruits)
#     elif choice == 2:
#         new_fruits = input("Enter the fruit to remove duplicate")
#         fruits.append(new_fruits)
#     elif choice == 3:
rem_fruits = input("Enter the fruit to delete all similar fruit")
index = 0
l = len(fruits)
for x in fruits:
    if fruits[index].lower() == rem_fruits:
        fruits.remove(rem_fruits)
        index += 1
            # else:
            #     break
print("This list", fruits)   