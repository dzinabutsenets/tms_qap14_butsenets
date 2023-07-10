#  HOMEWORK3
#  1.2 Определить переменные всех типов и выведете их на экран
print(type(int(111)))
print(type(float(0.452)))
print(type(str("RIP")))
print(type(list([90, 56, "street"])))
c = {"apple": 1, "orange": 2}
print(type(dict(c)))
b = {"how", "know"}
print(type(set(b)))
print(type(tuple("111")))
a = True
print(type(bool(a)))
#  1.3 Найти значение выражений
x1 = (17/(2*3))+2
x2 = 2+(17/(2*3))
x3 = 19%4+(15/(2*3))
x4 = (15+6)-(10*4)
x5 = (17/2)%(2*(3**3))
print(x1, x2, x3, x4, x5)
x6 = 17/2*3+2
print(x6)
#  1.4 Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран
# Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран
var1 = 90
var2 = 91
var3 = 89
print(var1 + var2 + var3)
var4 = (var1 + var2 + var3)/3
print(var4)

#1
a = int(-1.6)
print(a)

b = int(2.99)
print (b)

#2
string = 'www.my_site.com#about'
replace_symbol = string.replace("#", "/")
print(replace_symbol)

#3
str1 = "stroka"
str2 = "ing"
print(str1+str2)

#4
l = ["Ivanou", "Ivan"]
list.reverse(l)
print(" ".join(l))

#5
str1 = " any awesome text "
print(str1.strip())

#6
students_amount = {"1а": 30, "2а": 28, "3а": 26, "4а": 25, "5а": 19, "6а": 24, "7а": 28, "8а": 31, "9а": 29, "10а": 22}
for c, a in students_amount.items():
    print(c, a)

#7
list = [67, 76, 99]
print(list[1])

#8
str1 = "star"
str2 = "starman"
if str1 in str2:
    print(True)

#9
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:16:3]) #nesgt