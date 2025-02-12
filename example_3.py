# f = open("sample.txt", "w")
# for x in range(2):
#     x = input("enter the content")
#     last = x + "\n"
#     f.write(last)
# f.close()

import csv
with open("test.csv", "r") as f:
    csv_reader = csv.reader(f)
    # header = next(csv_reader)
    print("data starts")
    for x in csv_reader:
        print(x)