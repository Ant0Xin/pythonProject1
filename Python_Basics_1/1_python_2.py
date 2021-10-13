school = {'1a': 29, # расформировать
          '1b': 25, # +2
          '1c': 25, # +2
          '2a': 21, # +6 (одарённые)
          '2b': 25, # +2 (одарённые)
          '2c': 30, 
          '2d': 32, 
          '3a': 28,
          '3b': 24,
          '3c': 27}
print(school['2d'])
school['1i'] = 22   # +5
school['1z'] = 15   # +12
print(school)
school['1i'] += 5
school['1z'] += 12
school['1b'] += 2
school['1c'] += 2
school['2a'] += 6 
school['2b'] += 2
del school['1a']
print(school)


           
