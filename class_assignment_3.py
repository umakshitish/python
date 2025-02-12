i = "helloworld"

out = "###############Hello#########World#####################"

x = i[0:5].title() + "#########" + i[5:].title()
print(x)
total_length = len(out)

if out[0] != "H":
    text = input("Enter the character")
    left_length = total_length - len(out.lstrip("#"))
    right_length = total_length - len(out.rstrip("#"))
    result = text*left_length + x + text*right_length
    print("result", result)