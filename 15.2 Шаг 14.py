def print_products(*args):
    elems = [arg for arg in args]
    lem = []
    a = ')'
    for elem in elems:
        if isinstance(elem, str) and elem != '':
            lem.append(elem)
            for i in lem:
                b = str(lem.index(i))
                c = b+a
                print(c, i)  # из-за компанды принт после печати списка появляется None
        else:
            return 'Нет продуктов'