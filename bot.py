
from webbrowser import get
import telebot;
from getCloth import getCloth 

bot = telebot.TeleBot('5111904045:AAEDPZLqKaacz7BFQV9Aohjj-5gmjEmoUCA');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет это интеллектуальный Бот по подбору ткани для штор, чем я могу тебе помочь? Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Интллектуальный Бот по подбору ткани для штор. \n Список команд: \n /n - текст для анализа  - Положительные строны материала \n /p - текст для анализа  - Отрицательные строны материала \n /s - список всех тканей с описанием")
    elif splitted_text[0] == "/p":
        str1=""
        for item in splitted_text:
            if item!="/p":
                str1+=" " + item
        bot.send_message(message.from_user.id, getCloth(str1))
    else:
        bot.send_message(message.from_user.id, "Привет интеллектуальный Бот по подбору ткани для штор, чем я могу тебе помочь? Для информации введите /help.")

bot.polling(none_stop=True, interval=0)