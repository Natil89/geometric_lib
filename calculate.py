figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    if not all(isinstance(s, (int, float)) for s in size):
        raise TypeError("All size values must be numeric")

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size_input = input("Input figure sizes separated by space, 1 for circle and square\n")
        size = list(map(int, size_input.split(' ')))

    calc(fig, func, size)
