#grades = [5, 3, 4, 5, 2, 5, 4]
#count_of_5=grades.count(5)
#print(count_of_5)

#print(grades.index(2))

#grades.sort()
#print(grades)

#data = [0, 1, 0, 2, 3, 0, 4]

#for i in data:
  # if i == 0:
 #     data.remove(i)
#print(data)
#lenght = len(data)
#print(lenght)

#numbers = [1, 2, 3, 2, 4, 2, 5]

#numbers.remove(2)
#print(numbers)

#ast_number = numbers.pop()

#print(numbers)

#user_input = input("enter the numbers with space ")
#list = [int(num) for num in user_input.split()]
#print(list)
#list_2 = list[:]
#list_2.reverse()
#print(list_2)

#group_1 = ["Anna", "Bogdan", "Kate"]
#group_2 = ["Masha", "Sergey"]

#print(group_1 + group_2)
#result = group_1 + group_2

#result.append("Daniel")
#print(result)

#result.sort()
#print(result)

Products = []
while True:
    product_name = input(str("enter your items or no item"))
    if product_name.lower() == (' '):
        break
Products.append(product_name)
print(Products)
   