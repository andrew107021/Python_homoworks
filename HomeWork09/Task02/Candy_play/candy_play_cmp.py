# AMT_MAX = 28
# names = tuple()
# candies = 56
short_rules = \
'''
Играем в конфеты.
Конфеты берутся командой: /take кол-во конфет
Можно взять от 1 до 28 штук. Если взять меньше 1 или больше 28,
считается что взял 28.
Бот берет конфеты сам, по тем же правилам.
Поехали.
'''

AMT_MAX = 28
DEFAULT_CANDIES = 112
candies = 0


def intro(update, context):
    """Start function. Start/restart game"""
    from random import randint as r_int
    global candies
    candies = DEFAULT_CANDIES
    person = r_int(0, 1)
    update.message.reply_text(short_rules)
    if person == 1:
        update.message.reply_text(f'На столе: {candies} конфет')
        update.message.reply_text('Жребий брошен. Ход Бота.')
        candies_amt = ai_player()
        candies -= candies_amt
        update.message.reply_text(f'Бот берет: {candies_amt} конфет')
        update.message.reply_text(f'На столе: {candies} конфет')
    else:
        update.message.reply_text(f'На столе: {candies} конфет')
        update.message.reply_text('Жребий брошен. Ваш ход.')
        update.message.reply_text(f'Сколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?')


def ai_player() -> int:
    """primitive AI"""
    global candies
    if candies < AMT_MAX:
        return candies
    elif candies - AMT_MAX > 1 and candies < AMT_MAX * 2:
        return candies % (AMT_MAX + 1)
    else:
        return AMT_MAX


def human(update, context):
    """human capture and whole logic"""
    global candies
    # update.message.reply_text(f'Сколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?')
    msg = update.message.text.split('/take ')
    if msg[1] and candies > 0:
        try:
            candies_amt = int(msg[1])
        except ValueError:
            update.message.reply_text(f'Только целые числа.')
            print('value error. Integers only')         # debug semaphore
        else:
            if candies_amt > AMT_MAX or candies_amt < 1:
                candies_amt = AMT_MAX if candies > AMT_MAX else candies
                update.message.reply_text(f'Количество за пределами дозволенного.'
                                          f'\nВы берете: {candies_amt} конфет')
            candies -= candies_amt
            if candies > 0:
                update.message.reply_text(f'Вы взяли: {candies_amt} конфет')
                update.message.reply_text(f'На столе: {candies} конфет')
            else:
                update.message.reply_text(f'Вы взяли: {candies_amt} конфет')
                update.message.reply_text(f'Вы побеждаете и отбираете конфеты у Бота.')
            if candies > 0:
                candies_amt = ai_player()
                candies -= candies_amt
                update.message.reply_text(f'Бот взял: {candies_amt} конфет')
                # update.message.reply_text(f'Сколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?')
                if candies > 0:
                    update.message.reply_text(f'На столе: {candies} конфет')
                    update.message.reply_text(f'Сколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?')
                else:
                    update.message.reply_text(f'Бот побеждает и отбирает конфеты у Вас.')
    elif candies == 0:
        update.message.reply_text(f'Игра была окончена, на столе нет конфет'
                                  f'\nДля начала игры введите /play')
    else:
        update.message.reply_text(f'Не найдено число конфет')

