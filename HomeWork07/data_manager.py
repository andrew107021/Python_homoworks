import json
import os
my_storage = []
base_path = os.path.abspath(os.curdir) + '/testing.txt'


def read_book():
    global my_storage
    while True:
        print('Searching in: \n' + base_path)
        try:
            with open(base_path, 'r') as in_fl:
                data = in_fl.read()
                break
        except FileNotFoundError as err:
            print(err)
            this_path = input('Input the correct path to file or "exit" to exit (case sensitive!):\n')
            if this_path == 'exit':
                raise SystemExit

    my_storage = json.loads(data)


def get_all() -> list:
    return my_storage


def seeker(entry: str) -> str:
    return 'Search subsystem is under construction'


'''
tmp = []
for i_item in my_storage:
    if 'Ювеналий' in ' '.join(i_item.get('Name')):
        print(i_item)
    tmp.append(f"{i_item.get('Name')[0]:.<20} {' '.join(i_item.get('Phone')):<40}")

count = 0
for i in sorted(tmp):
    count += 1
    print(count, ') ', i, sep='')
'''
