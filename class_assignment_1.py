# if condition 

x = int(input("Enter the number"))

if x > 0:
     print("The number is positive")
elif x < 0:
    print("The number is negative")
else:
     print("The number is zero")

x = int(input("Enter the number"))

if x % 2 == 0:
     print("The number is even")
else:
     print("The number is odd")

print("The number is positive") if x > 0 else print("The number is negative")

x = int(input("Enter the number"))
y = int(input("Enter the number"))
#if only cases

if x == y:
     print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
     print("y is greater than x")
else:
     print("x is not greater than y")