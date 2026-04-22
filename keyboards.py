from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def poster_keyboard():
    keyboard = [
        [InlineKeyboardButton('История запросов', callback_data='history')]
    ]
    return InlineKeyboardMarkup(keyboard)


def menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Найти фильм', callback_data='search'),
         InlineKeyboardButton('История запросов', callback_data='history')]
    ]
    return InlineKeyboardMarkup(keyboard)

def search_keyboard():
    keyboard = [
        [InlineKeyboardButton('Найти фильм', callback_data='search')]
    ]
    return InlineKeyboardMarkup(keyboard)

def choose_movie_keyboard():
    keyboard = [
        [InlineKeyboardButton('1', callback_data='1'),
         InlineKeyboardButton('2', callback_data='2'),
         InlineKeyboardButton('3', callback_data='3')],
        [InlineKeyboardButton('4', callback_data='4'),
         InlineKeyboardButton('5', callback_data='5')]
    ]
    return InlineKeyboardMarkup(keyboard)
