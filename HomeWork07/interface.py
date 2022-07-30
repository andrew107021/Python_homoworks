# import data_manager
#               0     1         2           3             4        -1
COMMAND_LST = 'Add, Search, Print all, Export file, Import file, Exit'.split(', ')
MENU_LINE = ('Available commands: ' + ', '.join(COMMAND_LST)) + '\n'


def menu() -> str:
    print('\n\n\n' + 'Simple phonebook\n'.center(100))
    print(MENU_LINE.center(100), sep='')
    return input('Enter a command: '.rjust(29)).lower()


def display(line: [str, dict]) -> None:
    if isinstance(line, str):
        print(f'\n{line.rjust(100)}\n')
    elif isinstance(line, dict):
        # print(*line)
        dict_print(line)
    else:
        print('Unknown format =(')


def dict_print(my_storage: dict) -> None:
    count = 0
    # tmp = []
    if my_storage:
        for i_key, i_val in my_storage.items():
            for unit in i_val:
                count += 1
                print(*unit.get('Name'), *unit.get('Phone'), unit.get('Dsc'))
    else:
        print('Empty storage')

'''
def print_all() -> None:
    data = data_manager.get_all()
    print(data)

'''
if __name__ == '__main__':
    """view module"""
    menu()
