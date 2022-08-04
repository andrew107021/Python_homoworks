import csv
import os

path_cld = os.path.join(os.curdir, 'children.csv')
path_prn = os.path.join(os.curdir, 'parents.csv')

children = {}
parents = {}


def read_data(flag=0) -> str:
    global parents
    global children
    if flag:
        print('RELOADING.'.center(100) + '\nCurrent dictionaries now cleared'.center(100))
        parents.clear()
        print('parents:\n', parents)
        children.clear()
        print('Children:\n', children)

    with open(path_cld, 'r') as cld:
        csv_rdr = csv.reader(cld, dialect='excel', delimiter=';')
        for i in csv_rdr:
            c_key = (i[2] + 'ы' if not i[2].endswith('а') else i[2][:-1] + 'ы', i[1])
            if c_key not in children:
                children[c_key] = [[' '.join((i[2], i[3], i[4])), i[0]]]
            else:
                children[c_key].append([' '.join((i[2], i[3], i[4])), i[0]])

    with open(path_prn, 'r') as prn:
        csv_rdr = csv.reader(prn, dialect='excel', delimiter=';')
        for i in csv_rdr:
            blood_line = [[' '.join((i[1], i[2], i[3])), i[0]], [' '.join((i[6], i[7], i[8])), i[4]]]
            parents[(i[1] + "ы" if not i[1].endswith('а') else i[2][:-1] + "ы", i[0])] = blood_line
    return f"Data loaded.\nChildren totally: {len(children)} units\nParents totally: {len(parents)} units"


def seeker(line_in: str, dict_in: [dict, list] = None):
    if dict_in is None:
        dict_in = children

    def parents_search(in_list: list):
        line_out = ''
        try:
            for f_key, f_val in in_list[0].items():
                print(f_val)
                line_out += f'\n\n{f_val[0][0]}:\n{"-"*50}\n'
                for card in parents[f_key]:
                    line_out += f'{card[0]}\n'
        except KeyError as exc:
            print(f'!!!!Parents not found: {exc}')
            return f'!!!!Parents not found: {exc}'
        else:
            return line_out

    found = []
    for i_key, i_val in dict_in.items():
        for item in i_val:
            if line_in in item[0]:
                found.append({i_key: i_val})
                break
    if len(found) == 1:
        return parents_search(found)
    else:
        print(f'Found {len(found)} units:')
        for f_item in found:
            print(f_item)
        question = '''
Need more definite data. Please enter
surname, name and middle-name: '''
        line_in_dbl = input(question)
        return seeker(line_in_dbl)
