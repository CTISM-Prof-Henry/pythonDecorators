
def aumenta_um(func):
    def wrapper(p1):
        res = func(p1)
        return res + 1

    return wrapper


@aumenta_um
def soma(a, b):
    return a + b


def main():
    print(soma(3, 7))


if __name__ == '__main__':
    main()
