# Data types
#getting data type
z = frozenset({"apple", "banana"})
print(type (z))
r = None
print(type (r))

x = float(input("Enter first number"))
y = float(input("Enter second number"))
sum = x + y
subs = x - y
prod = x * y
quot = x / y
rem = x % y
intquot = x // y
pow = x ** y
print("The sum is", sum)
print("The difference is", subs)
print("The product is", prod)
print("The quotient is", quot)
print("The reminder is", rem)
print("The integer quotient is", intquot)
print("The power is", pow)
if(x > y):
    print("First number is greater")
else:
    print("Second number is greater")
print(type(sum))