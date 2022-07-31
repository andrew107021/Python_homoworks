import csv
import logger
import data_manager

data_manager.read_book()
storage = data_manager.storage
HEADLINE = ['id', 'Фамилия', 'Имя', 'Отчество', 'Примечание', 'Телефоны']


def rec_printer(in_instance: dict) -> str:      # Iterator function, uses yield
    def rearrange_name(fio):
        if len(fio) == 3: return fio
        elif len(fio) == 2: return [fio[0], fio[1], '--']
        else: return [fio[0], '--', '--']

    if isinstance(in_instance, dict):
        for i_k, i_v in in_instance.items():
            yield i_k
            yield from rec_printer(i_v)         # Recursive yield using
    if isinstance(in_instance, list):
        for j_v in in_instance:
            if isinstance(j_v, dict):
                line = f"\"{j_v['id']}\"", *rearrange_name(j_v['Name']), j_v['Dsc'], ', '.join(j_v['Phone'])
                if line:
                    yield line                  # yielding a result


def csv_exp(out_file: str) -> str:
    out_file += '.csv'
    if storage:
        with open(out_file, 'w', newline='', encoding='utf-8') as out_fl:
            spam_writer1 = csv.writer(out_fl, dialect='excel', delimiter=';', )
            spam_writer1.writerow(HEADLINE)
            for i in rec_printer(storage):
                print(*i)
                spam_writer1.writerow(i)
    else:
        logger.logger(f'{__name__}: Export error: empty storage')
        return f'Error: Empty storage'

    logger.logger(f'{__name__}: Storage dumped to {out_file}')
    return f'{__name__}: Storage dumped to {out_file}'


def txt_exp(out_file):
    out_file += '.txt'
    if storage:
        with open(out_file, 'w', newline='', encoding='utf-8') as out_fl:
            out_fl.write('{:<22} {:<20} {:<15} {:<22} {:<30} {}\n'.format(*HEADLINE))
            for i in rec_printer(storage):
                if isinstance(i, tuple):
                    line = f'{i[0]:<22} {i[1]:<20} {i[2]:<15} {i[3]:<22} {i[4]:<30} {i[5]}\n'
                    print(line)
                    out_fl.write(line)
                elif isinstance(i, str):
                    print(i)
                    out_fl.write(i + '\n')
    else:
        logger.logger(f'{__name__}: Export error: empty storage')
        return 'Error: Empty storage'

    logger.logger(f'{__name__}Storage dumped to {out_file}')
    return f'Storage dumped to {out_file}'


def exporter(file_nm, file_type):
    if file_nm == '':
        logger.logger(f'{__name__}: File name error.')
        return 'File name error.'
    if file_type == 'csv':
        response = csv_exp(file_nm)
    elif file_type == 'txt':
        response = txt_exp(file_nm)
    else:
        response = 'Unknown format.'
        logger.logger(f'{__name__}: Error {response}')
    return response


if __name__ == '__main__':
    exporter(input('Input file name: '), input('Input file type (csv/txt): '))
