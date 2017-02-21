#lesson3, hard

#1------------------------------

def fract(num):
    '''
    приведение целой и дробной части
    '''
    if num[0] and num[2]:
        num[1] = (num[0] * num[2] + num[1] if num[0] > 0 else
                  num[0] * num[2] - num[1])
        num[0] = False
    
    return [n for n in num if n]
 
def equfract(*n):
    '''
    вычисление дробей
    '''
    if len(n) == 3:
        sign = n[len(n)-1]
        num1 = fract([n[0]['int'], n[0]['num'], n[0]['dem']])
        num2 = fract([n[1]['int'], n[1]['num'], n[1]['dem']])
        print(num1, num2)

        if len(num1) == len(num2):
           res = list(zip(num1, num2))
           print(res)

                  
    if len(n) == 1:
        num = fract([n[0]['int'], n[0]['num'], n[0]['dem']])
        print(num)

def discharge(li):
    '''
    выделение числителя, знаменателя
    и целой части
    '''
    #int: целая часть
    #num: числитель
    #dem: знаменатель
    
    num = {'int': False, 'num': False, 'dem': False}

    if len(li) == 1:
        num['int'] = int(li[0])

    if len(li) == 2 and ~li[1].find('/'):
        num['int'] = int(li[0])
        num['num'] = int(li[1].split('/')[0])
        num['dem'] = int(li[1].split('/')[1])

    if len(li) == 2 and li[1].isdigit():
        num['num'] = int(li[0])
        num['dem'] = int(li[1])

    return num

def formatin():
    '''
    форматирование входной строки
    '''
    usr_in = '2 + 2'
    usr_in = usr_in.strip()

    is_one_operand = False
    sign = False

    plus = usr_in.find(' + ')
    minus = usr_in.find(' - ')

    if not ~minus and not ~plus:
        is_one_operand = True
    else:
        sign = usr_in[minus+1] if ~minus else usr_in[plus+1]
        
    if is_one_operand:
        oper = (usr_in.split(' ') if ~usr_in.find(' ') else
                usr_in.split('/'))
        num = discharge(oper)
        return equfract(num) 
    else:
        opers = usr_in.split(' ' + sign + ' ')
        oper1 = (opers[0].split(' ') if ~opers[0].find(' ') else
                 opers[0].split('/'))
        oper2 = (opers[1].split(' ') if ~opers[1].find(' ') else
                 opers[1].split('/'))
        num1 = discharge(oper1)
        num2 = discharge(oper2)
        return equfract(num1, num2, sign)    

formatin()

