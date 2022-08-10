def menu(menu_text: str, check: tuple = None) -> str:
    response = input(menu_text + ': ')
    return response


def display(in_line: str) -> None:
    print(in_line)


if __name__ == '__main__':
    ...
