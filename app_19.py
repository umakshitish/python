#exception handling

# try:

#     a = 1
#     b = "c"
#     result = a/b 
#     print(result)
# except:

# finally

#built in exception handling

#
# except ZeroDivisionError as e:
#     print(e)
#     print("You have eter the zero value for number second")
#     x = int(input("Enter the first number"))
#     y = int(input("Enter the second number"))
#     result = x / y
#     print("result", result)

# except ValueError as e:
#     print(e)
#     print("You have eter the character instead of numberzero value for number second")
#     x = int(input("Enter the first number"))
#     y = int(input("Enter the second number"))
#     result = x / y
#     print("result", result)


#custom exception

x = int(input("Enter your age"))

try:
    if x < 0:
        raise Exception("Sorry, no number belo zero")
    elif x == 0:
        raise Exception("Sorry, age is zero")
except Exception as e:
    print(e)
    x = int (input("Re-enter the age"))

#different exception handling differently

