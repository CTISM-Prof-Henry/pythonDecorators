import random


def aumenta_um(func):
    def wrapper(param):
        res = func(param)
        if res is True:
            return 'parabéns! Você adivinhou o número!'
        return 'que pena! Você errou!'

    return wrapper


@aumenta_um
def diga_um_numero(numero):
    numero_correto = random.randint(0, 10)
    acertou = numero == numero_correto
    return acertou


def main():
    print(diga_um_numero(7))


if __name__ == '__main__':
    main()
