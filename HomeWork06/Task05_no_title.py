from typing import Callable


def print_operation_table(operation: Callable, num_rows: int = 9, num_columns: int = 9) -> None:
    table = [[operation(x, y) for y in range(1, num_columns+1)] for x in range(1, num_rows + 1)]
    wi = len(str(table[num_rows - 1][num_columns - 1])) + 1
    print('__|', '|'.join([f'{x}'.center(wi, '_') for x in range(1, num_columns+1)]), end='|\n')
    for row in table:
        print(table.index(row) + 1, end=' | ')
        ln = '|'.join([f'{x}'.ljust(wi) for x in row])
        print(ln, end='|\n', sep='')
    print()


print_operation_table(lambda x, y: x*y)
print_operation_table(lambda x, y: x+y, 5, 9)
print_operation_table(lambda x, y: x**y)

