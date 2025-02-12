#file handling
#delete

# import os
# os.remove("d:/basic/fileread.txt")

import os
if os.path.exists("sample1.txt"):
    os.remove("sample1.txt")
else:
    print("the file does not exist")

# delete folder

# import os
# os.rmdir("myfolder")

#handling CSV files

# import csv
# with open("test.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#         print(row)

# import csv
# with open("test.csv", "r") as file:
#     csv_reader = csv.reader(file)

#     head = input("The header exists or not y/n")

#     if head == "y":
#         header = next(csv_reader)
#         for row in csv_reader:
#             print(row)
#     else:
#         for row in csv_reader:
#             print(row)

# import csv
# with open("test.csv", "r") as file:
#     csv_reader = csv.reader(file, delimiter=",")
#     check_header = False
#     # head = input("The header exists or not y/n")

#     if check_header:
#         header = next(csv_reader)
#             for row in csv_reader:
#             print(row)


# write in csv file

import csv
data = []

number = int(input("How many rows you have to enter"))
for x in range(number):
    row = []
    name = input("Enter the name")
    age = int(input("Enter the age"))
    city = input("Enter the city")

    row.append(name)
    row.append(age)
    row.append(city)

    data.append(row)
print(data)
with open("text.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["name", "age", "city"])
    for x in data:
        csv_writer.writerow(x)
        
    
