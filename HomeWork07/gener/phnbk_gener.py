import faker
import json
from random import randint as rint

fio = faker.Faker('ru_RU')

storage = {}
cnt = 1


def generate(amt=100):

    global storage
    extra = ('тов.', 'г-н', 'г-жа')
    for _ in range(amt):
        unit = {}
        line: str = fio.name()
        if line.startswith(extra):
            line = ' '.join(line.split()[1:])
        else:
            line = ' '.join(line.split())
        tmp = arrange(line)
        unit['Name'] = tmp
        unit['Phone'] = [phone for phone in phone_generator(rint(1, 3))]
        storage[hash(tmp[1])] = unit
        del tmp, unit


def arrange(line_in: str) -> list:
    global cnt

    suffixes = ('ов', 'ова', 'ев', 'ева', 'ив', 'ива')
    line_in = line_in.split()
    if line_in[-1].endswith(suffixes):
        line_in = [line_in[-1]] + line_in[:-1]
        # print(cnt, *line_in)
        cnt += 1
    return line_in


def phone_generator(amt):
    for _ in range(amt):
        phn = ''
        phn += '+7(' + str(rint(900, 999)) + ')' + str(rint(100_00_00, 999_99_99))
        yield phn


generate()
print(storage)
storage = json.dumps(storage)
with open('../phn_bk.txt', 'w') as out_fl:
    out_fl.write(str(storage))
