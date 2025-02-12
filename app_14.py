# student = {
#     "name":"abc",
#     "age":30,
#     "marks": [10,20,30,40,50]
#     "phone": [9842377700]
#     "totalmarks":444
# }

studednt_dic = {}
name = input("Enter the name of student:")
# student_dic["name"] = name
age = input("Enter the age of student:")
# student_dic["age"] = age
lst = []
while True:
    if len(lst) == 5:
        break
    marks =int(input("Enter the marks:"))
    if marks >= 0 and marks <=100: 
        lst.append(marks)
    else:
        print("Error entry")
numbers = int(input("enter how many numbers you have"))
lst_phone = []
for x in range(numbers):
    phone =int(input("Enter the pnone no.:"))
    lst_phone.append(phone)
print(lst)

