# Playing around with decorators
user_name = "john".lower()
user_password = "qweasdzxc".lower()

def log_in(func):

    def ask_info():
        while True:
            name = input("Enter your name: ").lower()
            password = input("Enter your password: ").lower()

            if name == user_name and password == user_password:
                return func()
            else:
                print("Invalid password and/or username")

    return ask_info


@log_in
def welcome():
    print(f"Welcome {user_name.capitalize()}")

welcome()

        