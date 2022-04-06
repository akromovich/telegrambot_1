import telebot
from telebot import types

bot = telebot.TeleBot('5113498361:AAGwOV5HpPjbelfp4FqUmWZ7y5zRAYnA66M')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"привет")

@bot.message_handler(commands=["w"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('нажми',url="https://instagram.com"))
    bot.send_message(message.chat.id,"привет",reply_markup=markup)

bot.polling(none_stop=True)