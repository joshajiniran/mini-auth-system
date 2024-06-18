user_base = [
    {"username": "josh", "password": "12345678"},
    {"username": "jane", "password": "87892434"},
    {"username": "james", "password": "something"},
]


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

    # TODO -> prevent duplicate username registration. Username already taken.

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

# TODO -> system should allow users to keep attempting options until one of the 3 is entered.
# hint: use a while loop
try:
    option: int = int(
        input("Press the corresponding number (1, 2 or 3) to interact with system: ")
    )
except ValueError:
    print("Invalid input, please enter a number not string")
    exit(1)

if option == 1:
    login()
elif option == 2:
    register()
elif option == 3:
    print("Closing the application...")
    exit(0)
else:
    print("Invalid input. Please enter one of the options (1, 2 or 3)")
    exit(-1)
