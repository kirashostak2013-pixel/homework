import random


def get_user_name():
    user_name = input("write your name ").strip()
    return user_name

def get_random_animal():
    animals = ["tiger", "wolf", "fox", "kittyeeahh", "dog", "panther", "lion", "otter"]
    return random.choice(animals)

def get_random_adjectives():
    adjectives = ["star", "moon", "cloud", "sun", "thunder", "pie", "tail", "banana", "avocado"]
    return random.choice(adjectives)

def get_random_numbers():
    return str(random.randint(1, 99))

def build_nickname(name, animal, adjective, number):
    return f"{name}_{animal}_{adjective}{number}"

def main():
    name = get_user_name()
    animal = get_random_animal()
    adjective = get_random_adjectives()
    number = get_random_numbers()

    nickname = build_nickname(name, animal, adjective, number)
    return nickname 

nickname = main()
print(nickname)

main()