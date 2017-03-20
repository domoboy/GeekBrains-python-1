# lesson6-1, hard
import classes as cl


def res_pay(obj):
    '''
    Возвращает расчёт сотрудника
    '''
    cash = float(obj.get_card['cash'])
    norm = float(obj.get_card['norm'])
    worked = float(obj.get_card['worked'])
    norm_cash_h = cash / norm
    
    if norm == worked:
        obj.get_card['real_cash'] = cash

    if norm > worked:
        obj.get_card['real_cash'] = norm_cash_h * worked

    if norm < worked:
        obj.get_card['real_cash'] = cash + (worked - norm)*(norm_cash_h*2)

    return round(obj.get_card['real_cash'], 2)

workers = cl.parse_file('workers.txt', cl.Person_Card)
fact = cl.parse_file('hourse_of.txt', cl.Person_Work)

workers_tab = cl.join_tab(workers, fact)

print('Расчёт сотрудников:\n')
for worker in workers_tab:
    worker.get_card['real_cash'] = res_pay(worker)
    print('{0:<10}{1:<12}{2:<10}руб.'.format(worker.get_full_name['last_name'],
                                 worker.get_full_name['name'],
                                 worker.get_card['real_cash']))
    





