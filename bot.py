
from webbrowser import get
import telebot;
import json
from printJson import printJson
from getCloth import getCloth 

bot = telebot.TeleBot('5111904045:AAEDPZLqKaacz7BFQV9Aohjj-5gmjEmoUCA');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет это интеллектуальный Бот по подбору ткани для штор, чем я могу тебе помочь? Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Интеллектуальный Бот по подбору ткани для штор. \n Список команд: \n /p - текст для анализа  - Положительные строны материала \n /n - текст для анализа  - Отрицательные строны материала \n /s - список всех тканей с описанием")
    elif str(message.text).lower() == "/s":
        aList=[]
        fileObject = open("data3.json", "r", encoding="UTF-8")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        str1 = printJson(aList)  
        bot.send_message(message.from_user.id, str1)
    elif splitted_text[0] == "/p":
        str1=""
        for item in splitted_text:
            if item!="/p":
                str1+=" " + item
        bot.send_message(message.from_user.id, getCloth(str1,"positive"))    
    elif splitted_text[0] == "/n":
        str1=""
        for item in splitted_text:
            if item!="/n":
                str1+=" " + item
        bot.send_message(message.from_user.id, getCloth(str1,"negative"))
    else:
        bot.send_message(message.from_user.id, "Привет интеллектуальный Бот по подбору ткани для штор, чем я могу тебе помочь? Для информации введите /help.")

bot.polling(none_stop=True, interval=0)