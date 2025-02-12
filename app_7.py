# String
# s = "######hello       world#########"
# x = s.strip("#")
# print(x)

# .split() and join()

# s = "Hello World!"
# x = s.split()
# print(x)
# k = ['Hello', 'World!', 'Python']
# y = " ".join(k)
# print(y)

# .isdigit():, .isupper():

# s = "123.45"
# print(s.isdigit())

# t = "hello"
# print(t.islower()) # True

# a = input("enter your name")
# b = int(input("Enter salary"))
# x = "hello {} this is {} python".format(a, b)
# # print(x)

# a = input("enter your name")
# b = int(input("Enter salary"))
# print(f"hello {a} this is {b} python")


# var = "###############Hello#########World#############"
# x = var.strip("#")
# result = x[:5]+x[-5:]
# print(result) #HelloWorld

# 

# input = "helloworld"

# output = "###############Hello#########World#####################"

# x = input[0:5].title() + "#########" + input[5:].title()
# total_length = len(output)
# left_length = total_length - len(output.lstrip("#"))
# right_length = total_length - len(output.rstrip("#"))
# result = "#"*left_length + x + "#"*right_length
# print("result", result)


input = "helloworld"

output = "###############Hello#########World#####################"

#if output[0] != "H":
    

x = input[0:5].title() + "#########" + input[5:].title()
total_length = len(output)
left_length = total_length - len(output.lstrip("#"))
right_length = total_length - len(output.rstrip("#"))
result = "#"*left_length + x + "#"*right_length
print("result", result)