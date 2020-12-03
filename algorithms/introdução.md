

# Introdução aos algoritmos

> Um algoritmo é um procedimento computacional que leva algum valor, ou conjunto de valores, como entrada e retorna algum valor, ou conjunto de valores, como resultado. Um algoritmo é, portanto, uma sequência de etapas computacionais que transformam a entrada na saída.

Por exemplo, podemos criar um algoritmo que inverte a sequência de uma lista:

```
def InverterLista(lista):
    tamanhoDaLista = len(lista)
    metadeDoTamanhoDaLista = tamanhoDaLista//2
    for item in range(metadeDoTamanhoDaLista):
        aux = lista[item]
        lista[item] = lista[(tamanhoDaLista - 1) - item]
        lista[(tamanhoDaLista - 1) - item] = aux
    return lista

```

O algoritmo empregado na função `InverterLista` possui 2 operações elementares em sua trajetória de execução, e três outras que se repetem de acordo com o tamanho da lista que passamos de entrada. Matematicamente, podemos dizer que a quantidade de processamentos (a quantidade de operações contidas no nosso algoritmo) é o equivalente a `2 + 3(n/2)`, sendo `n/2` a quantidade de vezes que as três operações elementares do loop for em nosso algoritmo serão executadas, que chamamos de complexidade de processamento. Observe, que tem relação direta com quanto tempo o algoritmo gasta de acordo com a entrada, pois independente do valor de entrada, a quantidade de etapas operacionais de nosso algoritmo sempre será a mesma.

## Referências

https://www.youtube.com/watch?v=KVlGx-9CuO4
