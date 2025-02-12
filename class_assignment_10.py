
import project_1

project_1.init_db()

while True:
    print("1. Create Record")
    print("2. Read Records")
    print("3. Update Records")
    print("4. Delete Records")
    print("5. Exit")

    option = int(input("Enter your option"))

    if option == 1:
        while True:
            name = input("Enter the name : ")
            age = int(input("Enter the age : "))
            email = input("Enter the Email Address : ")
            project_1.create_records(name, age, email)
            break
    elif option == 2:
        project_1.display_records()
    elif option == 3:
        update_records()
    elif option == 4:
        project_1.delete_records()
    else:
        break

