def menu() -> str:
    print('Simple phonebook\n'.center(100))
    print('Available commands: Add,\nSearch,\nExport file,\nImport file\nExit'.center(100))
    return input('Enter a command: '.rjust(38)).lower()


def display(line: str) -> str:
    print('Simple phonebook\n'.center(100))
    print(f'\n{line.rjust(100)}\n')
    print('Available commands: Add, Search, Export file, Import file'.center(100))
    return input('Enter a command: '.rjust(38)).lower()
