# Decorators

Decorators (decoradores, em inglês) são um recurso da linguagem de programação Python. Eles permitem que o comportamento
de uma função `a` seja modificado por uma outra função `b`, sem que para isto seja necessário modificar a função `a`.

Vamos supor, por exemplo, que exista uma função da seguinte forma:

```python
def diga_ola():
    return 'olá mundo!'
```

Agora vamos supor que quiséssemos que o texto dessa função saísse todo em letras maiúsculas. Da maneira tradicional,
seria necessário modificar a função da seguinte forma:

```python
def diga_ola():
    return 'olá mundo!'.upper()
```

Porém, existe uma maneira mais elegante de fazer isso, que **ainda** não usa decorators. Poderíamos definir uma função
`caixa_alta`, que pega qualquer texto que ela recebe, e retorna o texto recebido em caixa alta:

```python
def caixa_alta(texto):
    return texto.upper()
```

E então poderíamos usar esta função da seguinte maneira:

```bash
>>> caixa_alta(diga_ola())
>>> 'OLÁ MUNDO!'
```

Isso ainda **não utiliza** decorators. Para utilizarmos decorators, teríamos que fazer as seguintes modificações 
(segure-se na sua cadeira, vai ficar complicado bem rápido agora):

```python
def caixa_alta(func):
    def wrapper():
        res = func()
        return res.upper()

    return wrapper

@caixa_alta
def diga_ola():
    return 'olá mundo!'
```

`caixa_alta` agora recebe uma **função** como parâmetro, e ela **opera sobre esta função**. A maneira como ela está 
operando é definida dentro da função `wrapper`; e, depois que `caixa_alta` termina de definir como ela quer operar, ela
**retorna o conjunto de operações como resposta**.

Dessa forma, qualquer função que queira implementar o conjunto de operações definidos por `caixa_alta` pode fazê-lo 
utilizando o decorador `@caixa_alta`, que é exatamente o que `diga_ola` está fazendo agora.

Perceba que `diga_ola` é uma função que não recebe parâmetro nenhum; da mesma maneira, `wrapper` não recebe nenhum parâmetro.

## Exercícios

1. Olhe o código-fonte do arquivo [decorators/exemplo_1.py](decorators/exemplo_1.py). Contemple.
2. Olhe o código-fonte do arquivo [decorators/exemplo_2.py](decorators/exemplo_2.py). Ele não está funcionando! Corrija
   este código-fonte de forma que ele execute corretamente.
   1. Olhe a ausência de código-fonte do arquivo [decorators/exemplo_3.py](decorators/exemplo_3.py). Faça o seguinte neste
      arquivo:
      * Implemente uma função de nome `diz_abobrinha`, que deve retornar o seguinte: `o rato roeu a roupa do rei de roma`
      * Implemente uma função `capitaliza`, que deve receber uma função como parâmetro, e operar sobre ela; `capitaliza` 
        deve fazer com que cada palavra da função que ela recebeu tenha sua primeira letra maiúscula
      * Decore `diz_abobrinha` com `capitaliza`
      * A saída esperada desse arquivo deve ser o seguinte:
        ```bash
        >>> print(diz_abobrinha())
        >>> 'O Rato Roeu A Roupa Do Rei De Roma'
        ```