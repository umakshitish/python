# lambda function

# square = lambda x: x**2
# print(square(5)) 


# add = lambda a, b: a + b
# print(add(3, 4))


lst = [1, 2, 3, 4, 5, 6, 7]

# add1 = list(map(lambda x: x+1, lst))
# print(add1)

# squared = list(map(lambda x: x**2, lst))

# def sq(x):
#     return x ** 2
# squared = list(map(sq, lst))

# print(squared)

# def sq(x):
#     x +=1
#     return x
# squared = list(map(sq, lst))

# print(squared)

#filter
# even = list(filter(lambda x: x%2 == 0, lst))

# def even(x):
#     if x%2==0:
#         return x
    ##return x % 2 == 0 alternatively
# even = list(filter(even, lst))

# print(even)

# lst = ["abc", "cde", "apple", "coconut", "bob", "zoo"]
# f = list(filter(lambda x: x=="a", lst))
# print(f)

# def check_a(x):
#     return "a" in x

# result = list(filter(check_a, lst))

# print(result)

# # alternatively
# result = list(filter(lambda x: "a" in x, lst))

# print(result)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
# sum = reduce(lambda x, y: x+y, numbers)
# print(sum)

# max_num = reduce(lambda x, y: x if x>y else y, numbers)
# print(max_num)

words = ["Hello", " ", "World" ]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)

product = reduce(lambda x, y: x * y, numbers, 1)
print(product)