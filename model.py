

def write():
    pass


def delete(base, worker):
    base = base.split('\n')
    for i in base:
        if worker in i:
            # del base[i]
            base.remove(i)
    return base

def find(base, worker):
    base = base.split('\n')
    flag = True
    result = []
    for i in base:
        if worker in i:
            flag = False
            result.append(i)
    if flag:
       result.append('Работник не найден !')
    return result


def change():
    pass
