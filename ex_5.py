# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве

import math


x1 = float(input("Введите x1 - "))
y1 = float(input("Введите y1 - "))
x2 = float(input("Введите x2 - "))
y2 = float(input("Введите y2 - "))
L = math.sqrt((x2-x1)**2+(y2-y1)**2)
print (round (L,2 )) 


#Подробнее – на otvet.ya.guru – https: // otvet.ya.guru/questions/5078927-python-napishite-programmu-kotoraya-vvodit-koordinaty-dvuh-tochek.html
