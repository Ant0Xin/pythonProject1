from math import sqrt

a = int(input())
b = int(input())
c = input()

if c == '/' and (a == 0 or b == 0):
    print('На ноль делить нельзя!')
elif c == '/':
    print(a / b)
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '**':
    print(a ** b)
elif c == 'sqrt':
    print(sqrt(a), sqrt(b))
else:
    print('Неверная операция')
