from bs4 import BeautifulSoup
from urllib import request
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from cred import TOKEN
from menu import main_menu_keyboard, faculty_menu_keyboard
from key_buttons import button, faculty_button
from test import *


def start(update:  Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFO3NiyVIBAiciv6IvAAF2LNltyWNK8V8AAkEAA33smAfpT7DINbCxqikE'
    )
    update.message.reply_text(
        'Добро пожаловать, {username}'.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user
        ),
        reply_markup=main_menu_keyboard()             
    )


ABOUT_US = r'(?=('+(button[0])+r'))'
FACULTY = r'(?=('+(button[1])+r'))'
LOCATION = r'(?=('+(button[2])+r'))'
FAQ = r'(?=('+(button[3])+r'))'
ZAPIS = r'(?=('+(button[4])+r'))'
NEWS = r'(?=('+(button[5])+r'))'

ENGINEER = r'(?=('+(faculty_button[0])+r'))'
HUMANITARIAN = r'(?=('+(faculty_button[1])+r'))'
ECONOMY = r'(?=('+(faculty_button[2])+r'))'
MEDICINE = r'(?=('+(faculty_button[3])+r'))'
BACK_KEY = r'(?=('+(faculty_button[4])+r'))'

def faculty_menu(update:Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgEAAxkBAAEFQltizpB3B63BXkQfZdd7ddWfDxj2jAACLgAD9u8uLQVI2s_HbVEoKQQ'
    )
    update.message.reply_text(
        'Выберите факультет',
        reply_markup=faculty_menu_keyboard()
    )

def location(update:Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFQmFizpISHyV30fbL7SAV6hUpZcYQpAACvREAAuZ-CEn8akf161F9uCkE'
    )
    
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = """Международный университет Ала-Tоо, ул.Анкара 1/8, Тунгуч, 720048, Бишкек, Кыргызстан
Тел: +996 (312) 631425
Факс: +996 (312) 630409
E-mail: info@alatoo.edu.kg
Общественный транспорт: 5,6, 7, 102, 105, 128, 137, 147, 154, 166, 258, 262"""
    )
    
    update.message.reply_location(
        longitude=74.68120527078092,
        latitude=42.855851214199525,
        reply_to_message_id=msg.message_id
    )

def about_us(update:Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFNrxixru2-XWGUMP249aIzssR3K28CwACkQkAAli0IQAB7Bfptj-Da5spBA'
    )
    
    update.message.reply_text(
        '''
Наш университет состоит из пяти блоков, где имеются аудитории и лаборатории, оснащенные интернетом и современными интерактивными досками. Наш «Городок» является образовательным центром с библиотекой, конференц-залом, 3 стадионами, 1 теннисным кордом, 1 спортивным залом, 6 компьютерными классами, 1 интернет клубом, 1 научно-исследовательским центром, 2 кантинами, 1 медицинским центром.
В МУА имеются 4 факультета, 3 института и 16 кафедр.
Профилирующим языком обучения является английский. Русский, кыргызский и турецкий языки являются вспомогательными языками.  Кроме этого, студенты отдельных факультетов могут выбрать второй иностранный язык, на их выбор предоставляются японский, немецкий, китайский, французский языки. Для тех, кто не владеет английским языком, имеются подготовительные курсы. По окончании университета выдается диплом государственного образца о высшем профессиональном образовании Кыргызской Республики.
В университете обучаются студенты из более 20 стран мира.
С целью укрепления своих позиций на рынке образовательных услуг, университет работает над открытием новых образовательных программ, которые востребованы в новых информационно-конкурентоспособных условиях.

Больше вы можете прочесть на этом сайте:
http://alatoo.edu.kg/view/public/pages/page.xhtml;jsessionid=xc2p3HzchRmaEQG1ioOW_VfkndDc3kZrL8BZHrWS.unknown-host?id=3781#gsc.tab=0
    ''',
        reply_markup=main_menu_keyboard()  
    )


def resive_faq(update:Update, context: CallbackContext):
    
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFO2FiyUn9aG79JKbacqC9_YZLwjM17AAC0gEAAsVnCAABgpzLsIjCkgcpBA'
    )
    
    update.message.reply_text(
        '''
Страничка с ответами на часто задаваемые вопросы
http://eas.alatoo.edu.kg/view/public/pages/page.xhtml;jsessionid=xWuB0DPXzPSv1ymz2TguzQgfvk88QxrLv94BDMRo.unknown-host?id=8708
    ''',
        reply_markup=main_menu_keyboard()  

    )

def zapisat(update: Update, context: CallbackContext):

    z = update.message.text
    if z[:6] == 'Вопрос':
        context.bot.send_message(
            chat_id= '@alatoo_bo',
            text = z
        )

def zapis(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFO3FiyVFty0VGA8JJKQ0lZ5ayjoBK5wACRQADfeyYBwsgFRlEjN5FKQQ'
    )
    
    info = re.match(ZAPIS, update.message.text)
    update.message.reply_text(
    text = """
1. Напишите сообщение с "Вопрос: " и ваше имя.
2. Ваш номер телефона
После отправки вашего вопроса Администратор вам ответит.
"""
 )


def news_menu(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFQl9izpGAnfL64y4l4kK_ctak3NiNpgACFAADsp0FFr6eZ05nHpEcKQQ'
    )
    
    update.message.reply_text(l[0])


def engineer_fac(update:Update, context: CallbackContext):
    keyboard_hum = [
        [
            InlineKeyboardButton('Куратор', callback_data='engineer_curator'),
            InlineKeyboardButton('Цены', callback_data='engineer_price'),
            InlineKeyboardButton('Направления', callback_data='engineer_direction'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_hum)
    update.message.reply_text(
        'Выберете опцию',
        reply_markup=reply_markup
    )


def humanitarian_fac(update:Update, context: CallbackContext):
    keyboard_hum = [
        [
            InlineKeyboardButton('Куратор', callback_data='humanitarian_curator'),
            InlineKeyboardButton('Цены', callback_data='humanitarian_price'),
            InlineKeyboardButton('Направления', callback_data='humanitarian_direction'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_hum)
    update.message.reply_text(
        'Выберете опцию',
        reply_markup=reply_markup
    )

def economy_fac(update:Update, context: CallbackContext):
    keyboard_ec = [
        [
            InlineKeyboardButton('Куратор', callback_data='economy_curator'),
            InlineKeyboardButton('Цены', callback_data='economy_price'),
            InlineKeyboardButton('Направления', callback_data='economy_direction'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_ec)
    update.message.reply_text(
        'Выберете опцию',
        reply_markup=reply_markup
    )

def medicine_fac(update:Update, context: CallbackContext):
    keyboard_med = [
        [
            InlineKeyboardButton('Куратор', callback_data='medicine_curator'),
            InlineKeyboardButton('Цены', callback_data='medicine_price'),
            InlineKeyboardButton('Направления', callback_data='medicine_direction'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_med)
    update.message.reply_text(
        'Выберете опцию',
        reply_markup=reply_markup
    )

def button(update:Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'engineer_curator':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/tony.jpg', 'rb'),
            caption = """
ФИО: Тони Старк
Возраст: 52
Опыт преподования: 22   
            
            """
        )
    
    if query.data == 'engineer_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1100 - 2000$
                '''
        )
    
    if query.data == 'engineer_direction':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1.Информатика и вычислительная техника
2.Электроника и наноэлектроника
3.Прикладная математика и информатика
                '''
        )


    if query.data == 'humanitarian_curator':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/cap.jpg', 'rb'),
            caption = """
ФИО: Стив Роджерс
Возраст: 92
Опыт преподования: 4  
            
            """
        )
    
    if query.data == 'humanitarian_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
650 - 1500$
                '''
        )

    if query.data == 'humanitarian_direction':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1.Лингвистика (перевод и переводоведение)	
2.Филология (английский язык и литература)
3.Психология
4.Педагогика (педагогика и методика начального образования)	
5.Журналистика
                '''
        )


    if query.data == 'economy_curator':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/hulk.webp', 'rb'),
            caption = """
ФИО: Брюс Беннер
Возраст: 47
Опыт преподования: 15  
            
            """
        )
    
    if query.data == 'economy_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1700 - 1900$
                '''
            )

    if query.data == 'economy_direction':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
  
1.Экономика (Международная Экономика и Бизнес)
2.Международные отношения
3.Менеджмент
4.Экономика (финансы и кредит)
5.Международное право 
                '''
            )
    
    if query.data == 'medicine_curator':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/strange.webp', 'rb'),
            caption = """
ФИО: Стэфан Стрендж
Возраст: 47
Опыт преподования: 20            
            """
            )
    
    if query.data == 'medicine_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1700 - 1900$
                '''
            )

    if query.data == 'medicine_direction':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1.Лечебное дело
2.Педиатрия
                '''
            )
    


updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot-data'))
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT_US),
    about_us
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(FACULTY),
    faculty_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ENGINEER),
    engineer_fac
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HUMANITARIAN),
    humanitarian_fac
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ECONOMY),
    economy_fac
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MEDICINE),
    medicine_fac
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_KEY),
    start
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(FAQ),
    resive_faq
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAPIS),
    zapis
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(NEWS),
    news_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
))





# updater.dispatcher.add_handler(CallbackQueryHandler(faculty_button))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()