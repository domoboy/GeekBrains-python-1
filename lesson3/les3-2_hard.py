# lesson3-2, hard


def tolist(f_path):
    with open(f_path, encoding='utf-8') as lister:
        li = [elems for elems in lister]
        li = [[e.strip() for e in elem if len(e)] for
               elem in [elems.split(' ') for elems in li]]
        return li


persons = tolist('workers.txt')
hourse = tolist('hourse_of.txt')

print(persons)
print(hourse)


