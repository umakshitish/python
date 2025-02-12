# pythen function
#def function_name(parameters):

#function_name(argument):

#Parameter type function
# def addition(a,b):
#     result = a + b
#     print(result)
#     return result

# addition(1, 5)

# #Parameter less and no return type function

# def add():
#     a = 5
#     b = 4
#     print("adding")
#     result = a + b
#     print(result)

# print("entering the function")
# add()


# #with Parameter and no return type function

# def add(x, y):
#     print("adding")
#     result = x + y
#     print(result)
# print("entering the function")
# a = 1
# b = 2

# add(a,b)


#with parameter less with return type

def add():
    print("adding")
    x = 10
    y = 20
    result = x + y
    return result
print("entering the function")

x = add()
x = x +1
print(x)

#parameter with return type

def add(x,y):
    print("adding")
    result = x + y
    return result, a

print("entering the function")

a = 1
b = 2


addition = add(a, b)
print(type(addition))
final_result = addition +1