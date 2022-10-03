import telebot
from telebot import types
from bs4 import BeautifulSoup as bs
import requests
import lxml



token = '5795816169:AAGGth1R_3OFDk5MhAECh6oGth343FLw9e0'
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def bot_func(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Знайти')
    button2 = types.KeyboardButton(text='/start')
    buttons.add(button1, button2)
    button_text = bot.send_message(message.chat.id, text='Знайти останнє аніме на сайті?', reply_markup=buttons)
    bot.register_next_step_handler(button_text, bot_action)


def bot_action(message):
    if message.text == 'Знайти':
        get_url(message)
    else:
        return


def get_url(message):
    url = 'https://www.anilibria.tv/'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    all_i_need = soup.find_all(class_="release-link")

    for i in all_i_need:
        i_href = i.get("href")

        bot.send_message(message.chat.id, text=f'https://www.anilibria.tv/{i_href}')


if __name__ == '__main__':
    bot.polling(none_stop=True)