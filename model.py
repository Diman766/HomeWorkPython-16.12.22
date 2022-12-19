
def delete(base, worker):
    worker = worker.split(' ')
    worker = ';'.join(worker)
    base = base.split('\n')
    for i in base:
        if worker in i:
            base.remove(i)
    del base[-1]
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


def change(worker):
    lst = ''.join(worker)
    x = lst.split(';')
    x = ' '.join(x)
    lst = list(lst.split(';'))
    lst_show = list(enumerate(lst, start=1))
    print(lst_show)
    id = int(input('Введите номер изменяемой области  '))
    change = input('Введите новое значение  ')
    lst[id - 1] = change
    lst = ' '.join(lst)
    return lst, x
