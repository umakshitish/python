# # copy in dictonary




# #nested loop in dictonary

# myfamily = {
#     "child1" : {
#         "name":"Emil",
#         "year":"2007",
#     },
#     "child2":{
#         "name":"Ram",
#         "year":"2010",
#     },
#     "child3":{
#         "name":"Kumar",
#         "year":2004,
#     },
# }
# # print(myfamily["child1"]["name"])
# # print(myfamily["child2"]["name"])
# # print(myfamily["child3"]["name"])

# for k, v, in myfamily.items():
#     # print("this is key",k)
#     # print("this is value",v)
#     if type(v) == dict:
#         print(v["year"])
#     else:
#         print(v)

myfamily = {}


# num = int(input("Enter the number of children"))
# for x in range(num):
#     child = {}
#     name = input("Enter the name")
#     year = input("Enter the year")

#     child["name"] = name
#     child["year"] = year
#     myfamily[f"child{x+1}"] = child
# print(myfamily)

# {'child1': {'name': 'ram', 'year': '2005'}, 'child2': {'name': 'shyam', 'year': '2006'}}

num = int(input("Enter the number of children"))
for x in range(num):
    child = {}
    name = input("Enter the name")
    year = input("Enter the year")

    child["name"] = name
    child["year"] = year
    myfamily[f"child{x+1}"] = child
print(myfamily)
k1 = input("Enter the key")
myfamily.pop(k1)
print(myfamily)


# student = {
#     1:{
#         "name":"abc",
#         "age":"32",
#         "class":5,
#         "address":"Ktm",
#         "marks":{
#             "science":60
#             "math":50
#             "english":79
#         }
#     }
# }

# 1. insert
# 2. delete
# 3. update