#3.     
#   *Пример:* 
#   - x=34; y=-30 -> 4
#  - x=2; y=4-> 1
# - x=-34; y=-30 -> 
x = int(input("Введите координат x "))
y = int(input("Введите координат y "))
if (x > 0) and (y > 0):
    print("I четверть")
elif(x < 0) and (y > 0):
    print("II четверть")
elif(x < 0) and (y < 0):
    print("III четверть")
elif (x > 0) and (y < 0):
    print("IV четверть") 
else:
    print("точка лежит на оси")      

            
               