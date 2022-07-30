import json
import os

# base_path = '/large/data2/Home/Andrew/Documents/geekbrains/Python_20220705/Homeworks'
base_path = os.path.abspath(os.curdir)
this_path = os.path.join(base_path) + '/../phn_bk3.txt'

while True:
    print('Searching in: \n' + this_path)
    try:
        with open(this_path, 'r', encoding='utf-8') as in_fl:
            data = in_fl.read()
            break
    except FileNotFoundError as err:
        print(err)
        this_path = input('Input the correct path to file or "exit" to exit (case sensitive!):\n')
        if this_path == 'exit':
            raise SystemExit

my_storage = json.loads(data)

# for i_key, i_val in my_storage.items():
#     print('id:', i_key)
#     for j_key, j_val in i_val.items():
#         print(f'{j_key}:', *j_val)
#     print('\n', '='*100, '\n', sep='')
# #
# print(my_storage.get('572052653667047361')['Name'][0])
# print(my_storage.get('572052653667047361')['Name'][1])
# print(my_storage.get('572052653667047361')['Phone'][0])
# print(my_storage.get('572052653667047361')['Phone'][1])

# print(sorted(my_storage, key=my_storage.values()['Name'][0]))
tmp = []
for i_item in my_storage:
    if 'Ювеналий' in ' '.join(i_item.get('Name')):
        print(i_item)
    tmp.append(f"{i_item.get('Name')[0]:.<20} {' '.join(i_item.get('Phone')):<40}")

count = 0
for i in sorted(tmp):
    count += 1
    print(count, ') ', i, sep='')

