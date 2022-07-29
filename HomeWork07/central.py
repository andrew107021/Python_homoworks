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
from interface import COMMAND_LST

data_manager.read_book()

while True:
    command = interface.menu()
    if command == COMMAND_LST[-1].lower():
        print('Exiting...'.rjust(22))
        raise SystemExit
    elif command == COMMAND_LST[1].lower():
        print('Calling searcher...'.rjust(31))
        interface.display(data_manager.seeker(input('Input a person: '.rjust(28))))
    elif command == COMMAND_LST[2].lower():
        print('Calling viewer...'.rjust(29))
        interface.display(data_manager.get_all())
    else:
        print('Wrong input.'.rjust(24))

