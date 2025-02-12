# Dictonary with nested loop

result_sheet = {}
a ={}
while True:
    choice = int(input("Do you want to enter the number press 1 to Insert, 2 to Delete, 3 to Update, and 4 to Exit"))
    if choice == 1:
        num = int(input("Enter the number of student"))
        student = {}
        for x in range(num):            
            
            name = input("Enter the name")
            age = input("Enter the age")
            cla = input("Enter hte class")
            add = input("Enter the address")
            student["name"] = name
            student["age"] = age
            student["class"] = cla
            student["address"] = add
            sub = int(input("Enter the number of subjects"))
            marks = {}
            for y in range(sub):
                
                subject = input("enter the subject name")
                mark = int(input("Enter the marks :"))
                marks[subject] = mark
            student[f"marks"] = marks
            a[f"student{x}"]= student
            result_sheet[f"a{x}"] = a
        print(result_sheet)   
    elif choice == 2:
        result_sheet[f"student{x+1}"]= student 
    else:
        break

#     myfamily[f"child{x+1}"] = child
# print(myfamily)
# k1 = input("Enter the key")
# myfamily.pop(k1)
# print(myfamily)

