import faker
import json
import os
import csv
import xlsxwriter


ext = {
    'json': 'json',
    'text': 'txt',
    'csv': 'csv',
    'xlsx': 'xlsx'
}


def export(data: [str, list, dict], fmt: str='text') -> None:
    place = os.path.abspath(os.curdir)
    place = os.path.join(place, ('phone_book.' + ext[fmt]))
    print(place)
    with open(place, 'w') as out_file:
        out_file.write(data)


export('this\nis\na\ntext\ntest_line')

