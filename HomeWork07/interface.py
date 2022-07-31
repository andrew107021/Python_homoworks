# import data_manager
#               0     1         2           3             4        -1
COMMAND_LST = 'Add, Search, Print all, Export file, Import file, Remove, Exit'.split(', ')
MENU_LINE = ('Available commands: ' + ', '.join(COMMAND_LST)) + '\n'


def menu() -> str:
    print('\n\n\n' + 'Simple phonebook\n'.center(100))
    print(MENU_LINE.center(100), sep='')
    return input('Enter a command: '.rjust(29)).lower()


def display(line: [str, dict, list]) -> None:
    if isinstance(line, str):
        print(f'\n{line.center(100)}\n')
    elif isinstance(line, dict):
        dict_print0(line)
    elif isinstance(line, list):
        if line[0] == 'Found:':
            line.pop(0)
        for entry in line:
            if isinstance(entry, dict):
                dict_print(entry)
            else:
                print('SOMETHING WRONG', entry)     # debugging semaphore TODO: clear
    else:
        print('Unknown format =(')     # debugging semaphore TODO: clear


def dict_print0(my_storage: dict) -> None:      # A rough CRUTCH TODO: fix
    if my_storage:
        for i_key, i_val in my_storage.items():
            for unit in i_val:
                print(*unit.get('Name'), *unit.get('Phone'), unit.get('Dsc'))
    else:
        print('Empty storage')


def dict_print(my_storage: dict) -> None:   # TODO: Still debugging
    if isinstance(my_storage, dict):
        f_name = '\n' + ' '.join(my_storage['Name']).center(100)
        phones = '\n'.join(x.center(100) for x in my_storage['Phone'])
        dscr = (my_storage['Dsc']).center(100) + '\n'
        print('\n'.join([f_name, phones, dscr]))
        # print(*my_storage['Name'], *my_storage['Phone'], my_storage['Dsc'])
    else:
        print('Wrong instance')


if __name__ == '__main__':
    """view module"""
    menu()
