#  Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# - под форматами понимаем структуру файлов, например:
# в файле на одной строке хранится одна часть записи, пустая строка - разделитель
#
# *Фамилия_1*
#
# *Имя_1*
#
# *Телефон_1*
#
# *Описание_1*
#
# *Фамилия_2*
#
# *Имя_2*
#
# *Телефон_2*
#
# *Описание_2*
#
# *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***
#
# *Фамилия_1,Имя_1,Телефон_1,Описание_1*
#
# *Фамилия_2,Имя_2,Телефон_2,Описание_2*
#
# *и т.д.*
#
# ** (Модульность) Логирование, Главный файл и тд****
#
import interface
import data_manager
import logger
from interface import COMMAND_LST

data_manager.read_book()

while True:
    command = interface.menu()
    if command == COMMAND_LST[-1].lower():
        logger.logger(f'Command: {command}')
        print('Exiting...'.rjust(22))
        raise SystemExit
    elif command == COMMAND_LST[0].lower():
        print('Calling adder...'.rjust(31))
        logger.logger(f'Command: {command}')
        data_manager.adder()
    elif command == COMMAND_LST[1].lower():
        print('Calling searcher...'.rjust(31))
        person = input('Input a person: '.rjust(28))
        logger.logger(f'Command: {command}; request: {person}')
        interface.display(data_manager.seeker(person))
    elif command == COMMAND_LST[2].lower():
        print('Calling viewer...'.rjust(29))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.get_all())
    elif command == COMMAND_LST[3].lower():
        print('Calling exporter...'.rjust(29))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.get_all())
    elif command == COMMAND_LST[4].lower():
        print('Calling importer...'.rjust(29))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.get_all())

    else:
        logger.logger(f'Command: "{command}". Wrong input. Command does not exist.')
        print('Wrong input.'.rjust(24))

