#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#even_number = []
#odd_number = []

#for i in range(len(numbers)):
   # if numbers[i] % 2 == 0:
  #      even_number.append(numbers[i])
 #   else:
#        odd_number.append(numbers[i])
#print(even_number)
#print(odd_number)    

numbers = [-1, 3, -8, -4, 6, 9, -10, 7, 2, -3]

result = []
for i in range(len(numbers)):
    if numbers[i] < 0:
        result.append(0)
    else:
        result.append(1)
print(result)