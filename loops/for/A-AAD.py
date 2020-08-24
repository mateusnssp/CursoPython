a, b = 0, 1
for i in list(range(11)):
    print(a, end = ' ')
    a, b = b, a + b
