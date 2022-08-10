import clc_view
import clc_complex
import clc_rational

main_menu = '1) Calculate rational\n' \
            '2) Calculate complex\n' \
            '0) Exit\n' \
            'Input number'

calculate_rational_menu = ''
calculate_complex_menu = ''


while True:
    command = clc_view.menu(main_menu, )
    if command not in ('1', '2', '0'):
        print('Wrong input. Try again.')
    elif command == '0':
        raise SystemExit
    elif command == '1':
        answer = clc_rational.query()
        clc_view.display(answer)
    elif command == '2':
        answer = clc_complex.query()
        clc_view.display(answer)
