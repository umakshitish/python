# List

# name = "abc"

# lst = ["apple", "banbaba", "grapes"]
# if "apple" in lst:
#     print("there is a in ", lst)

# List comprehensive

# lst = ["pple", "banbaba", "grapes"]
# newlst = []
# for x in lst:
#     if "a" in x:
#         newlst.append(x)
# print(newlst)

# lst = ["pple", "banbaba", "grapes"]
# newlst = [x for x in lst if "a" in x]
# print(newlst)

# numbers = [1, 2, 3, 4, 5, 6]
# even_list = []
# for x in numbers:
#     md = x%2
#     if md == 0:
#         even_list.append(x)
# print(even_list)

# numbers = [1, 2, 3, 4, 5, 6]
# even_list = [x**2 for x in numbers if x%2!=0]
# print(even_list)

# fruits = ["apple", "banbaba", "grapes"]
# newlist = [x if x!= "banana" else "orange" for x in fruits ]
# print(newlist)

# list1 = []
# for x in fruits:
#     if x!= "banana":
#         list1.append(x)
#     else:
#         list.append("orange")
# print(list1)


# numbers = [1, 2, 3, 4, 5, 6]
# even_list = []
# for x in numbers:
#     md = x%2
#     if md == 0:
#         even_list.append(x)
# print(even_list)


# numbers = [1, 2, 3, 4, 5, 6]
# even_list = ["odd" if x%2!=0 else "even" for x in numbers]
# print(even_list)


# Short

# lst = ["apple", "banbaba", "grapes", "app", 1, 2, 3]
# lst.sort()
# print(lst)


str_list = []
num_list =[]
lst = ["apple", "mango", "anbaba", "grapes", "app", 1, 2, 3]

while True:
    option = int(input("Enter the option 1 for string list, 2 for number list and any number to exit"))
    if option == 1:
        str_list = [x for x in lst if type(x)==str]
        str_list.sort()
        print(str_list)
    elif option == 2:
        num_list = [x for x in lst if type(x) == int]
        num_list.sort(reverse = True)
        print(num_list)
    else:
        break
#a = str_list.sort(reverse = True)
#print(a)

# newlist = sorted(lst, reverse = True)




# lst = ["apple", "banbaba", "grapes", "app", 1, 2, 3]
# #shallocopy
# #  mylist = lst

# mylist = lst.copy()
# print(lst)
# print(mylist)


# lst = ["apple", "banbaba", "grapes"]
# lst1 = [1, 2, 3]

# lst2 = lst + lst1
# lst3 = lst.extend(lst1)
# print(lst2)
# print("extend",lst3)