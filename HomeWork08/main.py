import view
import data_part

COMMANDS = ['View children', 'View parents', 'Find', 'Reload', 'Exit']

view.display(data_part.read_data(flag=0))

while True:
    command = view.main_menu(COMMANDS)
    if command == COMMANDS[-1].lower():
        view.display('Exiting...')
        raise SystemExit()
    elif command == COMMANDS[0].lower():
        view.display(view.print_dic(data_part.children))
    elif command == COMMANDS[1].lower():
        view.display(view.print_dic(data_part.parents))
    elif command == COMMANDS[2].lower():
        pers = input('Enter person for search: ')
        if not pers.isspace() or pers not in (None, ''):
            result = data_part.seeker(pers)
            view.print_dic(result)
        else:
            view.display('Skipped by user')
    elif command == COMMANDS[3].lower():
        result = data_part.read_data(flag=1)
        view.print_dic(result) if isinstance(result, dict) else view.display(result)
    else:
        view.display('Wrong input')
