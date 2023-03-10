# не получается избавиться от None
def info_kwargs(**kwargs):
    for k,v in kwargs.items():
        sign = ': '
        print(k + sign + str(v))