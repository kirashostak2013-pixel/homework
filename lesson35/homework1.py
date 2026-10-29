with open("Epic.txt", "w", encoding="utf-8") as file:
    file.write ("Waiiiiting\n")
    file.write("this life is amazing when you greet it with open arms!\n")
    file.write("you all know I'm a fan of catchy songs!\n")


#1
with open("Epic.txt", "a", encoding="utf-8") as file:
        file.write("I wanna be legendary\n")

#2

keyword = "legendary"
legendary = "search results for"

with open("Epic.txt", "r", encoding="utf-8") as file:
      print(f"--- {legendary} '{keyword}' ---")

      for line in file:
            if keyword in line:
                print(line.strip())

#3

with open("Epic.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()
      total_entries = len(lines)
print(f"total entries: {total_entries}")



#4

