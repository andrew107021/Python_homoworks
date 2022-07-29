import json
import os

base_path = '/large/data2/Home/Andrew/Documents/geekbrains/Python_20220705/Homeworks'
this_path = os.path.join(base_path, 'HomeWork07')
print(os.listdir(this_path))

try:
    with open(this_path + '/phn_bk.txt', 'r') as in_fl:
        data = in_fl.read()
except FileNotFoundError as err:
    print(err)
    raise SystemExit

my_storage = json.loads(data)

for i_key, i_val in my_storage.items():
    print('id:', i_key)
    for j_key, j_val in i_val.items():
        print(f'{j_key}:', *j_val)
    print('\n', '='*100, '\n', sep='')

print(my_storage.get('572052653667047361')['Name'][0])
print(my_storage.get('572052653667047361')['Name'][1])
print(my_storage.get('572052653667047361')['Phone'][0])
print(my_storage.get('572052653667047361')['Phone'][1])
