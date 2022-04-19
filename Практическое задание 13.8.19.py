m = int(input('Количество билетов '))
s = 0
for i in range(m):
    age = int(input('Укажите возраст '))
if age < 18:
    s += 0
elif 18 <= age < 25:
    s += 990
else:
    s += 1390
if m > 3:
    f = 0.9
else:
    f = 1
print( s  * f  * m, ' рублей')



