# Introdução aos algoritmos

O estudo dos algoritmos é importante para a computação para que possamos programar softwares viáveis para cada situação e que realize tarefas com a mais alta performance.
Estudar algoritmos fornece para o programador, noção fundamentalmente pura da estrutura de dados de seu trabalho de forma a deixar os defeitos de programação mais visíveis e portanto, reparáveis.

Vamos começar compreendendo o que de fato, é um algoritmo:

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
Vamos analisar isto nos tópicos seguintes.

## Complexidade de espaço

Trata-se de quanto de espaço o algoritmo precisará para executar suas operações; isto inclui as variáveis existentes no mesmo. No caso de nosso exemplo, temos cinco variáveis contando com os argumentos da função ou a lista, portanto, a complexidade de espaço é equivalente a `4 + n`, sendo `n` os valores guardados na lista, afinal, a mesma guarda vários valores na mesma variável, que varia de acordo com a entrada.

## Complexidade de tempo

Uma maneira de calcular a complexidade de processamento seria encontrando alguma fórmula que dê o número exato de operações feitas pelo algoritmo.
O algoritmo empregado na função `InverterLista` possui 2 operações elementares em sua trajetória de execução e mais três outras que se repetem de acordo com o tamanho da lista que passamos de entrada. Matematicamente, podemos dizer que a quantidade de processamentos (a quantidade de operações contidas no nosso algoritmo) é o equivalente a `2 + 3(n/2)`, sendo `n/2` a quantidade de vezes que as três operações elementares do loop for em nosso algoritmo serão executadas. Observe, que tem relação de base direta com quanto tempo o algoritmo gasta de acordo com a entrada, pois independente do valor de entrada, a quantidade de etapas operacionais de nosso algoritmo sempre será a mesma, ou em outra forma de dizer, a base para calcular o tempo de processamento de qualquer tarefa para este algoritmo parte da mesma regra matemática, com independência de valores concretos.

## Referências

* Introduction to Algorithms por Thomas H. Cormen;
* [COMPLEXIDADE de ALGORITMOS I - Noção INTUITIVA](https://www.youtube.com/watch?v=KVlGx-9CuO4)
