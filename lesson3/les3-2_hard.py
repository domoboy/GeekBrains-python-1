# lesson3-2, hard


def tolist(path):
    '''
    Возвращает массив строк из файла path
    '''
    with open(path, encoding='UTF-8') as lister:
        nlist = [elems for elems in lister]
        nlist = [[el.strip() for el in elem if len(el)] for
                 elem in [elems.split(' ') for elems in nlist]]
        return nlist


def couple(header, values):
    '''
    Возвращает массив словарей с ключами из
    header и соответсвующими им значениями из
    values
    '''
    nlist = [list(zip(header, value)) for value in values]
    nlist = [{elem[0]: elem[1] for elem in elems} for elems in nlist]
    return nlist


def merge(file1, file2):
    '''
    Возвращает общую таблицу из file1 и file2
    в виде списка из словарей по каждому сотруднику
    '''
    persons_list = tolist(file1)  # Создание списка строк из табл.№1
    houres_list = tolist(file2)  # Создание списка строк из табл.№2
    header_p = persons_list.pop(0)  # Выделение заголовка из табл.№1
    header_h = houres_list.pop(0)  # Выделение заголовка из табл.№2
    '''
    Создание пары заголовок - значение для каждого сотрудника
    в каждой таблице
    '''
    personal = couple(header_p, persons_list)
    hourse = couple(header_h, houres_list)
    '''
    Слияние таблиц
    '''
    for el in personal:
        for e in hourse:
            if (el['Фамилия'] == e['Фамилия'] and
               el['Имя'] == e['Имя']):
                el.update(e)

    return personal


def calc_pay(tabl):
    '''
    Расчёт зарплаты
    '''
    for person in tabl:
        pay = int(person['Зарплата'])
        h_need = int(person['Норма_часов'])
        h_fact = int(person['Отработано_часов'])
        h_pay = int(pay / h_need)

        if h_fact == h_need:
            person['Расчёт'] = '%s' % (pay)
        elif h_fact > h_need:
            person['Расчёт'] = '%s' % (pay + (h_fact - h_need) * (h_pay*2))
        else:
            person['Расчёт'] = '%s' % (h_pay * h_fact)

    return tabl


personal = calc_pay(merge('workers.txt', 'hourse_of.txt'))

with open('calc_pay.txt', 'w', encoding='UTF-8') as pay_list:
    header = []
    for key in personal[0].keys():
        if key == 'Фамилия':
            header.insert(0, key)
        if key == 'Имя':
            header.insert(1, key)
        if key == 'Расчёт':
            header.insert(2, key)
    header = '%s    %s    %s\n' % (header[0], header[1], header[2])
    body = '\n'.join(['%s   %s' %
                      (pers['Фамилия'] + ' ' + pers['Имя'],
                       pers['Расчёт']) for pers in personal])

    print(header + body)

    pay_list.write(header + body)
