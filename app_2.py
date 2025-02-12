# Operators
# Comparison Operators
a = 10
b = 12
x = 5
if(a <= b):
    print("B is greater")
else:
    print("A is greater")
#logical operator
print((x<5 and x<10) or x!=1)
print(a == b)
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is not y)

m = "hello"
print("a" not in m)

x = 20
print(x)
x %= 6
print(x)

# Data types
#getting data type
z = frozenset({"apple", "banana"})
print(type (z))
r = None
print(type (r))

x = float(input("Enter first number"))
y = float(input("Enter second number"))

x == y

result = x + y

print("The sum is", result)
print(type(result))