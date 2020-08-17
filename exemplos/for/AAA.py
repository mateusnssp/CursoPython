import random
"""
range(start = 0 , stop , step = 1)
"""
l = []
for num in range (11):
    l.append(num)
print(l)

## alternativa mais complexa:
l, num = [], 0
while num < 11:
    l.append(num)
    num += 1
print(l)






lista_num_pares = []
for num in l:
    if num % 2 == 0:
        lista_num_pares.append(num)

print(lista_num_pares)




