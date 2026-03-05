user = {
    "name": "Kira",
    "age": 11,
    "city": "Mora"
}

#print(user["name"])     
user["age"] = 12         
#user["email"] = "a@b.com"
print(user)

#user.keys()      # все ключи
#user.values()
print(user.values())    # все значения
#user.items()     # пары (ключ, значение)
#print(user.items)
user.get("age")  # без ошибки, если ключа нет (вернёт None)
print(user.get("abrakadabra"))