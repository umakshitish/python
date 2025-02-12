import csv
import pandas as pd

# with open("text.csv", "r") as f:
#     csv_reader = csv.DictReader(f)
#     for row in csv_reader:
#         print(row["name"], row["age"], row["city"])

# data = [
#     {"name":"Bedant", "age":10, "city":"ktm"},
#     {"name":"Bedanshi", "age":16, "city":"btm"},
#     {"name":"Manish", "age":52, "city":"ktm"}
# ]

# file_path = "output.csv"
# fieldnames = ["name", "age", "city"]

# with open(file_path, mode = "w", newline = "") as file:
#     writer = csv.DictWriter(file, fieldnames = fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)


# import pandas as pd

# df = pd.read_csv('cleaning_test.csv')
# print(df)
# new_df = df.dropna()
# print(new_df)

# df = pd.read_csv('cleaning_test.csv')
# df.dropna(inplace = True)
# print(df)

# df = pd.read_csv('cleaning_test.csv')
# df.fillna(20, inplace = True)
# print(df)

# df = pd.read_csv('cleaning_test.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)
# print(df)

df = pd.read_csv('cleaning_test.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.fillna(20, inplace = True)
print(df)


# df.dropna(subset = ['Date'], inplace = True)