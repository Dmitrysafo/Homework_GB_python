#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
  
  
   # *Пример:*
    
    #- 6 -> да
    #- 7 -> да
    #- 1 -> нет
a = int(input("Введите число"))
if 1 <= a <= 5:
   print("рабочий")
elif 5 <= a <= 7:
   print("выходной")
else:
   print("неправильно введены данные")

