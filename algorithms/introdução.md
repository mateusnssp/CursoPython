

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

O algoritmo empregado na função `InverterLista` possui 2 operações elementares em sua trajetória de execução, e três outras que se repetem de acordo com o tamanho da lista que passamos de entrada. Matematicamente, podemos dizer que a quantidade de processamentos (a quantidade de operações contidas no nosso algoritmo) é o equivalente a <img src="http://www.sciweavers.org/tex2img.php?eq=2%20%2B%203%20%5Ccdot%20%5Cfrac%7Bn%7D%7B2%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" width="50"> .

## Referências

https://www.youtube.com/watch?v=KVlGx-9CuO4
