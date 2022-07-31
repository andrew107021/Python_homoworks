import json
import os
import logger

storage = {}
base_path = os.path.join(os.path.abspath(os.curdir), 'testing.json')
# think this preset could be placed into a separate configuration file (not really needed at this stage)


def read_book():
    err_menu = '''
    Input the correct path to file or "exit" to exit (case sensitive!):
    '''
    global storage
    global base_path
    while True:
        print(__name__ + ' Searching in: \n' + base_path)
        logger.logger(__name__ + ' Searching in: ' + base_path)
        try:
            with open(base_path, 'r') as in_fl:
                data = in_fl.read()
                break
        except FileNotFoundError as err:
            print(err)
            logger.logger(f'{__name__}: {err}')
            base_path = input(err_menu).rstrip()
            if base_path == 'exit':
                return "error reading and exited"
                # raise SystemExit

    storage = json.loads(data)


# command print section
def get_all() -> dict:
    logger.logger(__name__ + 'transferring the whole data.')
    return storage


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

    surname = input('Input surname (Enter to skip): ').replace(' ', '_')
    name = input('Input name (Enter to skip): ').replace(' ', '_')
    f_name = input('Input father\'s name (Enter to skip): ').replace(' ', '_')
    if surname or name or f_name:
        response = {'id': time_ns(), 'Name': [item for item in (surname, name, f_name) if item]}
        while True:
            phone_num = input('Input phone number(s) or "end" to finish: ').lower()
            if phone_num == 'end':
                break
            elif phone_num.replace('+', '').replace('(', '').replace(')', '').replace('-', '').isdigit():
                phone.append(phone_num)
            else:
                print('Wrong input.')
        response['Phone'] = phone
        response['Dsc'] = input('Input description: ') or 'No Description'
    print(response)
    if input('Save? (y/n)').lower() in ('y', 'yes'):
        saver(response)
        read_book()
    else:
        return '0'


def dump_json(file_name: str) -> None:
    global storage
    file_name = file_name.replace('.txt', '.json')
    print(file_name)
    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as out_fl:
            json.dump(storage, out_fl, indent=4, ensure_ascii=False,
                      sort_keys=True)  # ensure_ascii=False for cyrillic in file
            read_book()
    except Exception as exc:
        print(exc)


# Command search section
def seeker(person: str) -> [str, dict, list]:
    """
    The most basic searching mechanism.
    :param person: str
    :param key: str
    :return: str, dict, list: on conditions
    """
    response = 'Not found'
    person = person.split(' ')
    read_book()

    def inner_seek(in_key: str):
        nonlocal response
        for entry in storage[in_key]:
            if person[0] in entry['Name']:
                if len(person) == 3 and person[1] in entry['Name'] and person[2] in entry['Name']:
                    response.append(entry)
                elif len(person) == 2 and person[1] in entry['Name']:
                    response.append(entry)
                elif len(person) == 1 and person[0] in entry['Name']:
                    response.append(entry)
                elif len(person) > 3:
                    print('seek lvl 2.1.0', end='---> ')  # Debugging semaphore TODO: clear
                    print(*entry['Name'], *entry['Phone'])
                    response.append(entry)
        return response

    if person[0][0] in storage.keys():
        response = ['Found:']
        inner_seek(person[0][0])
        if response == ['Found:']:
            response = 'Nothing found.'
    return response


# Remove command section
def remover(person: str):
    global storage
    response = 0
    count = 0
    id_to_delete = 0

    rm_list: list = seeker(person)
    if isinstance(rm_list, str):
        return rm_list

    print(rm_list.pop(0))
    for item in rm_list:
        count += 1
        item['count'] = count
        print('=' * 80)
        print(
            'Number: ', item.get('count'), '\n',
            'id: ', str(item.get('id')), '\n',
            ' '.join(item.get('Name')), ' ',
            item.get('Dsc'), '\n',
            '\n'.join(item.get('Phone')), sep='')

    while True:
        mark = input('What entry to be deleted? Enter number or "cancel" to exit: ')
        if mark == 'cancel':
            response = f"{__name__}: Deletion cancelled by user."
            print('Deletion cancelled.')
            break
        else:
            try:
                mark = int(mark)
                if 0 < mark <= count:
                    break
                else:
                    print('No such number, try again please.')
            except ValueError as exc:
                print(f'Input error: {exc} try again please.')

    for item in rm_list:
        if item['count'] == mark:
            id_to_delete = item['id']
    for item in storage.get(person[0][0]):
        if item['id'] == id_to_delete:
            print(item)
            mark = input('Should this entry to be deleted (no backups available yet)? (Yes/No): ')
            if mark == 'Yes':
                storage.get(person[0][0]).remove(item)
                print(f"{item['Name']} removed successfully.")
                logger.logger(f"{__name__}: {item['Name']} removed successfully.")
                response = f"{__name__}: {item['Name']} removed successfully."
                print('Saving to disk...')
                dump_json(base_path)
            elif mark.lower() == 'no':
                logger.logger(f"{__name__}: {item['Name']} Deletion cancelled")
                response = f"{__name__}: {item['Name']} Deletion cancelled by user."
                print('Deletion cancelled.')
            else:
                logger.logger(f"{__name__}: {item['Name']} Not exact answer. Deletion cancelled.")
                response = f"{__name__}: {item['Name']} Not exact answer. Deletion cancelled."
                print('Not exact answer. Deletion cancelled')
    read_book()
    return response
