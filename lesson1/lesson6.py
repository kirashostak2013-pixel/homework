number = [1,2,3,4,5,6,7,8,9,10]

#print(number[6])

#for i in range(len(number)):
 #   print(number[i])

#for i in range(len(number)):
    #if number[i] % 2 == 0:
     #   print(number[i])

result = 0
for i in range(len(number)):
    if number[i] % 2 == 0:
        result += number[i]
print(result)