# def get_stats(numbers):
#     min_value = min(numbers)
#     max_value = max(numbers)
#     sum_value = sum(numbers)
#     return min_value, max_value, sum_value

# numbers = [1, 2, 3, 4, 5]
# result = get_stats(numbers)

# print("minimum", result[0])
# print("maximum", result[1])
# print("sum", result[2])

# def get_stats(numbers):
#     return{
#         'min': min(numbers),
#         'max': max(numbers),
#         'sum': sum(numbers)
#     }
    

# numbers = [1, 2, 3, 4, 5]
# result = get_stats(numbers)

# print("minimum", result['min'])
# print("maximum", result['max'])
# print("sum", result['sum'])



# def ui():
#     print("""
#           1. addition
#           2. substraction
#           3. multiply
#           4. division
#           """)
# add()
# subs()
# multiply()
# division()


def add(*args):
    print(args[0])
    result= sum(args[0])
    return result
def subs(**args):
    for i in range(len(x)):
        result = a - b
    return result
def mul():
    pass

while True:
    choice = int(input("Enter your choice 1. Add, 2. Substract, 3. Multifly and 4. Exit"))
    if choice == 1:
        nos = int(input("How many numbers you want :"))
        x = []
        for i in range(nos):
            a = int(input("Enter the number: "))
            x.append(a)
        result = add(x)
        print(result)
    elif choice == 2:
        nos = int(input("How many numbers you want :"))
        x = []
        for i in range(nos):
            a = int(input("Enter the number: "))
            x.append(a)
        result = subs(x)
        print(result)
    elif choice == 3:
        nos = int(input("How many numbers you want :"))
        x = []
        for i in range(nos):
            a = int(input("Enter the number: "))
            x.append(a)
        result = add(x)
        print(result)
    else:
        break
