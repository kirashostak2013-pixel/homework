def greet(name):
    return ("hello " + name)
print(greet("Sarah "))


def multiply(a, b):
    return a * b
print(multiply(4, 7))


def add(a, b):
    return (a + b)
    add (4, 7)
print(add(4, 7))



def even_or_odd(number):
    if number % 2 == 0:
        return "its even"
    else:
        return "its odd"
        
user_number = int(input("write your number "))
print(even_or_odd(user_number))



def bigger(a, b):
    if a > b:
        return f"{a} is bigger"
    else:
        return f"{b} is bigger"
print(bigger(4, 6))



def double(a):
    return a * 2
print(double(5))



def first_letter(word):
    return word[0]
print(first_letter("cat"))



def last_letter(word):
    return word[5]
print(last_letter("python"))



def make_upper(word):
    return word.upper()
print(make_upper("hello"))


def add_three(a, b, c):
    return a + b + c
print(add_three(4, 5, 8))
