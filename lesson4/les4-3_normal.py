# lesson4-3, normal

import re
import random

with open('longnum.txt', 'w', encoding='UTF-8') as file:
    n = [str(random.randint(0, 9)) for _ in range(2499)]
    n = str(random.randint(1, 9)) + ''.join(n)
    file.write(n)

with open('longnum.txt', 'r', encoding='UTF-8') as file:
    result = ['0']
    longnum = file.readline()
    pattern = '([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
              '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})'
    found = re.findall(pattern, longnum)
    [result.insert(0, x) for x in found if len(x) > len(result[0])]
    print(result.pop(0))
