# input = "helloworld"

# output = "###############Hello#########World#####################"

# x = input[0:5].title() + "#########" + input[5:].title()
# print(x)
# total_length = len(output)

# if output[0].lower !="h":
#     char = output[0]
#     result = input[0:5].lower() + "##" + input[5:].lower()
#     totallength = len(output)
#     lsidelenght = totallength - len(output.lstrip(char))
#     rsidelenght = totallength - len(output.rstrip(char))

#     final = char*lsidelenght + result + char*rsidelenght
#     print(final)



# List

# numbers = [1, 2, 3, 2 4, 2, 5]

# fruits = ['apple', 'banana', 'cherry']

# mixed_list = [10, 'hello, true, 3.14']

# print(numbers, fruits, mixed_list)

# print(fruits[2])
# print(numbers[4])
# print(mixed_list[0])

# print(numbers[:5])
# print(numbers[::-1])

# # for x in numbers:
# #     print(numbers[x])


# numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# fruits = fruits = ['apple', 'banana', 'cherry', 'banana', 'apple']
# count = 0
# y = int(input("Enter the number to print"))
# for x in numbers:
#     if x == y:
#         print(x)
#         count = count + 1
# print(count)


# numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# fruits = ['apple', 'banana', 'cherry', 'banana', 'apple']


# while True:
#     s = int(input(Select the list to count"))
#     if s == 1:
#         count = 0
#         y = int(input("Enter the number to print"))
#         for x in numbers:
#             if x == y:
#                 count = count + 1
#         print("count for", y, count)
#     elif s == 2:
#         count = 0
#         y = input("Enter the fruits to print")
#         for x in fruits:
#             if x == y:
#                 count = count + 1
#         print("count for fruits", y, count)
#     else:
#         print("Exiting for the program")
#         break

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
fruits = ['apple', 'banana', 'cherry', 'banana', 'apple']

print("number1 list", numbers)

count = 0

num = int(input("enter the number to get count"))
for x in numbers:
    
