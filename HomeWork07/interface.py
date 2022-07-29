# import data_manager
#               0     1         2           3             4        -1
COMMAND_LST = 'Add, Search, Print all, Export file, Import file, Exit'.split(', ')
MENU_LINE = ('Available commands: ' + ', '.join(COMMAND_LST)) + '\n'


def menu() -> str:
    print('\n\n\n' + 'Simple phonebook\n'.center(100))
    print(MENU_LINE.center(100), sep='')
    return input('Enter a command: '.rjust(29)).lower()


def display(line: [str, list]) -> None:
    if isinstance(line, str):
        print(f'\n{line.rjust(100)}\n')
    elif isinstance(line, list):
        print(*line)
    else:
        print('Unknown format =(')


'''
def print_all() -> None:
    data = data_manager.get_all()
    print(data)

'''
if __name__ == '__main__':
    """view module"""
    menu()
