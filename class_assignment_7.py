with open("sample1.txt", "a") as f:
    for i in range(3):
        x = input("enter the content")
        last = x + "\n"
        f.write(last)
