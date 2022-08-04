def main_menu(commands: list) -> str:
    print(', '.join(commands))
    response = input('Type a command: ').strip().lower()
    return response or None


def display(line_in) -> None:
    print(line_in)


def print_dic(in_dict: [dict, list, str]) -> [str]:
    try:
        if isinstance(in_dict, dict):
            for i_key, i_val in in_dict.items():
                print('='*50)
                print(i_key[0] + ':')
                print_dic(i_val)
        elif isinstance(in_dict, list):
            for item in in_dict:
                print_dic(item)
        else:
            print(in_dict)
    except Exception as exc:
        return f'An error occurred: {exc}'
