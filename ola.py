def caixa_alta(func):
    def wrapper():
        res = func()
        return res.upper()

    return wrapper


@caixa_alta
def diga_ola():
    return 'olá mundo!'


def main():
    print(diga_ola())


if __name__ == '__main__':
    main()
