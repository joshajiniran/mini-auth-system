from getpass import getpass
import json


def login() -> None:
    print("Login")
    print("======================")
    username: str = input("Enter your username: ")
    password: str = getpass("Enter your password: ")

    with open("user_db.txt", "r", encoding="utf-8") as file:
        users = [json.loads(line.strip()) for line in file]

    for user in users:
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

    with open("user_db.txt", "a+", encoding="utf-8") as file:
        json.dump({"username": username, "password": password}, file)
        file.write("\n")

    print("Registration successful.")


print("Welcome to Auth System\n=========================")


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
