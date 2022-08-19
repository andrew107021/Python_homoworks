from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from candy_play import candy_play_cmp as cpc

import os

tkn_path = os.path.join(os.path.abspath(os.curdir), 'token.txt')
with open(tkn_path, 'r') as tk_fl:
    bot_token = tk_fl.read().strip()

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

START = 0
FIRST_STATE = 1
CANCELLING = 3


def start(update, context):
    context.bot.send_message(update.effective_chat.id, cpc.short_rules)
    msg = cpc.intro(update, context)
    print(msg)
    context.bot.send_message(update.effective_chat.id, msg)
    return FIRST_STATE


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Game over. Всего доброго.')
    return ConversationHandler.END


def numb(msg_in: str) -> [int, str]:
    try:
        return int(msg_in)
    except ValueError as exc:
        return f'Ошибка ввода {exc}. Повторите ввод.'


def user_move(update, context):
    msg = numb(update.message.text)
    if isinstance(msg, int):
        new_msg, status = cpc.human(update, context, msg)
        if not status:
            context.bot.send_message(update.effective_chat.id, new_msg)
            new_msg, status = cpc.bot_move(update, context)
            context.bot.send_message(update.effective_chat.id, new_msg)
            if status == 3:
                context.bot.send_message(update.effective_chat.id, 'Игра окончена. '
                                                                   '\nДля перезапуска введите /start')
                return ConversationHandler.END
        else:
            context.bot.send_message(update.effective_chat.id, new_msg)
    else:
        context.bot.send_message(update.effective_chat.id, msg)
    return FIRST_STATE


start_handler = CommandHandler('start', start)
cancel_handler = MessageHandler(Filters.text, cancel)
user_handler = MessageHandler(Filters.text, user_move)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={FIRST_STATE: [user_handler], CANCELLING: [cancel_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()

