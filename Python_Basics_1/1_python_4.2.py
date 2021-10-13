#4.2
odds = "Don't panic! Now_is_the_time."
olist = list(odds)
print(odds)
print(odds[8:])

for i in range(4):
    olist.pop(13)
new_odds = ''.join(olist)
print(new_odds)  # Removed 4 fom the center

print(odds[::3])
print(odds[::-1])
