hlp_calc, hlp_text = '', ''


def preload():
    import os
    global hlp_text, hlp_calc
    hlp_path = os.path.join(os.path.abspath(os.curdir), 'bot_help.txt')
    with open(hlp_path, 'r', encoding='utf-8') as hlp_fl:
        data = hlp_fl.read().split('# calc help\n')
        hlp_text = data[0]
        hlp_calc = data[1]


def short_help(update, context):
    """Short help printer"""
    context.bot.send_message(update.effective_chat.id, f'{hlp_text}')


def starter_func(update, context):
    """Say "hello" and print short help on start"""
    name = update.effective_chat.first_name
    context.bot.send_message(update.effective_chat.id, f'Hello, {name}\n{hlp_text}')


def time_send(update, context):
    """Sends current bot (server) time"""
    from datetime import datetime as dt
    out_text = dt.now().strftime('Время: %H:%M:%S/%Y.%m.%d')
    context.bot.send_message(update.effective_chat.id, out_text)


def calc_simple(update, context):
    """Simple calc based on 'eval' function"""
    msg = update.message.text.split('/calc')
    if msg[1]:
        update.message.reply_text(f'{msg[1]} = {eval(msg[1])}')
    else:
        update.message.reply_text(f'Отсутствует выражение для вычисления.')
        update.message.reply_text(hlp_calc)


def message_react(update, context):
    msg = update.message.text
    update.message.reply_text(f'Вы написали: "{msg}". Бот ожидает команды.')
    update.message.reply_text(hlp_text)
