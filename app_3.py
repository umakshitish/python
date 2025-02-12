# Nested if
#x = int(input("Enter the number"))

# if x > 0:
#     if x < 10:
#         print("The number is positive")
#         print("The number is single digit")
#     elif x < 100:
#         print("The number is positive")
#         print("The number is double digit")
# elif x < 0:
#     print("The number is negative")
# else:
#      print("The number is zero")

# if x > 0 and x < 10:
#         print("The number is positive and single digit")
# elif x > 0 and x > 10 and x < 100:
#     print("The number is positive and double digit")
# elif x < 0:
#     print("The number is negative")
x = input("Enter the number")
print(type(x))
if x.isdigit():
    y = int(x)
    print(y)
    print(type(y))
elif "." in x:
    y = float(x)
    print(y)
    print(type(y))
else:
    print("String")
