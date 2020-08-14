
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador += contador
    contador += 1

else:         #Else vai agir quando expressão do while se tornar falsa.
    print('Cheguei no else')
