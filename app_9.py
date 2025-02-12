# Modifying List

# thislist = ["apple", "Banana", "cherry", "orange", "kiwi", "mango"]
# print(thislist)
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist[1:3] = ["tomato"]
# print(thislist)


# thislist = ["apple", "Banana", "cherry", "orange", "kiwi", "mango"]

# thislist.insert(2, "lichhi")
# print(thislist)


# thislist = ["apple", "Banana", "cherry", "orange", "kiwi", "mango"]

# thislist.append("abcde")
# print(thislist)


# thislist = ["apple", "Banana", "cherry"]
# tropical = ["orange", "kiwi", "mango"]

# thislist.extend(tropical)

# print(thislist)


# thislist = ["apple", "Banana", "cherry"]
# thistuple = ("orange", "kiwi", "mango")

# thislist.extend(thistuple)

# print(thislist)



#numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# numbers = []
# while True:
#     choice = int(input("Do you want to enter the number press 1 to add"))
#     if choice == 1:
#             num = int(input("Enter the number to print"))
#             numbers.append(num)
#         print(numbers)
#     else:
#         break:
# print("This list", numbers)           
  
fruits = ["apple", "banana", "cherry", "mango", "banana"]
# print(fruits)

# val = input("enter which value to be repalced")
# updated_value = input("what value to be replaced")

# index = 0
# for x in fruits:
#     if x == val.lower():
#         fruits[index] = updated_value
#     index += 1
# print(fruits)

# Alternate
# index = 0
# for x in range(len(fruits)):
#     if fruits[x] ==val.lower():
#         fruits[index] = updated_value
#     index += 1
# print(fruits)


this_list = ["apple", "banana"]

#del this_list

# this_list.clear()
# print(this_list)
this_list.remove("apple")
print(this_list)