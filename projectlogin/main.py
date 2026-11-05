from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("400x450")
master.title("Login and Registration")

def open_registration_window():
    registration_window = Toplevel(master)
    registration_window.title("Registration")
    registration_window.geometry("300x350")

    Label(registration_window, text="This is the registration window").pack(pady=10)

Label(master, text="This is the main window of the login and registration system").pack(pady=10)
Button(master, text="Registration", command=open_registration_window).pack(pady=10)

def open_login_window():
    login_window = Toplevel(master)
    login_window.title("Login")
    login_window.geometry("300x350")

    Label(login_window, text="This is the login window").pack(pady=10)

Button(master, text="Login", command=open_login_window).pack(pady=10)

def open_exit_window():
    exit_window = Toplevel(master)
    exit_window.title("Exit")

Button(master, text="Exit", command=master.destroy).pack(pady=10)

master.mainloop()

def show_menu():
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("Registration\n")
        file.write("Login\n")
        file.write("Exit\n")

    while True:
        with open("data.txt", "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                print(f"{line_number}. {line.strip()}")
            
        try:
            user_choice = int(input("choose 1, 2 or 3: "))
        except ValueError:
            print("invalid! choose between 1, 2 or 3\n")
            continue

        if user_choice == 1:
            print("you want to get registrated?")
            user_register()
        elif user_choice == 2:
            print("oh you already have an account?")
            user_login()
        elif user_choice == 3:
            print("bye then!")
            break  
        else:
            print("invalid! choose between 1, 2 or 3")


def user_register():
    username = input("Enter your username: ")
    password = input("enter your password: ")

    # Using your exact validation method structure
    is_valid = True

    if len(username) < 3 or len(password) < 3:
        print("username and password must at least have 3 charcters")
        is_valid = False

    if len(username) > 25 or len(password) > 25:
        print("username and password can not be more than 25 charcters")
        is_valid = False

    if username.isdigit() or password.isdigit():
        print("username has to include symbols and letters. not only numbers")
        is_valid = False

    if username.isalpha() or password.isalpha():
        print("username has to include symbols and numbers. not only letters")
        is_valid = False

    if is_valid:
        print("the password and username are correct! you can now register!")
        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(f"{username},{password}\n")


def user_login():
    username = input("enter your username: ")
    password = input("enter your password: ")

    login_successful = False

    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                if "," in line:
                    stored_username, stored_password = line.strip().split(",")

                    if username == stored_username and password == stored_password:
                        login_successful = True
                        break
    except FileNotFoundError:
        print("no accounts found yet!\n")
        return

    if login_successful:
        print("welcome back!\n")
    else:
        print("maybe you got something wrong?")


show_menu()