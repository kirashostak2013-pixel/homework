with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Регистрация\n")
    file.write("Вход\n")
    file.write("Завершить программу\n")
    
with open("data.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        print(f"{line_number}.{line.strip()}")
    
user_choice = int(input("choose 1, 2 or 3 "))

if user_choice == 1:
    print("you want to get registrated?")
if user_choice == 2:
    print("oh you already have an account?")
else:
    print("bye then!")
    