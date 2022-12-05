import telebot
from telebot import types
bot = telebot.TeleBot('5804162619:AAHof-vd0mE8A6Oyg-MPHw2ShemK2p9GW-8')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет,{message.from_user.first_name}'
    about_me = 'Я могу дать тебе информацию об языке программирования Python. \nС помощью меня ты можешь вспомнить всё что позабыл'
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, about_me)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("Переменные")
    item_2 = types.KeyboardButton("Функции")
    item_3 = types.KeyboardButton("Декораторы")
    item_4 = types.KeyboardButton("Циклы")
    item_5 = types.KeyboardButton("list comprehension")
    item_6 = types.KeyboardButton("tuple unpacking")
    item_7 = types.KeyboardButton("Как работает память")
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7)
    bot.send_message(message.chat.id,'Вот что я могу тебе подсказать',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Переменные":
            bot.send_message(message.chat.id, "Переменная — это именованная область памяти. После того как вы дали имя области, появляется возможность обращаться к данным, что в ней хранятся.")
            img_1 = open("perem.png",'rb')
            bot.send_photo(message.chat.id,img_1)
            bot.send_message(message.chat.id, 'Более подробно об переменных можно прочитать на - "https://pythonchik.ru/osnovy/peremennye-v-python"')
        if message.text == "Функции":
            bot.send_message(message.chat.id,"Функция — это набор инструкций, объединенных для выполнения одной задачи. Блоки кода, однажды оформленные в виде функций, можно использовать в коде многократно.")
            img_2 = open("func.png","rb")
            bot.send_photo(message.chat.id,img_2)
            bot.send_message(message.chat.id,"Более подробно о функциях можно прочитать на - 'https://highload.today/funktsii-python/'")
        if message.text == "Декораторы":
            bot.send_message(message.chat.id,"Декораторы в Python представляют функцию, которая в качестве параметра получает функцию и в качестве результата также возвращает функцию. Декораторы позволяют модифицировать выполняемую функцию, значения ее параметров и ее результат без изменения исходного кода этой функции.")
            bot.send_message(message.chat.id,'Почитать подробнее о декораторах можно на - https://medium.com/nuances-of-programming/%D0%B4%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D1%8B-%D0%B2-python-%D0%B7%D0%B0-%D1%82%D1%80%D0%B8-%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D1%8B-7bf1b5641886 /nА также на - https://tproger.ru/translations/demystifying-decorators-in-python/')
        if message.text == "Циклы":
            bot.send_message(message.chat.id,"Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого условия.")
            img_3 = open("for.png","rb")
            img_4 = open("while.jpg","rb")
            bot.send_photo(message.chat.id,img_3)
            bot.send_photo(message.chat.id,img_4)
            bot.send_message(message.chat.id,"Более подробно о циклах можно прочитать на - 'https://metanit.com/python/tutorial/2.7.php'")
        if message.text == "list comprehension":
            bot.send_message(message.chat.id,"List comprehension трудно перевести правильно на русский, потому, раз он генерирует новый список, будем называть его просто генератором списков. Это одна из самых приятных вещей в python, научившись писать которую, будешь применять её везде.")
            img_5 = open("list-comprehension.png","rb")
            bot.send_photo(message.chat.id,img_5)
            bot.send_message(message.chat.id,"Более подробно на - 'https://dvmn.org/encyclopedia/qna/5/chto-takoe-list-comprehension-zachem-ono-kakie-esche-byvajut/'")
        if message.text == "tuple unpacking":
            img_tuple = open("tuply.png","rb")
            bot.send_photo(message.chat.id,img_tuple)
            bot.send_message(message.chat.id,"Все об кортежах будет тут - 'https://www.bestprog.net/ru/2020/04/15/python-operations-on-tuples-bypass-of-tuple-methods-of-working-with-tuples-ru/'")
        if message.text == "Как работает память":
            bot.send_message(message.chat.id,"Ни одна компьютерная программа не может работать без данных. А данные, чтобы программа имела к ним доступ, должны располагаться в оперативной памяти вашего компьютера.")
            img_6 = open("memory.png","rb")
            bot.send_photo(message.chat.id,img_6)
            bot.send_message(message.chat.id, "Все об памяти и её работа е в Python тут - 'https://habr.com/ru/company/domclick/blog/530804/'")
bot.polling(none_stop=True)