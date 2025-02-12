import app_25
while True:
    while True:
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Enter your option"))
   
        if choice == 1:
            while True:
                a = int(input("Enter the first no"))
                b = int(input("Enter the second number"))
                app_25.sum(a,b) 
                break
        elif choice == 2:
            while True:
                a = int(input("Enter the first no"))
                b = int(input("Enter the second number"))
                app_25.diff()
                break 
            
            