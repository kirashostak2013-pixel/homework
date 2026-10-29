#with open("notes.txt", "w", encoding="utf-8") as file:
    #file.write("Привет, Кира!\n")
   # file.write("Изучаем Python.\n")

#with open("notes.txt", "r", encoding="utf-8") as file:
 #   text = file.read()

#print(text)

#with open("notes.txt", "a", encoding="utf-8") as file:
#    file.write("Новая строка.\n")

#with open("notes.txt", "r",  encoding="utf-8") as file:
    #for line in file:
        #print(line.rstrip("\n"))


#with open("notes.txt", "r", encoding="utf-8") as file:
#    for _ in range(2):
        #line = file.readline()
       # if line == "":
        #    break
       # print(line.rstrip("\n"))

#with open("notes.txt", "r", encoding="utf-8") as file:
 #   text = file.read()

#text = text.replace("Python", "JavaScript")
#
#with open("notes.txt", "w", encoding="utf-8") as file:
  #  file.write(text)

#with open("hadestown.txt", "w", encoding="utf-8") as file:
    #file.write ("Orpheussss!\n")
   # file.write("waiiittt for meee\n")
  #  file.write("I'm coominnng\n")


with open("hadestown.txt", "w", encoding="utf-8") as file:
    file.write ("Orpheussss!\n")
    file.write("waiiittt for meee\n")
    file.write("I'm coominnng\n")

with open("hadestown.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"{line_number}. {line.strip()}")