class Person:
    def __init__(self, string):
        self._full_name = {
            'name': string.split()[0],
            'last_name': string.split()[1]
        }

    @property
    def get_full_name(self):
        return self._full_name


class Person_Card(Person):
    def __init__(self, string):
        Person.__init__(self, string)
        self._data = {
            'cash': string.split()[2],
            'job': string.split()[3],
            'norm': string.split()[4]
        }

    @property
    def get_card(self):
        return self._data


class Person_Work(Person):
    def __init__(self, string):
        Person.__init__(self, string)
        self._fact_work = string.split()[2]

    @property
    def get_fact_work(self):
        return self._fact_work


def parse_file(file, obj):
    with open(file, encoding='UTF-8') as lister:
        elems = [obj(elem) for elem in lister][1:]
        return elems


def join_tab(elems1, elems2):
    pass
