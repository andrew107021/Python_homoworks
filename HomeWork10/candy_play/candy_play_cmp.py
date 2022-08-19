short_rules = \
'''
Играем в конфеты.
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
    if person == 1:
        update.message.reply_text(f'На столе: {candies} конфет'
                                  f'\nЖребий брошен. Ход Бота.')
        candies_amt = ai_player()
        candies -= candies_amt
        ret_line = f'Бот берет: {candies_amt} конфет' \
                   f'\nНа столе: {candies} конфет' \
                   f'\nСколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?'
        return ret_line
    else:
        ret_line = f'На столе: {candies} конфет' \
                   f'\nЖребий брошен. Ваш ход.' \
                   f'\nСколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?'
        return ret_line


def ai_player() -> int:
    """primitive AI"""
    global candies
    if candies < AMT_MAX:
        return candies
    elif candies - AMT_MAX > 1 and candies < AMT_MAX * 2:
        return candies % (AMT_MAX + 1)
    else:
        return AMT_MAX


def bot_move(update, context):
    global candies
    ret_line = ''
    if candies > 0:
        candies_amt = ai_player()
        candies -= candies_amt
        update.message.reply_text(f'Бот взял: {candies_amt} конфет')
        if candies > 0:
            return f'На столе: {candies} конфет' \
                   f'\nСколько конфет берёте (от 1 до 28), {update.effective_chat.first_name}?', 1
        else:
            return f'Бот побеждает и отбирает конфеты у Вас.', 3


def human(update, context, msg):
    """human capture and whole logic"""
    global candies
    if candies > 0:
        candies_amt = msg
        if candies_amt > AMT_MAX or candies_amt < 1:
            candies_amt = AMT_MAX if candies > AMT_MAX else candies
            update.message.reply_text(f'Количество за пределами дозволенного.'
                                      f'\nВы берете: {candies_amt} конфет')
        candies -= candies_amt
        if candies > 0:
            line_out = f'Вы взяли: {candies_amt} конфет' \
                       f'\nНа столе: {candies} конфет'
            return line_out, 0
        else:
            line_out = f'Вы взяли: {candies_amt} конфет' \
                       f'\nВы побеждаете и отбираете конфеты у Бота.'
            return line_out, 3
