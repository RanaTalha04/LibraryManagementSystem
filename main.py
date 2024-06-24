def signUp_student():
    UserName = input("Enter User Name to sign up: ")
    Password = input("Enter password: ")

    with open("Student.txt","a") as f:
        f.write(f"{UserName},{Password}\n")
        print("\t\tSign Up Successfull...")

def login_student():
    UserName = input("Enter user name to sign in: ")
    Password = input("Enter Password: ")

    with open("Student.txt","r") as f:
        for line in f:
            stored_username,stored_password = line.strip().split(",")
            if(stored_username == UserName and stored_password == Password):
                print("\t\tLogin Successfull")
                return 
        print("\t\tLogin Failed....")

def signUp_faculty():
    UserName = input("Enter User Name to sign up: ")
    Password = input("Enter password: ")

    with open("Faculty.txt","a") as f:
        f.write(f"{UserName},{Password}\n")
        print("\t\tSign Up Successfull...")

def login_faculty():
    UserName = input("Enter user name to sign in: ")
    Password = input("Enter Password: ")

    with open("Faculty.txt","r") as f:
        for line in f:
            stored_username,stored_password = line.strip().split(",")
            if(stored_username == UserName and stored_password == Password):
                print("\t\tLogin Successfull")
                return 
        print("\t\tLogin Failed....")

def signUp_admin():
    UserName = input("Enter User Name to sign up: ")
    Password = input("Enter password: ")

    with open("Admin.txt","a") as f:
        f.write(f"{UserName},{Password}\n")
        print("\t\tSign Up Successfull...")

def login_admin():
    UserName = input("Enter user name to sign in: ")
    Password = input("Enter Password: ")

    with open("Admin.txt","r") as f:
        for line in f:
            stored_username,stored_password = line.strip().split(",")
            if(stored_username == UserName and stored_password == Password):
                print("\t\tLogin Successfull")
                return 
        print("\t\tLogin Failed....")


print("\t\t\t\t\t\t-------------------- WELCOME TO OUR LIBRARY --------------------")

print("1. Student\n2. Faculty\n3. Administrator\n4. Exit")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("\t\t\t\t\t\t-------------------- WELCOME TO STUDENT PROTAL --------------------")
    print("1. Login")

    cho = int(input("Enter your choice: "))

    if cho == 1:
        login_student()
    else:
        print("Invalid Option\nProgram terminated")

elif choice == 2:
    print("\t\t\t\t\t\t-------------------- WELCOME TO FACULTY PROTAL --------------------")
    print("1. Login")

    cho = int(input("Enter your choice: "))

    if cho == 1:
        login_faculty()
    else:
        print("Invalid Option\nProgram terminated")

elif choice == 3:
    print("\t\t\t\t\t\t-------------------- WELCOME TO ADMIN PROTAL --------------------")
    print("1. Sign Up\n2. Login\n3. Add a new student\n4. Add a new faculty member")
    
    cho = int(input("Enter your choice: "))

    if cho == 1:
        signUp_admin()
    elif cho == 2:
        login_admin()
    elif cho == 3:
        signUp_student()
    elif cho == 4:
        signUp_faculty()
    else:
        print("Invalid Option\nProgram terminated")

elif choice == 4:
    exit()

else:
    print("Invalid Choice\nProgram Terminated")
