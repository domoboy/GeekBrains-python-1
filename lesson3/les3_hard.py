#lesson 3, hard

#1------------------------

def equfract():
    #user_input = input('Введите выражение: ')

    eq = '-3/5 + 6 7/8'

    ones_oper = False
    sign = False

    int_part, int_part2 = False, False
    num_part, num_part2 = False, False
    dem_part, dem_part2 = False, False

    plus = eq.find(' + ')
    minus = eq.find(' - ')

    if plus != -1:
        sign = (eq)[plus+1]
    elif minus != -1:
        sign = (eq)[minus+1]

    if sign:
        operands = eq.split(sign)    
    else:
        operands = eq.split(' ')
        ones_oper = True

    operands = [oper.strip() for oper in operands]

    if len(operands) > 2:
        print('Ошибка при вводе: лишний операнд\n%s'%(operands))
        return

    if ones_oper:
        int_part = int(operands[0]) if len(operands) == 2 else 1

        num_part = (int(operands[1].split('/')[0]) if len(operands) == 2 else
                    int(operands[0].split('/')[0]))

        dem_part = (int(operands[1].split('/')[1]) if len(operands) == 2 else
                    int(operands[0].split('/')[1]))
        
        
    
    print('Целая часть:%s Числитель:%s Знаменатель:%s'%(int_part, num_part, dem_part))
    print('%s Знак %s'%(operands, sign))

equfract()
