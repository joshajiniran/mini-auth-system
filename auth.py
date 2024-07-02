from getpass import getpass
import json


MAINTENANCE_MODE = False


def login() -> None:
    print("======================\nLogin\n======================")
    username: str = input("Enter your username: ")
    password: str = getpass("Enter your password: ")

    with open("user_db.txt", "r", encoding="utf-8") as file:
        users = [json.loads(line.strip()) for line in file]

    for user in users:
        if username == user["username"]:
            if password == user["password"]:
                print("\nLogged in successfully.")
                return
            else:
                print("\nInvalid password")
                return

    print("\nInvalid username")


def register() -> None:
    print("======================\nRegister\n======================")

    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    confirm_password = getpass("Confirm your password: ")

    if password != confirm_password:
        print("\nPassword do not match")
        return

    with open("user_db.txt", "a+", encoding="utf-8") as file:
        users = [json.loads(line.strip()) for line in file]
        # Check if the username is already taken
        for user in users:
            if username == user["username"]:
                print("Username already taken")
                return

        json.dump({"username": username, "password": password}, file)
        file.write("\n")

        print("\nRegistration successful.")
