import csv
data = []

number = int(input("How many rows you have to enter"))
for x in range(number):
    row = []
    name = input("Enter the name")
    age = int(input("Enter the age"))
    math = int(input("Enter the numbers in math: "))
    eng =int(input("Enter the numbers in english: "))
    sci = int(input("Enter the numbers in science: "))
    total = math + eng + sci

    row.append(name)
    row.append(age)
    row.append(math)
    row.append(eng)
    row.append(sci)
    row.append(total)
    data.append(row)
print(data)
with open("result.csv", "a", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["name", "age", "math", "english", "science", "total"])
    for x in data:
        csv_writer.writerow(x)