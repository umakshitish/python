#File handling
# Open

# f = open("fileread.txt", "r")
# value = f.read()
# print(value)
# print(value[0:5])
# print(value[7:14])
# print(value[48:56])
# print(value[-5:-1])


# f = open("fileread.txt", "r")
# value = f.read()

# print(value)
# print(value[0:5])
# print(value[7:14])
# print(value[48:56])
# print(value[-5:-1])
# splitted_value = value.split()
# print(splitted_value[1])
# print(splitted_value[-4])
# print(splitted_value[-1])


# f = open("fileread.txt", "r")
# value = f.readline()
# splitted_value = value.split()

# print(splitted_value[1])

# splitted_value2 = value.split()
# print(splitted_value[-3])

# splitted_value2 = value.split()
# print(splitted_value[-4])

# f = open("fileread.txt", "r")

# for x in f:
#     print(x)
#     print(type(x))

# value = f.readlines()
# print(value)
# f.close()


# file write
# f = open("sample.txt", "a")
# f.write("\n This is new text")

# f.close()

# f = open("sample.txt", "a")
# text = input("enter the text")
# f.write("\n text \n")

# f.close()


f = open("sample.txt", "w")
for x in range(2):
    x= input("enter the content")
    last = x +"\n"
    f.write(last)

f.close