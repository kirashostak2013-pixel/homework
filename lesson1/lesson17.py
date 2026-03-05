#user_number1 = int(input("please write your firtst number "))
#user_number2 = int(input("please write your second number "))
#
#print(user_number1 / user_number2)

#try:
   # user_number1 = str(input("please write your first number "))
  #  user_number2 = str(input("please write your second number "))
 #   print(user_number1 / user_number2)
#except ZeroDivisionError:
   # print("do not do that again")

try:
    user_number1 = int(input("please write your first number "))
    user_number2 = int(input("write your second number "))
except ZeroDivisionError:
    print("do not do that please ")
except ValueError:
    print("jokes on you. this wont work")