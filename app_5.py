# For Loop
# for x in range(10, 20, 2):
#     print("even numbers", x)
# for x in range(11, 20, 2):
#     print("Odd numbers", x)

# While Loop

# x = 0
# while x < 10:
#     if x % 2 == 0:
#         print("even", x)
#     else:
#         print("Odd", x)
#     x = x + 1

# for x in range(10):
#     if x == 5:
#         sum = x + 1
#         print("sum", sum)

#         print("breaking loop")    
#         break
#         print("after breaking loop")
# sum = sum + x
 
# for x in range(10):
#     if x == 5:
#         print("breaking loop")
#         continue
#         print("after breaking loop")
#     print(x)

# sum = 0
# for x in range(10):
#     if x == 5:
#         print("breaking loop")
#         break
#         print("after breaking loop")
#     print(sum)
#     sum = sum + x

# pass
sum = 0
for x in range(10):
    pass

# Swapping variable
# x = 10
# y = 20
# print("Before Swap")
# print("x", x)
# print("y",y)

# #swapping
# # z = x
# # x = y
# # y = z
# x = x + y
# y = x - y
# x = x - y

# #x, y = y, x
# print("After Swap")
# print("x", x)
# print("y",y)

#Nested loop
    
# for r in range(6):
#     for c in range(r):
#         print(c+1, end = " ")
#     print("\n")

# String
# name = """My name is
# Kshitish Bhattarai"""
# print(name)

# # Indexing

# print(name[11])
# print(name[-9])

# name = "Hello World"
# l = len(name)
# for x in range(l):
#     # print(name[x])
#     if name[x] == "W" or name[x] == "w":
#         print(x)

# name = "Hello World"
# print(name[6:])
# print(name[::-1])

# name = "hi" + name[:5]
# print(name)

# String methods

# name = name.replace("World", "Python")
# print(name)

# name = "Hello World w"
# l = len(name)
# for x in range(l):
#     # print(name[x])
#     if name[x].lower() == "w":
#         print(x)

# name.replace("World", "WORLD")
# print(name.title())

name = "      Kshitish        Bhattarai      "
print(name)
print(name.lstrip())
print(name.rstrip())

s = name.strip()
result = s[:8]+s[-9:]
print(result)