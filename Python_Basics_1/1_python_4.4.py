#4.4
test_tring = "Hello world!"
print(test_tring.index('w'))
print(test_tring.count('l'))
print('Hello' in test_tring)
print('qew' in test_tring)

#проверка последних 3х индексов
ltt = list(test_tring)
s = ltt[-3]+ltt[-2]+ltt[-1]
print(s)
print('qew' == s)

