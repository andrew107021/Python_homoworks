import clc_view

ERR_MSG = 'Wrong Input.Try again'


def query():
    global first, second
    flag = 0
    while not flag:
        try:
            first = float(clc_view.menu('Input first rational operand'))
        except ValueError:
            print(ERR_MSG)
        else:
            flag = 1
    flag = 0
    while not flag:
        try:
            second = float(clc_view.menu('Input second rational operand'))
        except ValueError:
            print(ERR_MSG)
        else:
            flag = 1
    while True:
        operator = clc_view.menu('Input operator (+,-,*,/)')
        if operator not in ('+', '-', '*', '/'):
            print(ERR_MSG)
        else:
            return calc(first, second, operator)


def calc(fst, scnd, op):
    global first, second
    if op == '+':
        return fst + scnd
    if op == '-':
        return fst - scnd
    if op == '*':
        return fst * scnd
    if op == '/':
        return fst / scnd
    if op == '**':
        return fst ** scnd


if __name__ == '__main__':
    first = 0 + 0j
    second = 0 + 0j
    print(query())
