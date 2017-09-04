import telebot
import os

token = os.environ['TELEGRAM_TOKEN'] # or you can just type token from FatherBot here
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def message_handler(message):
  bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)