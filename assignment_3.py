user_details = {}
marks_li = []
phone_li = []

print("Please enter all your details:")

#user's name
name = input("Enter your name: ").title()
user_details["Name"] = name

#user's age
while True:
    age = int(input("Enter your age: "))
    if age < 1:
        print("Invalid age")
    else:
        break
user_details["Age"] = age

#user's marks
while len(marks_li) < 5:
    marks = int(input("Enter your marks: "))
    if 0 < marks <= 100:
        marks_li.append(marks)
    else:
        print("Please input a valid number")
user_details["Marks"] = marks_li

#user's phone numbers
phone_u = int(input("How many numbers do you want to input: "))
while len(phone_li) < phone_u:
    phone = int(input("Enter your phone number: "))
    if len(str(phone)) == 10 and phone > 0:
        phone_li.append(phone)
    else:
        print("Please input a valid phone number")
user_details["Phone"] = phone_li

#total marks
total_marks = sum(marks_li)
user_details["Total Marks"] = total_marks

#user details
for k, v in user_details.items():
    print(k, v, "|", end=" ")