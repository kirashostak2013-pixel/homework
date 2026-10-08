def greet(name):
    return f"hello, {name}"
print(greet("John"))


def add(a, b):
    return a + b
print(add(3, 5))


def positive(num):
    if num > 0:
        return True
    else:
        return False
print(positive(8))



def bigger(a, b):
    if b > a:
        return b
    else:
        return a
        
print(bigger(4, 7))



def count_letters(word):
    return len(word)
    
print(count_letters("Hello"))


