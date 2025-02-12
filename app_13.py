# # Dictonary

# empty_dict = {}

# my_dict = {
#     "name" : "Kshitish",
#     "Age" : 49,
#     "City" : "Kathmandu"
# }
# # print(my_dict)

# mixed_dict = {
#     1: "One",
#     "2": "Two"
#     # (1, 2):"Tuple"
# }
# # print(my_dict["address"])
# print(my_dict.get("address"))


# dict1 = {
#     "name":"abc",
#     "age":24,
#     "name":"Kshitish"
# }
# print(dict1.get("name", 123))

#adding dictonary


# my_dict = {}
# name1 = input("Enter the name")
# add1 = input("Enter the address")
# age1 = int(input("Enter the age"))

# my_dict["name"] = name1
# my_dict["address"] = add1
# my_dict["age"] = age1

# print(my_dict)

#delete

# my_dict = {}
# name1 = input("Enter the name")
# add1 = input("Enter the address")
# age1 = int(input("Enter the age"))

# my_dict["name"] = name1
# my_dict["address"] = add1
# my_dict["age"] = age1

# print(my_dict)

# my_dict.pop("address")

# print(my_dict)

#loop

# my_dict = {
#     "name" : "Kshitish",
#     "Age" : 49,
#     "City" : "Kathmandu"
# }
# # for x in my_dict:
# #     print(my_dict[x]) # alternate
# #     print(my_dict.get(x))

# for x in my_dict.values():
#     print(x)


my_dict = {
    "name" : "Kshitish",
    "Age" : "49",
    "City" : "Kathmandu"
}
# for x in my_dict:
#     print(x, my_dict.get(x))

# update = input("Which key you want to update")
# if 

for x, y in my_dict.items():
    print(x, y)
    
