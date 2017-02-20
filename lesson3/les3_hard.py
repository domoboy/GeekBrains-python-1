#lesson 3, hard

#1------------------------

def equfract():
    #user_input = input('Введите выражение: ')

    eq = '-2 3/7 - -5 7/10'

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
    else:
        operand1 = (operands[0].split(' ') if operands[0].find(' ') != -1 else
                    operands[0].split('/'))

        operand2 = (operands[1].split(' ') if operands[1].find(' ') != -1 else
                    operands[1].split('/'))

        print('%s %s'%(operand1, operand2))
        
        int_part = int(operand1[0]) if len(operand1) == 2 else 1

        num_part = (int(operand1[1].split('/')[0]) if len(operand1) == 2 else
                    int(operand1[0].split('/')[0]))

        dem_part = (int(operand1[1].split('/')[1]) if len(operand1) == 2 else
                    int(operand1[0].split('/')[1]))

        int_part2 = int(operand2[0]) if len(operand2) == 2 else 1

        num_part2 = (int(operand2[1].split('/')[0]) if len(operand2) == 2 else
                    int(operand2[0].split('/')[0]))

        dem_part2 = (int(operand2[1].split('/')[1]) if len(operand2) == 2 else
                    int(operand2[0].split('/')[1]))
        
         
    print('Целая часть:%s Числитель:%s Знаменатель:%s'%
          (int_part, num_part, dem_part))
    print('Целая часть:%s Числитель:%s Знаменатель:%s'%
          (int_part2, num_part2, dem_part2))
    
equfract()



















