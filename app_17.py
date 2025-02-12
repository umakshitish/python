# function continue global variable/ local variable

# def my_function():
#     x = 10
#     print("inside function:", x)

# my_function()

# # print("outside function:", x)

# def update_global():
#     global z
#     z = 5
#     print("inside function:", z)

# update_global()

# print("outside function:", z)

# y = 20

# def my_funcgtion():
#     print("inside function", y)

# my_funcgtion()
# print("Outside function:", y)

# def my_function(*kids):
#     a = type(kids)
#     for x in range(len(kids)):
#         print(f" Child{x+1} {kids[x]}")

# my_function("Emil", "Tobias", "Linus")


# def my_function(**kids):
#     a = type(kids)
#     print(a)
#     for x in range(len(kids)):
#         print(f" Child{x+1} =  {kids[x]}")


# print(myfamily)


# my_function(fname = "Emil", lname = "Linus")


# recurrisive function (self calling function)

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n -1)

# print(fact(5))

def fib(n):