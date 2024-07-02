import auth
from home import show_instruction

<<<<<<< HEAD
if auth.MAINTENANCE_MODE:
    print("Application is under maintainance.\nPlease check back later.")
    exit()
=======

def login() -> None:
    print("Login")
    print("======================")
    username: str = input("Enter your username: ")
    password: str = input("Enter your password: ")

    for user in user_base:
        if username == user["username"]:
            if password == user["password"]:
                print("Logged in successfully.")
                return
            else:
                print("Invalid password")
                return

    print("Invalid username")


def register() -> None:
    print("Register")
    print("======================")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    # Check if the username is already taken
    for user in user_base:
        if username == user["username"]:
            print("Username already taken")
            return

    if password != confirm_password:
        print("Password do not match")
        return

    user_base.append({"username": username, "password": password})

    print(user_base)


print("Welcome to Auth System")
print("======================")

print("1. Login")
print("2. Register")
print("3. Exit")
>>>>>>> 4d2ee8a (duplicate-registration-fixed)

while True:
    show_instruction()

    option = input(
        "Press the corresponding number (1, 2 or 3) to interact with system: "
    )

    if option == "1":
        auth.register()
    elif option == "2":
        auth.login()
    elif option == "3":
        print("\nClosing the application...")
        break
    else:
        print("\nInvalid input. Please enter one of the options (1, 2 or 3)")
