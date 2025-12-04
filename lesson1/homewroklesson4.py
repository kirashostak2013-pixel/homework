user_password = str(input("write your password "))
user_login = str(input("enter your login "))

server_password = "hamilton1234"
server_login = "revolution67"

if server_password == user_password and server_login == user_login:
    print("welcome, you have logged in now ")
else:
    print("sorry you can't come in ")