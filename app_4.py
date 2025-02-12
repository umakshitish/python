# loop (Iteration)

# numbers = [1, 2, 3, 4, 5]
# s = 0
# t = 0
# for num in numbers:
#     if num % 2 == 0:
#         s = num + s
#     elif num % 2 != 0:
#         t = num + t
# print("Sum of odd", t)
# print("Sum of even", s)

# strings = ["Ram", "Shyam", "Gita", "Hari", "Sangita"]
# for str in strings:
#     if str == "Gita":
#         print(str)

# sum = 0
# for x in range(5):
#     value = int(input("Enter the number: "))
#     sum = sum + value
# print("The sum is: ", sum)


value1 = int(input("Enter the number: "))
value2 = int(input("Enter the number: "))
s = 0
t = 0
for x in range(value1, value2):
    if x % 2 == 0:
        s = x + s
    elif x % 2 != 0:
        t = x + t
print("Sum of odd", t)
print("Sum of even", s)