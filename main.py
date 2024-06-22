from getpass import getpass

user_base = [
    {"username": "josh", "password": "12345678"},
    {"username": "jane", "password": "87892434"},
    {"username": "james", "password": "something"},
]


def login() -> None:
    print("Login")
    print("======================")
    username: str = input("Enter your username: ")
    password: str = getpass("Enter your password: ")

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
    password = getpass("Enter your password: ")
    confirm_password = getpass("Confirm your password: ")

    # TODO -> prevent duplicate username registration. Username already taken.

    if password != confirm_password:
        print("Password do not match")
        return

    user_base.append({"username": username, "password": password})
    print("Registration successful.")

    print(user_base)


print("Welcome to Auth System")
print("======================")

print("1. Register")
print("2. Login")
print("3. Exit")

while True:
    option = input(
        "Press the corresponding number (1, 2 or 3) to interact with system: "
    )

    if option == "1":
        register()
    elif option == "2":
        login()
    elif option == "3":
        print("Closing the application...")
        break
    else:
        print("Invalid input. Please enter one of the options (1, 2 or 3)")
