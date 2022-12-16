import csv


def writer(contact):

    try:
        with open('HomeWorkPython 16.12.22/base.csv', 'a') as f:
            
            # writer = csv.writer(f, delimiter=';')
            # writer.writerows([contact.split(' || ')])
            
            f.write(f'{contact}\n')
            
    except FileNotFoundError:
        with open('HomeWorkPython 16.12.22/base.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])

def get_base():
    with open('HomeWorkPython 16.12.22/base.csv', 'r') as f:
        return f.read()

def rewriter(base):
    f = open('HomeWorkPython 16.12.22/base.csv', "w+")
    f.close()
    for i in base:
        with open('HomeWorkPython 16.12.22/base.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([i.split(' || ')])

# print(type(get_base()))

# writer('Павел 7777')
