import telebot

API_TOKEN = '5444090912:AAFu-pyN6gCKlrGfccrVxuxVoC5b0Jt7kGc'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am MusicCacherBot.
If you print me YouTube video URL-address I'll return good music\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
