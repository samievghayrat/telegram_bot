import telebot
from telebot import types
bot = telebot.TeleBot("5662415327:AAHSyUwZM5kV8UaMaNN8qk6wwszDn84pY0I")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, " Hi, wassup", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('sample_png.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I dont understand you', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Wow, nice photo")

@bot.message_handler(commands=['website'])
def website(message):
   markup = types.InlineKeyboardMarkup()
   markup.add(types.InlineKeyboardButton("Open the website", url="https://www.youtube.com/watch?v=HodO2eBEz_8"))
   bot.send_message(message.chat.id, "Come to this website", reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
   markup = types.ReplyKeyboardMarkup()
   website = types.KeyboardButton("Website")
   start  =types.KeyboardButton("Start")
   markup.add(website, start)
   bot.send_message(message.chat.id, "Visit website2", reply_markup=markup)


   markup.add(types.InlineKeyboardButton("Open the website", url="https://www.youtube.com/watch?v=HodO2eBEz_8"))
   bot.send_message(message.chat.id, "Come to this website", reply_markup=markup)


bot.polling(none_stop=True)


