from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

import bot_functions
from Candy_play import candy_play_cmp as cpc

tkn_path = os.path.join(os.path.abspath(os.curdir), 'token.txt')
with open(tkn_path, 'r', encoding='utf-8') as tkn_fl:
    bot_token = tkn_fl.read().strip()

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

bot_functions.preload()


def main():

    # Basic commands handlers
    start_handler = CommandHandler('start', bot_functions.starter_func)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', bot_functions.short_help)
    dispatcher.add_handler(help_handler)

    time_handler = CommandHandler('time', bot_functions.time_send)
    dispatcher.add_handler(time_handler)

    # calculator handler
    calc_handler = CommandHandler('calc', bot_functions.calc_simple)
    dispatcher.add_handler(calc_handler)

    # candy-play handlers
    play_handler = CommandHandler('play', cpc.intro)
    dispatcher.add_handler(play_handler)

    take_handler = CommandHandler('take', cpc.human)
    dispatcher.add_handler(take_handler)

    # message handler
    msg_handler = MessageHandler(Filters.text, bot_functions.message_react)
    dispatcher.add_handler(msg_handler)

    updater.start_polling()     # start listening
    updater.idle()              # start idle circuit


if __name__ == '__main__':
    main()

