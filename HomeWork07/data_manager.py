import json
import os
import logger
my_storage = []
storage = {}
base_path = os.path.join(os.path.abspath(os.curdir), 'testing.json')
# think this preset could be placed into a separate file


def read_book():
    err_menu = '''
    Input the correct path to file or "exit" to exit (case sensitive!):
    '''
    global storage
    global base_path
    while True:
        print(__name__ + 'Searching in: \n' + base_path)
        logger.logger(__name__ + 'Searching in: ' + base_path)
        try:
            with open(base_path, 'r') as in_fl:
                data = in_fl.read()
                break
        except FileNotFoundError as err:
            print(err)
            logger.logger(f'{err}')
            base_path = input(err_menu).rstrip()
            if base_path == 'exit':
                return "error"
                # raise SystemExit

    # my_storage = json.loads(data)
    storage = json.loads(data)


# command print section
def get_all() -> dict:
    logger.logger(__name__ + 'transferring the whole data.')
    return storage


def seeker(entry: str) -> str:
    logger.logger(__name__ + f' searching "{entry}"' + ' this module is still under construction.')
    return 'Search subsystem is under construction'


# Command Add section
def saver(unit_in: dict) -> None:
    global storage
    if unit_in['Name'][0][0] not in storage.keys():
        storage[unit_in['Name'][0][0]] = [unit_in]
    else:
        (storage[unit_in['Name'][0][0]]).append(unit_in)
    print('Saving to disk...')
    dump_json(base_path)


def adder() -> [str, dict]:
    from time import time_ns
    response = '0'
    phone = []

    surname = input('Input surname (Enter to skip): ')
    name = input('Input name (Enter to skip): ')
    f_name = input('Input father\'s_name (Enter to skip): ')
    if surname or name or f_name:
        response = {'id': time_ns(), 'Name': [item for item in (surname, name, f_name) if item]}
        while True:
            phone_num = input('Input phone number(s) or "end" to finish: ').lower()
            if phone_num == 'end':
                break
            elif phone_num.replace('+', '').replace('(', '').replace('+', ')').isdigit():
                phone.append(phone_num)
            else:
                print('Wrong input')
        response['Phone'] = phone   # [phone for phone in phone_generator(rint(1, 3))]
        response['Dsc'] = input('Input description: ') or 'No Description'
    print(response)
    if input('Save? (y/n)').lower() in ('y', 'yes'):
        saver(response)
    else:
        return '0'
    # return response


def dump_json(file_name: str) -> None:
    global storage
    file_name = file_name.replace('.txt', '.json')
    print(file_name)
    # print(storage)
    # storage = json.dumps(storage, indent=4, ensure_ascii=False, sort_keys=True)  # ensure_ascii=False for cyrillic
    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as out_fl:
            # out_fl.write(str(storage))
            # out_fl.write(str(storage))
            json.dump(storage, out_fl, indent=4, ensure_ascii=False, sort_keys=True)  # ensure_ascii=False for cyrillic in file
    except Exception as exc:
        print(exc)


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
