# lesson3-3, hard

alphabet = tuple(map(chr, range(ord('А'), ord('Я')+1)))

def extract_fruits(file):
    '''
    Возвращает сортированный по алфавиту
    список фруктов из file
    '''
    with open(file, 'r', encoding='UTF-8') as fr:
        fruits = []
        fr_all = [fruit.strip() for fruit in fr]
        fr_all = [fruit for fruit in fr_all if len(fruit)]
        for letter in alphabet:
            fr_sorted = [fruit for fruit in fr_all if letter == fruit[0]]
            if len(fr_sorted):
                fruits.append({letter: fr_sorted})

    return fruits

def sort_fruits(fr_list):
    '''
    В зависимости от первой буквы названия
    фрукта, записывает его в соответсвующий файл
    '''
    for fruit in fr_list:
        for key, value in fruit.items():
            with open('fruits_' + key + '.txt',
                      'w', encoding='UTF-8') as fr_sort:

                fr_sort.write('\n\n'.join(value))

sort_fruits(extract_fruits('fruits.txt'))

