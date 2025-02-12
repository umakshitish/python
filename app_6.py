# name = "Hello World"
# print(name[6:])
# print(name[::-1])

# name = "hi" + name[:5]
# print(name)

# String methods

# name = name.replace("World", "Python")
# print(name)

name = "Hello World w"
l = len(name)
for x in range(l):
    # print(name[x])
    if name[x].lower() == "w":
        print(x)

name.replace("World", "WORLD")
print(name.title())

# name = "      Kshitish        Bhattarai      "
# print(name)
# print(name.lstrip())
# print(name.rstrip())

# s = name.strip()
# result = s[:8]+s[-9:]
# print(result)