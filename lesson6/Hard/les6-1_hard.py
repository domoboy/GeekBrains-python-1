# lesson6-1, hard
import classes as cls

def string_result(res):
    '''
    Формат вывода результата
    '''
    return '{0:<16} {1} руб.'.format(res.get('name'), res.get('real_cash'))

def res_pay(obj):
    '''
    Возвращает словарь с именем и расчётом
    по сотруднику
    '''
    cash = float(obj.get_card['cash'])  # зарплата
    norm = float(obj.get_card['norm'])  # норма
    worked = float(obj.get_card['worked'])  # отработано
    norm_cash_h = cash / norm  # норма в час
    
    obj.get_card['real_cash'] = round(norm_cash_h * worked if
                                      norm > worked else
                                      cash + (worked - norm)*(norm_cash_h*2), 2)

    return {'name': obj.get_full_name,
            'real_cash': obj.get_real_cash()
            }

workers = cls.parse_file('workers.txt', cls.Person_Card)
fact = cls.parse_file('hourse_of.txt', cls.Person_Work)
workers_cash = list(map(res_pay, cls.join_tab(workers, fact)))

print('РАСЧЁТ СОТРУДНИКОВ:')
print('\n'.join(list(map(string_result, workers_cash))))

    





