import telegram
from key_buttons import button, faculty_button


def main_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(button[0]),
    telegram.KeyboardButton(button[1]),],
    [telegram.KeyboardButton(button[2]),
    telegram.KeyboardButton(button[3]),],
    [telegram.KeyboardButton(button[4]),
    telegram.KeyboardButton(button[5]),],
    ])

    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def faculty_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(faculty_button[0]),
    telegram.KeyboardButton(faculty_button[1]),],
    [telegram.KeyboardButton(faculty_button[2]),
    telegram.KeyboardButton(faculty_button[3]),],
    [telegram.KeyboardButton(faculty_button[4]),],
    ])

    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


