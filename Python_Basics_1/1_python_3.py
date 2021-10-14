#4.3
a = 10
b = 5

"""Логические выражения с AND"""
z = a > b and (b * 2 == a)
d = a + b == 15 and a // 2 == b
print(z, d)  # Истина
z = a < b and a == b
d = a // b >= b and a + b != 15
print(z, d)  # Ложь

"""Логические выражения с OR"""

z = a > b or b * 4 == a
d = a * b == 15 or a // 2 == b
print(z, d)  # Истина
z = a < b or a == b
d = a // b >= b or a + b - a != 5
print(z, d)  # Ложь

"""
Попробуйте использовать
в сложных логических выражениях
работу с переменными строкового типа"""

s = ['github', 'cat', 'apple', 'hub', 'engineer', 'pornhub']
z = 'cat' in s
y = 'hub' == 'cat'
d = 'porn' not in s
p = 'hub' in ('github' and 'pornhub' or 'engineer')
x = 'github' >= 'pornhub'
print(z, y, d, p, x)


