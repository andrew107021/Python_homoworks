#! /usr/bin/env python3
import interface
import data_manager
import logger
from interface import COMMAND_LST

data_manager.read_book()

while True:
    command = interface.menu()
    if command == COMMAND_LST[-1].lower():              # Exit
        logger.logger(f'Command: {command}')
        print('Exiting...'.rjust(22))
        raise SystemExit
    elif command == COMMAND_LST[0].lower():             # Add person TODO: more tests needed
        print('Calling adder...'.rjust(28))
        logger.logger(f'Command: {command}')
        data_manager.adder()
    elif command == COMMAND_LST[1].lower():             # Search person TODO: more tests needed
        print('Calling searcher...'.rjust(31))
        person = input('Input a person: '.rjust(28))
        logger.logger(f'Command: {command}; request: {person}')
        interface.display(data_manager.seeker(person))
    elif command == COMMAND_LST[2].lower():             # Print the whole phonebook
        print('Calling viewer...'.rjust(29))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.get_all())
    elif command == COMMAND_LST[3].lower():             # TODO: Export phonebook, still not ready
        print('Calling exporter...'.rjust(31))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.get_all())
    elif command == COMMAND_LST[4].lower():             # TODO: Import phonebook, still in work
        print('Calling importer...'.rjust(31))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.get_all())
    elif command == COMMAND_LST[5].lower():             # TODO: Remove, on testing
        print('Calling remover...'.rjust(30))
        logger.logger(f'Command: {command}')
        interface.display(data_manager.remover(input('Input a person: '.rjust(28))))

    else:
        logger.logger(f'Command: "{command}". Wrong input. Command does not exist.')
        print('Wrong input.'.rjust(24))

