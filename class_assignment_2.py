#Nested loop
    
# for r in range(6):
#     for c in range(r):
#         print(c+1, end = " ")
#     print("\n")
for r in range(5, 0, -1):
    for c in range(r):
        print(c+1, end = " ")
    print("\n")


# for r in range(5, 0, -1):
#     for c in range(r):
#         print(r, end = " ")
#     print("\n")

# for r in range(6):
#     for c in range(r):
#         print(r, end = " ")
#     print("\n")

# x = 0
# y = 0
# while x < 6:
#     while y < 6:
#         print(y+1, end = " ")
#         y = y + 1
#     print("\n")
#     x = x + 1