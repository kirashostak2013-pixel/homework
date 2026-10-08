text = "hello my balance 750 and 67 or 14589 USD."

def search_number(text):
    result_arr = []

    for word in text.split():
        if word.isdigit():
            result_arr.append(int(word))

    largest = max(result_arr)
    result = largest

    for num in result_arr:
        if num != largest:
            result = result / num

    return result

print(search_number(text))