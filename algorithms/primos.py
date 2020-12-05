
# Solução do Diego
def fun1(n):
    if n > 1:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True
    return False
# (n - 1) - 2

print(fun1(997))

# Solução da Júlia

import math
def fun2(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True
    return False
# (int(sqrt(n)) - 2)

print(f'Júlia: {fun2(997)}')



print(list(range(2, 4 - 1)))
