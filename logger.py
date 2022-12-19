
def writer(worker):
    lst = list(worker.split(' '))
    with open('HomeWorkPython 16.12.22/base.csv', 'a') as f:
        f.write(f'{lst[0]};{lst[1]}\n')


def get_base():
    with open('HomeWorkPython 16.12.22/base.csv', 'r') as f:
        return f.read()


def rewriter(base):
    f = open('HomeWorkPython 16.12.22/base.csv', "w+")
    f.close()
    with open('HomeWorkPython 16.12.22/base.csv', 'a') as f:
        for i in base:
            x = ''.join(i)
            f.write(f'{x}\n') 
