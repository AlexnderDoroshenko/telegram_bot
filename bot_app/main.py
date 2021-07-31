"""Main app module"""

from settings import TOKEN
import telebot


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.reply_to(message, "Привет, чем я могу тебе помочь?")
    else:
        bot.reply_to(message, "Я тебя не понимаю. Напиши /help.")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == "/start":
        bot.reply_to(message, "Пора тебе вернуть кнопки!!!")
    elif message.text == "/help":
        bot.reply_to(message, "Пожалуй я тебе помогу")


bot.polling(none_stop=True, interval=2)



