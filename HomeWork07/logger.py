from datetime import datetime as dt
import os
log_path = base_path = os.path.abspath(os.curdir) + '/history.log'


def logger(log_line: str) -> None:
    log_line = dt.now().strftime('%Y.%m.%d at %H:%M:%S') + ' ' + log_line
    with open(log_path, 'a') as out_log:
        out_log.write(log_line + '\n')


if __name__ == '__main__':
    print(log_path)
    logger('test line')
