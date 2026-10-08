# upper()
text = "hello"
print(text.upper())  # HELLO


# lower()
text = "HELLO"
print(text.lower())  # hello


# capitalize()
text = "hello world"
print(text.capitalize())  # Hello world


# title()
text = "hello world"
print(text.title())  # Hello World


# strip()
text = "   hello   "
print(text.strip())  # hello


# replace()
text = "I like Java"
print(text.replace("Java", "Python"))
# I like Python


# find()
text = "Hello Python"
print(text.find("Python"))
# 6


# index()
text = "Hello Python"
print(text.index("Python"))
# 6


# count()
text = "banana"
print(text.count("a"))
# 3


# split()
text = "Python Java C++"
print(text.split())
# ['Python', 'Java', 'C++']


# join()
languages = ["Python", "Java", "C++"]
print(" ".join(languages))
# Python Java C++


# startswith()
text = "Hello Python"
print(text.startswith("Hello"))
# True


# endswith()
filename = "main.py"
print(filename.endswith(".py"))
# True


# isdigit()
text = "12345"
print(text.isdigit())
# True


# isalpha()
text = "Hello"
print(text.isalpha())
# True


# isalnum()
text = "Hello123"
print(text.isalnum())
# True