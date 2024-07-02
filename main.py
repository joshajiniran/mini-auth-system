import auth
from home import show_instruction


if auth.MAINTENANCE_MODE:
    print("Application is under maintainance.\nPlease check back later.")
    exit()


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
